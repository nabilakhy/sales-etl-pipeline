import pandas as pd
from pathlib import Path


def extract_data():
    """
    Membaca raw sales data dari file CSV.
    """

    # Menentukan folder
    base_dir = Path(__file__).resolve().parent.parent

    # Lokasi file dataset
    file_path = base_dir / "data" / "raw" / "Sample - Superstore.csv"

    # Memastikan file tersedia
    if not file_path.exists():
        raise FileNotFoundError(f"Dataset tidak ditemukan: {file_path}")

    # Membaca CSV
    df = pd.read_csv(file_path, encoding="latin1")

    print("=== EXTRACT PROCESS ===")
    print("File:", file_path.name)
    print("Total rows:", len(df))
    print("Total columns:", len(df.columns))
    print("Extract status: SUCCESS")

    return df


if __name__ == "__main__":
    df = extract_data()
    print("\nPreview data:")
    print(df.head().to_string(index=False))