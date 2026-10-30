from pathlib import Path

from extract import extract_data
from transform import transform_data
from load import load_data
from validate import validate_data


BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_PATH = BASE_DIR / "data" / "processed" / "clean_sales.csv"


def run_pipeline():

    print("\n" + "=" * 45)
    print("       SALES ETL PIPELINE STARTED")
    print("=" * 45)

    try:
        # 1. EXTRACT
        print("\n[1/4] EXTRACT")
        raw_df = extract_data()

        # 2. TRANSFORM
        print("\n[2/4] TRANSFORM")
        clean_df = transform_data(raw_df)

        # Save processed data
        clean_df.to_csv(OUTPUT_PATH, index=False)
        print("Processed data saved:", OUTPUT_PATH)

        # 3. LOAD
        print("\n[3/4] LOAD")
        load_data()

        # 4. VALIDATE
        print("\n[4/4] VALIDATE")
        validation_success = validate_data(
            expected_rows=len(clean_df)
        )

        if not validation_success:
            raise RuntimeError("Data validation failed!")

        print("\n" + "=" * 45)
        print("       ETL PIPELINE COMPLETED!")
        print("=" * 45)

    except Exception as error:
        print("\nETL PIPELINE FAILED!")
        print("Error:", error)
        raise


if __name__ == "__main__":
    run_pipeline()