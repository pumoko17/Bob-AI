from google import genai
from dotenv import load_dotenv
import os

# Ambil API key dari file .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: API key tidak ditemukan di file .env")
    print("Pastikan file .env sudah ada dan isinya: GEMINI_API_KEY=api_key_kamu")
    exit()

client = genai.Client(api_key=api_key)

# Identitas Bob AI
SYSTEM_PROMPT = """Kamu adalah Bob AI, asisten produktivitas berbahasa Indonesia.
Tugasmu membantu pengguna meringkas dokumen, membuat jadwal belajar,
memperbaiki tulisan, dan menjawab pertanyaan sehari-hari.
Jawab dengan bahasa Indonesia yang jelas, singkat, dan mudah dipahami.
Selalu akhiri jawaban dengan kalimat:
'Periksa sumber resminya ya untuk memastikan keakuratan informasi ini.'"""

# Buat sesi chat
chat = client.chats.create(
    model="gemini-3.5-flash",
    config={"system_instruction": SYSTEM_PROMPT}
)

# Tampilan awal
print("=" * 52)
print("  Halo! Saya Bob AI, asisten produktivitas kamu.")
print("  Ketik 'keluar' untuk mengakhiri percakapan.")
print("  Ketik 'baca:namafile.pdf' untuk membaca PDF.")
print("=" * 52)

# Loop percakapan
while True:
    pertanyaan = input("\nKamu  : ")

    if pertanyaan.strip().lower() == "keluar":
        print("\nBob AI: Sampai jumpa! Semangat belajarnya ya.")
        break

    if pertanyaan.strip() == "":
        continue

    # Fitur baca PDF
    if pertanyaan.strip().lower().startswith("baca:"):
        nama_file = pertanyaan.strip()[5:].strip()
        if not os.path.exists(nama_file):
            print(f"\nBob AI: File '{nama_file}' tidak ditemukan. Pastikan file ada di folder bob_AI.")
            continue
        try:
            import pdfplumber
            with pdfplumber.open(nama_file) as pdf:
                teks = ""
                for halaman in pdf.pages:
                    teks += halaman.extract_text() or ""
            if not teks.strip():
                print("\nBob AI: File PDF tidak bisa dibaca atau kosong.")
                continue
            print(f"\nBob AI: File '{nama_file}' berhasil dibaca ({len(pdf.pages)} halaman). Silakan tanya apa saja tentang isinya!")
            response = chat.send_message(f"Berikut isi dokumen yang perlu kamu pahami:\n\n{teks[:3000]}\n\nKonfirmasi bahwa kamu sudah membaca dokumen ini.")
            print(f"\nBob AI: {response.text}")
        except ImportError:
            print("\nBob AI: Library pdfplumber belum terinstall.")
            print("Ketik perintah ini di terminal: pip install pdfplumber")
        continue

    response = chat.send_message(pertanyaan)
    print(f"\nBob AI: {response.text}")