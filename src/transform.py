import pandas as pd


def transform_data(df):
    """
    Membersihkan dan memperkaya raw sales data.
    """

    print("=== TRANSFORM PROCESS ===")

    # 1. Salin data
    df = df.copy()

    # 2. Hapus exact duplicates
    duplicate_count = df.duplicated().sum()
    df = df.drop_duplicates()

    print("Duplicates removed:", duplicate_count)

    # 3. Konversi kolom tanggal
    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        format="%m/%d/%Y"
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        format="%m/%d/%Y"
    )

    # 4. Tipe data numerik
    numeric_columns = [
        "Sales",
        "Quantity",
        "Discount",
        "Profit"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="raise"
        )

    # 5. Tambahkan delivery_days
    df["delivery_days"] = (
        df["Ship Date"] - df["Order Date"]
    ).dt.days

    # 6. Tambahkan profit_margin
    df["profit_margin"] = (
        df["Profit"] / df["Sales"]
    ) * 100

    print("Total rows after transformation:", len(df))
    print("Total columns after transformation:", len(df.columns))
    print("Transform status: SUCCESS")

    return df


if __name__ == "__main__":

    from extract import extract_data
    from pathlib import Path

    # Extract
    raw_df = extract_data()

    # Transform
    clean_df = transform_data(raw_df)

    # Save processed data
    BASE_DIR = Path(__file__).resolve().parent.parent
    OUTPUT_PATH = BASE_DIR / "data" / "processed" / "clean_sales.csv"

    clean_df.to_csv(OUTPUT_PATH, index=False)

    print("\n=== SAVE PROCESSED DATA ===")
    print("Output file:", OUTPUT_PATH)
    print("File exists:", OUTPUT_PATH.exists())
    print("Save status: SUCCESS")