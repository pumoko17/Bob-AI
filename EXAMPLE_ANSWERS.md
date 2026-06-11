# Contoh Jawaban AI - Bob AI

## Contoh 1: Pertanyaan tentang Definisi Bob AI

**Pertanyaan User:**
"Apa itu Bob AI dan apa fungsinya?"

**Retrieved Context:**
- Chunk 1 dari S01_Ide_AI_Assistant_Bob.docx (Score: 8.4521)
- Chunk 2 dari S01_Ide_AI_Assistant_Bob.docx (Score: 7.2341)

**Jawaban Bob AI:**
Bob AI adalah asisten produktivitas berbahasa Indonesia yang dirancang khusus untuk membantu mahasiswa dalam kegiatan belajar sehari-hari. Fungsi utama Bob AI meliputi:

1. **Meringkas dokumen** - Membantu mahasiswa memahami isi dokumen akademik dengan cepat
2. **Membuat jadwal belajar** - Membantu merencanakan jadwal belajar yang efektif
3. **Memperbaiki tulisan** - Memberikan saran perbaikan untuk tulisan akademik
4. **Menjawab pertanyaan** - Menjawab pertanyaan sehari-hari terkait produktivitas belajar

Bob AI menggunakan teknik Retrieval-Augmented Generation (RAG) untuk memberikan jawaban yang akurat berdasarkan dokumen yang dimuat, sehingga mengurangi risiko halusinasi.

Periksa sumber resminya ya untuk memastikan keakuratan informasi ini.

**Sumber dokumen:**
- S01_Ide_AI_Assistant_Bob.docx

---

## Contoh 2: Pertanyaan tentang Komponen RAG

**Pertanyaan User:**
"Apa saja komponen utama dalam workflow RAG yang digunakan Bob AI?"

**Retrieved Context:**
- Chunk 1 dari S06_Retrieval_Semantic_Search_Plan.docx (Score: 9.1234)
- Chunk 2 dari S06_Retrieval_Semantic_Search_Plan.docx (Score: 8.5678)
- Chunk 3 dari S06_Retrieval_Semantic_Search_Plan.docx (Score: 7.8901)

**Jawaban Bob AI:**
Workflow RAG Bob AI terdiri dari 5 komponen utama:

1. **Query Expansion** - Memperluas pertanyaan asli menjadi 3-4 variasi untuk meningkatkan recall dalam pencarian

2. **Retrieval (Semantic Search)** - Menggunakan ChromaDB dengan embedding model Sentence Transformer (all-MiniLM-L6-v2) untuk mencari chunk yang relevan secara semantik

3. **Reranking (BM25)** - Mengurutkan ulang hasil pencarian menggunakan algoritma BM25 untuk meningkatkan presisi dan memilih top-3 chunk paling relevan

4. **Context Compression** - Mengompresi retrieved context menggunakan LLM untuk menghilangkan informasi yang tidak relevan dan fokus pada bagian yang terkait dengan pertanyaan

5. **Generation** - Menggunakan Google Gemini 3.5 Flash untuk menghasilkan jawaban berdasarkan konteks yang telah dikompresi

Komponen-komponen ini bekerja bersama untuk memastikan jawaban yang diberikan akurat, relevan, dan berbasis pada sumber dokumen yang dimuat.

Periksa sumber resminya ya untuk memastikan keakuratan informasi ini.

**Sumber dokumen:**
- S06_Hizkia Reinaldy_24110400036_Retrieval_Semantic_Search_Plan.docx

---

## Contoh 3: Pertanyaan tentang Guardrails

**Pertanyaan User:**
"Bagaimana Bob AI mencegah halusinasi dalam memberikan jawaban?"

**Retrieved Context:**
- Chunk 1 dari S02_Prompt_and_Safety_Plan_Bob.docx (Score: 8.9876)
- Chunk 2 dari S02_Prompt_and_Safety_Plan_Bob.docx (Score: 7.6543)

**Jawaban Bob AI:**
Bob AI menerapkan beberapa mekanisme guardrails untuk mencegah halusinasi:

1. **Constraint-based Answering** - System prompt secara eksplisit memerintahkan Bob AI untuk hanya menjawab berdasarkan konteks dokumen yang diberikan

2. **Explicit Refusal** - Jika jawaban tidak tersedia dalam konteks, Bob AI akan memberitahu secara jujur bahwa informasi tersebut tidak tersedia dalam dokumen

3. **Source Attribution** - Setiap jawaban dilengkapi dengan daftar sumber dokumen yang digunakan, sehingga user dapat memverifikasi informasi

4. **Disclaimer Statement** - Setiap jawaban diakhiri dengan kalimat: "Periksa sumber resminya ya untuk memastikan keakuratan informasi ini" untuk mengingatkan user untuk verifikasi

5. **Context-based Generation** - LLM hanya menerima konteks yang telah melalui proses retrieval dan compression, bukan pengetahuan umum yang mungkin tidak akurat

Mekanisme ini memastikan Bob AI memberikan jawaban yang terpercaya dan dapat diverifikasi.

Periksa sumber resminya ya untuk memastikan keakuratan informasi ini.

**Sumber dokumen:**
- S02_Prompt_and_Safety_Plan_Bob.docx

---

## Catatan untuk Demo

- Pastikan dokumen yang relevan sudah dimuat sebelum mengajukan pertanyaan
- Jawaban selalu diakhiri dengan disclaimer
- Sumber dokumen ditampilkan di bawah jawaban
- Jika informasi tidak ada dalam konteks, Bob AI akan menolak menjawab dengan jujur
