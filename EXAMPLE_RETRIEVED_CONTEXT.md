# Contoh Retrieved Context - Bob AI

## Contoh Output Retrieved Context

Berikut adalah contoh output yang ditampilkan oleh Bob AI saat melakukan retrieval:

```
=======================================================
📄 RETRIEVED CONTEXT:
=======================================================

[Chunk 1] Sumber: S01_Ide_AI_Assistant_Bob.docx
Score BM25: 8.4521
Isi: Bob AI adalah asisten produktivitas berbahasa Indonesia yang dirancang khusus untuk membantu mahasiswa dalam kegiatan belajar sehari-hari. Asisten ini dapat meringkas dokumen, membuat jadwal belajar, memperbaiki tulisan, dan menjawab pertanyaan...

[Chunk 2] Sumber: S06_Hizkia Reinaldy_24110400036_Retrieval_Semantic_Search_Plan.docx
Score BM25: 7.8934
Isi: Query Expansion adalah teknik untuk memperluas pertanyaan asli menjadi beberapa variasi pertanyaan yang semantiknya mirip. Tujuannya adalah untuk meningkatkan recall dalam proses retrieval dengan menangkap berbagai cara user mungkin mengungkapkan...

[Chunk 3] Sumber: S02_Prompt_and_Safety_Plan_Bob.docx
Score BM25: 6.5421
Isi: Guardrails adalah mekanisme keamanan yang diterapkan untuk mencegah halusinasi. Bob AI diprogram untuk hanya menjawab berdasarkan konteks dokumen yang diberikan. Jika informasi tidak tersedia dalam konteks, sistem akan memberitahu secara jujur...
```

## Penjelasan Komponen

### 1. Chunk Information
- **Chunk Number**: Menunjukkan urutan chunk yang diambil (1-3)
- **Sumber**: Nama file dokumen asal chunk
- **Score BM25**: Skor relevansi dari algoritma BM25 (semakin tinggi semakin relevan)
- **Isi**: Potongan teks dari dokumen (truncated untuk preview)

### 2. Proses Retrieval
1. **Query Expansion**: Pertanyaan user diperluas menjadi 3-4 variasi
2. **Semantic Search**: Setiap variasi query dicari di ChromaDB
3. **Deduplication**: Chunk yang sama dari query berbeda dihilangkan
4. **Reranking**: Hasil diurutkan ulang menggunakan BM25
5. **Top-K Selection**: Hanya 3 chunk dengan skor tertinggi yang diambil

### 3. Context Compression
Setelah retrieved context ditampilkan, konteks dikompres menggunakan LLM untuk:
- Menghilangkan informasi yang tidak relevan
- Menyimpan hanya bagian yang terkait dengan pertanyaan
- Membatasi panjang konteks (maksimal 500 kata)

## Cara Melihat Retrieved Context di Demo

Jalankan file `rag.py`:
```bash
python rag.py
```

Kemudian ajukan pertanyaan, misalnya:
```
Apa itu Bob AI?
```

Sistem akan menampilkan:
1. Proses Query Expansion
2. Proses Retrieval
3. Proses Reranking dengan BM25
4. Retrieved Context lengkap dengan sumber dan skor
5. Context Compression
6. Jawaban akhir dari Bob AI
