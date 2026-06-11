"""Bob AI - Streamlit Chat Application

A simple Streamlit-based AI assistant for Indonesian language productivity tasks.
"""

import streamlit as st
from google import genai
import pdfplumber

# API key dari environment variable
import os

API_KEY = os.getenv("GEMINI_API_KEY")

# Konfigurasi halaman
st.set_page_config(page_title="Bob AI", page_icon="🤖", layout="centered")
st.title("🤖 Bob AI")
st.caption("Asisten Produktivitas Berbahasa Indonesia")

# System prompt
SYSTEM_PROMPT = """Kamu adalah Bob AI, asisten produktivitas berbahasa Indonesia.
Tugasmu membantu pengguna meringkas dokumen, membuat jadwal belajar,
memperbaiki tulisan, dan menjawab pertanyaan sehari-hari.
Jawab dengan bahasa Indonesia yang jelas, singkat, dan mudah dipahami.
Selalu akhiri jawaban dengan kalimat:
'Periksa sumber resminya ya untuk memastikan keakuratan informasi ini.'"""

# Inisialisasi riwayat di session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "riwayat_gemini" not in st.session_state:
    st.session_state.riwayat_gemini = []

if "pdf_dimuat" not in st.session_state:
    st.session_state.pdf_dimuat = False

# Sidebar upload PDF
with st.sidebar:
    st.header("📄 Upload Dokumen PDF")
    uploaded_file = st.file_uploader("Pilih file PDF", type=["pdf"])

    if uploaded_file and not st.session_state.pdf_dimuat:
        with st.spinner("Membaca PDF..."):
            try:
                with pdfplumber.open(uploaded_file) as pdf:
                    teks = ""
                    for halaman in pdf.pages:
                        teks += halaman.extract_text() or ""
                if teks.strip():
                    PESAN_PDF = (
                        f"Berikut isi dokumen '{uploaded_file.name}':\n\n"
                        f"{teks[:3000]}\n\n"
                        "Konfirmasi bahwa kamu sudah membaca dokumen ini."
                    )
                    st.session_state.riwayat_gemini.append(
                        {"role": "user", "parts": [{"text": PESAN_PDF}]}
                    )
                    # Dapatkan konfirmasi dari Gemini
                    client = genai.Client(api_key=API_KEY)
                    response = client.models.generate_content(
                        model="gemini-3.5-flash",
                        contents=st.session_state.riwayat_gemini,
                        config={"system_instruction": SYSTEM_PROMPT},
                    )
                    konfirmasi = response.text
                    st.session_state.riwayat_gemini.append(
                        {"role": "model", "parts": [{"text": konfirmasi}]}
                    )
                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": f"📄 **{uploaded_file.name}** berhasil dibaca!\n\n{konfirmasi}",
                        }
                    )
                    st.session_state.pdf_dimuat = True
                    st.success("PDF berhasil dimuat!")
            except IOError as e:
                st.error(f"Error reading PDF: {e}")
            except Exception as e:
                st.error(f"Error: {e}")

    if st.session_state.pdf_dimuat:
        st.success("✅ PDF sudah dimuat")

    st.divider()
    if st.button("🗑️ Reset Percakapan"):
        st.session_state.messages = []
        st.session_state.riwayat_gemini = []
        st.session_state.pdf_dimuat = False
        st.rerun()

# Tampilkan riwayat chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input chat
if prompt := st.chat_input("Ketik pertanyaan kamu di sini..."):
    # Tampilkan pesan user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Tambahkan ke riwayat Gemini
    st.session_state.riwayat_gemini.append(
        {"role": "user", "parts": [{"text": prompt}]}
    )

    # Kirim ke Gemini
    with st.chat_message("assistant"):
        with st.spinner("Bob AI sedang berpikir..."):
            try:
                client = genai.Client(api_key=API_KEY)
                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=st.session_state.riwayat_gemini,
                    config={"system_instruction": SYSTEM_PROMPT},
                )
                jawaban = response.text
                st.markdown(jawaban)
                st.session_state.riwayat_gemini.append(
                    {"role": "model", "parts": [{"text": jawaban}]}
                )
                st.session_state.messages.append(
                    {"role": "assistant", "content": jawaban}
                )
            except genai.errors.APIError as e:
                st.error(f"API Error: {e}")
            except Exception as e:
                st.error(f"Error: {e}")
