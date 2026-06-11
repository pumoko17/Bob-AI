"""Dataset Preparation for University Rankings

Downloads and processes Kaggle university ranking datasets,
converting them to text format for RAG applications.
"""
import os

import kagglehub
import pandas as pd

# Download dataset
path1 = kagglehub.dataset_download("mylesoneill/world-university-rankings")

# Cek kolom timesData dan shanghaiData dulu
df_times = pd.read_csv(os.path.join(path1, "timesData.csv"))
df_shanghai = pd.read_csv(os.path.join(path1, "shanghaiData.csv"))
df_cwur = pd.read_csv(os.path.join(path1, "cwurData.csv"))

print("Kolom timesData:", list(df_times.columns))
print("Kolom shanghaiData:", list(df_shanghai.columns))
print("\nPreview timesData:")
print(df_times.head(2).to_string())
print("\nPreview shanghaiData:")
print(df_shanghai.head(2).to_string())

# ── Konversi ke teks natural untuk RAG ───────────────
teks_output = []

# CWUR Data — ambil tahun terbaru
print("Memproses cwurData...")
df_cwur_latest = df_cwur[df_cwur['year'] == df_cwur['year'].max()]
for _, row in df_cwur_latest.iterrows():
    teks = (
        f"Menurut CWUR ranking tahun {int(row['year'])}, "
        f"{row['institution']} dari {row['country']} "
        f"berada di peringkat dunia ke-{int(row['world_rank'])} "
        f"dengan skor {row['score']:.2f}. "
        f"Universitas ini mendapat peringkat nasional "
        f"ke-{int(row['national_rank'])} di negaranya. "
        f"Kualitas pendidikannya berada di peringkat "
        f"{int(row['quality_of_education'])}, "
        f"kualitas fakultasnya di peringkat "
        f"{int(row['quality_of_faculty'])}, "
        f"dan tingkat keberhasilan alumni di dunia kerja "
        f"di peringkat {int(row['alumni_employment'])}."
    )
    teks_output.append(teks)

# Times Data — ambil tahun terbaru
print("Memproses timesData...")
df_times_clean = df_times.dropna(subset=['university_name', 'world_rank'])
df_times_latest = df_times_clean[df_times_clean['year'] == df_times_clean['year'].max()]
for _, row in df_times_latest.head(200).iterrows():
    teks = (
        f"Menurut Times Higher Education ranking tahun {row['year']}, "
        f"{row['university_name']} dari {row['country']} "
        f"berada di peringkat {row['world_rank']} dunia. "
        f"Skor pengajaran (teaching): {row['teaching']}, "
        f"skor riset (research): {row['research']}, "
        f"skor sitasi (citations): {row['citations']}."
    )
    teks_output.append(teks)

# Shanghai Data — ambil tahun terbaru
print("Memproses shanghaiData...")
df_shanghai_clean = df_shanghai.dropna(subset=['university_name', 'world_rank'])
df_shanghai_latest = df_shanghai_clean[df_shanghai_clean['year'] == df_shanghai_clean['year'].max()]
for _, row in df_shanghai_latest.head(200).iterrows():
    teks = (
        f"Menurut Shanghai (ARWU) ranking tahun {int(row['year'])}, "
        f"{row['university_name']} dari {row['country']} "
        f"berada di peringkat {row['world_rank']} dunia. "
        f"Total skor alumni: {row['alumni']}, "
        f"skor publikasi: {row['pub']}, "
        f"skor penghargaan (award): {row['award']}."
    )
    teks_output.append(teks)

# ── Simpan ke file teks ───────────────────────────────
OUTPUT_FILE = "dataset_university_rankings.txt"
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for teks in teks_output:
        f.write(teks + "\n\n")

print(f"\n✅ Selesai! {len(teks_output)} entri disimpan ke {OUTPUT_FILE}")
print("Preview 2 entri pertama:")
print("-" * 50)
for t in teks_output[:2]:
    print(t)
    print()
