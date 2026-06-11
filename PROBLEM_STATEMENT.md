# Problem Statement - Bob AI

## Nama AI Assistant
**Bob AI** - Asisten Produktivitas Berbahasa Indonesia

## Target User
Mahasiswa Indonesia yang membutuhkan bantuan dalam:
- Meringkas dokumen akademik
- Membuat jadwal belajar
- Memperbaiki tulisan
- Menjawab pertanyaan sehari-hari terkait produktivitas

## Problem Statement

### Masalah Utama
Mahasiswa Indonesia sering menghadapi tantangan dalam mengelola informasi dari berbagai sumber dokumen (PDF, DOCX) dan membutuhkan alat yang dapat:
1. Membaca dan memahami dokumen dalam bahasa Indonesia
2. Menjawab pertanyaan berdasarkan konteks dokumen yang diberikan
3. Memberikan jawaban yang akurat dan terpercaya
4. Menghindari halusinasi (informasi yang tidak berdasarkan sumber)

### Solusi yang Ditawarkan
Bob AI menggunakan teknik **Retrieval-Augmented Generation (RAG)** dengan fitur:
- **Query Expansion**: Memperluas pertanyaan untuk pencarian yang lebih komprehensif
- **Semantic Search**: Pencarian berbasis makna menggunakan embedding
- **Reranking**: Mengurutkan hasil pencarian dengan BM25 untuk relevansi yang lebih tinggi
- **Context Compression**: Mengompresi konteks yang diambil agar lebih fokus
- **Guardrails**: Mencegah halusinasi dengan membatasi jawaban hanya berdasarkan konteks

### Teknologi yang Digunakan
- **LLM**: Google Gemini 3.5 Flash
- **Vector Database**: ChromaDB dengan Sentence Transformer (all-MiniLM-L6-v2)
- **Reranking**: BM25Okapi
- **Document Processing**: pdfplumber, python-docx
- **UI Framework**: Streamlit (untuk versi web)

### Tujuan Proyek
Membuat asisten AI yang dapat membantu mahasiswa Indonesia dalam:
- Memahami dokumen akademik dengan cepat
- Mendapatkan jawaban yang akurat berdasarkan sumber dokumen
- Meningkatkan produktivitas belajar
- Mengurangi risiko mendapatkan informasi yang salah (halusinasi)

### Batasan Proyek
- Hanya menjawab berdasarkan dokumen yang dimuat
- Tidak dapat mengakses internet secara real-time
- Bahasa utama: Bahasa Indonesia
- Format dokumen yang didukung: PDF, DOCX
