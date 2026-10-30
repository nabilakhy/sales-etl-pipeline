import pandas as pd
from pathlib import Path

# Tentukan folder utama project
BASE_DIR = Path(__file__).resolve().parent.parent

# Lokasi dataset
DATA_PATH = BASE_DIR / "data" / "raw" / "Sample - Superstore.csv"

print("=== DATASET INSPECTION ===")

# Cek file
if not DATA_PATH.exists():
    raise FileNotFoundError(f"Dataset tidak ditemukan: {DATA_PATH}")

# Baca CSV
df = pd.read_csv(DATA_PATH, encoding="latin1")

# Tampilkan informasi dataset
print("\n=== DATASET OVERVIEW ===")
print("Total rows:", df.shape[0])
print("Total columns:", df.shape[1])

print("\n=== COLUMN NAMES ===")
print(df.columns.tolist())

print("\n=== FIRST 5 ROWS ===")
print(df.head().to_string(index=False))

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== DUPLICATE RECORDS ===")
print("Total duplicates:", df.duplicated().sum())

print("\n=== NUMERICAL SUMMARY ===")
print(df.describe())

print("\n=== DATA QUALITY CHECK ===")

# 1. Cek Order ID dan Product ID kosong
print("Empty Order ID:", df["Order ID"].isna().sum())
print("Empty Product ID:", df["Product ID"].isna().sum())

# 2. Cek format tanggal
order_dates = pd.to_datetime(
    df["Order Date"], errors="coerce"
)

ship_dates = pd.to_datetime(
    df["Ship Date"], errors="coerce"
)

print("Invalid Order Date:", order_dates.isna().sum())
print("Invalid Ship Date:", ship_dates.isna().sum())

# 3. Cek nilai Quantity dan Sales
print("Quantity <= 0:", (df["Quantity"] <= 0).sum())
print("Sales <= 0:", (df["Sales"] <= 0).sum())

# 4. Cek rentang Discount
print("Discount below 0:", (df["Discount"] < 0).sum())
print("Discount above 1:", (df["Discount"] > 1).sum())

# 5. Cek transaksi dengan Profit negatif
print("Negative Profit:", (df["Profit"] < 0).sum())

# 6. Cek tanggal pengiriman sebelum tanggal pemesanan
print(
    "Ship Date before Order Date:",
    (ship_dates < order_dates).sum()
)