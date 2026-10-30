import pandas as pd
import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Folder utama
BASE_DIR = Path(__file__).resolve().parent.parent

# Baca konfigurasi .env
load_dotenv(BASE_DIR / ".env")

# Konfigurasi database
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Validasi konfigurasi
if not all([DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD]):
    raise ValueError("Konfigurasi database belum lengkap!")

# Buat koneksi database
DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

# Tes koneksi
def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version();"))
            print("=== DATABASE CONNECTION ===")
            print("PostgreSQL:", result.scalar())
            print("Connection status: SUCCESS")

    except Exception as error:
        print("Connection status: FAILED")
        print("Error:", error)

def load_data():
    print("\n=== LOAD PROCESS ===")

    # Lokasi file
    file_path = BASE_DIR / "data" / "processed" / "clean_sales.csv"

    if not file_path.exists():
        raise FileNotFoundError(f"File tidak ditemukan: {file_path}")

    # Membaca data
    df = pd.read_csv(
    file_path,
    parse_dates=["Order Date", "Ship Date"]
)

    # Mengubah nama kolom menjadi format snake_case
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )

    # Memasukkan data ke PostgreSQL
    df.to_sql(
        name="clean_transactions",
        con=engine,
        if_exists="replace",
        index=False,
        chunksize=1000
    )

    # Validasi jumlah data
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT COUNT(*) FROM clean_transactions")
        )
        total_rows = result.scalar()

    print("Source rows:", len(df))
    print("Loaded rows:", total_rows)
    print("Target table: clean_transactions")
    print("Load status: SUCCESS")

if __name__ == "__main__":
    test_connection()
    load_data()