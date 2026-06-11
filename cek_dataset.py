import kagglehub
import pandas as pd
import os

print("=" * 55)
print("Download Dataset 1 — World University Rankings")
print("=" * 55)
path1 = kagglehub.dataset_download("mylesoneill/world-university-rankings")
print(f"Path: {path1}")

# Cek file apa saja yang ada
print("\nFile yang tersedia:")
for f in os.listdir(path1):
    print(f"  - {f}")

# Baca file CSV pertama yang ditemukan
for f in os.listdir(path1):
    if f.endswith(".csv"):
        df = pd.read_csv(os.path.join(path1, f))
        print(f"\nPreview {f}:")
        print(f"  Jumlah baris: {len(df)}")
        print(f"  Kolom: {list(df.columns)}")
        print(df.head(3).to_string())
        break

print("\n" + "=" * 55)
print("Download Dataset 2 — US Education")
print("=" * 55)
path2 = kagglehub.dataset_download("noriuk/us-education-datasets-unification-project")
print(f"Path: {path2}")

print("\nFile yang tersedia:")
for f in os.listdir(path2):
    print(f"  - {f}")

for f in os.listdir(path2):
    if f.endswith(".csv"):
        df = pd.read_csv(os.path.join(path2, f))
        print(f"\nPreview {f}:")
        print(f"  Jumlah baris: {len(df)}")
        print(f"  Kolom: {list(df.columns)}")
        print(df.head(3).to_string())
        break
    