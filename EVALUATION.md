# Evaluasi Sederhana - Bob AI

## Metode Evaluasi

Evaluasi dilakukan dengan menguji 3 pertanyaan kunci dan menilai:
1. **Relevansi** - Apakah jawaban relevan dengan pertanyaan?
2. **Akurasi** - Apakah jawaban akurat berdasarkan sumber dokumen?
3. **Sumber** - Apakah sumber dokumen ditampilkan dengan benar?
4. **Guardrails** - Apakah guardrails berfungsi (tidak halusinasi)?

## Test Case 1: Pertanyaan Definisi

**Pertanyaan:**
"Apa itu Bob AI dan apa fungsinya?"

**Expected Output:**
- Jawaban menjelaskan definisi Bob AI sebagai asisten produktivitas berbahasa Indonesia
- Menyebutkan fungsi: meringkas dokumen, jadwal belajar, memperbaiki tulisan, menjawab pertanyaan
- Sumber: S01_Ide_AI_Assistant_Bob.docx
- Diakhiri dengan disclaimer

**Hasil Evaluasi:**
- [ ] Relevansi: Ya/Tidak
- [ ] Akurasi: Ya/Tidak
- [ ] Sumber ditampilkan: Ya/Tidak
- [ ] Guardrails aktif: Ya/Tidak
- **Skor**: ___/4

---

## Test Case 2: Pertanyaan Teknis RAG

**Pertanyaan:**
"Apa saja komponen utama dalam workflow RAG yang digunakan Bob AI?"

**Expected Output:**
- Jawaban menyebutkan 5 komponen: Query Expansion, Retrieval, Reranking, Context Compression, Generation
- Penjelasan singkat untuk setiap komponen
- Sumber: S06_Retrieval_Semantic_Search_Plan.docx
- Diakhiri dengan disclaimer

**Hasil Evaluasi:**
- [ ] Relevansi: Ya/Tidak
- [ ] Akurasi: Ya/Tidak
- [ ] Sumber ditampilkan: Ya/Tidak
- [ ] Guardrails aktif: Ya/Tidak
- **Skor**: ___/4

---

## Test Case 3: Pertanyaan Guardrails

**Pertanyaan:**
"Bagaimana Bob AI mencegah halusinasi dalam memberikan jawaban?"

**Expected Output:**
- Jawaban menjelaskan mekanisme guardrails
- Menyebutkan constraint-based answering, explicit refusal, source attribution
- Sumber: S02_Prompt_and_Safety_Plan_Bob.docx
- Diakhiri dengan disclaimer

**Hasil Evaluasi:**
- [ ] Relevansi: Ya/Tidak
- [ ] Akurasi: Ya/Tidak
- [ ] Sumber ditampilkan: Ya/Tidak
- [ ] Guardrails aktif: Ya/Tidak
- **Skor**: ___/4

---

## Test Case 4: Pertanyaan di Luar Konteks (Opsional)

**Pertanyaan:**
"Berapa harga iPhone 15 terbaru?"

**Expected Output:**
- Bob AI menolak menjawab karena informasi tidak ada dalam konteks
- Pesan: "Informasi tersebut tidak tersedia dalam dokumen"
- Tidak ada sumber dokumen

**Hasil Evaluasi:**
- [ ] Menolak dengan jujur: Ya/Tidak
- [ ] Tidak halusinasi: Ya/Tidak
- **Skor**: ___/2

---

## Ringkasan Evaluasi

| Test Case | Relevansi | Akurasi | Sumber | Guardrails | Skor |
|-----------|-----------|---------|--------|------------|------|
| 1. Definisi Bob AI | | | | | /4 |
| 2. Komponen RAG | | | | | /4 |
| 3. Guardrails | | | | | /4 |
| 4. Luar Kontek (opsional) | | | | | /2 |
| **TOTAL** | | | | | **/14** |

## Kriteria Kelulusan
- **Minimal**: 9/14 (64%)
- **Baik**: 11/14 (79%)
- **Sangat Baik**: 13/14 (93%)

## Cara Menjalankan Evaluasi

1. Pastikan semua dokumen .docx ada di folder
2. Jalankan `python rag.py`
3. Masukkan setiap pertanyaan satu per satu
4. Catat hasil dan isi tabel evaluasi
5. Hitung total skor
