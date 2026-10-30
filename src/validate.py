from sqlalchemy import text
from load import engine


def validate_data(expected_rows=None):

    print("\n=== DATA VALIDATION ===")

    query = text("""
        SELECT
            COUNT(*) AS total_rows,

            COUNT(*) FILTER (
                WHERE order_id IS NULL OR TRIM(order_id) = ''
            ) AS empty_order_id,

            COUNT(*) FILTER (
                WHERE product_id IS NULL OR TRIM(product_id) = ''
            ) AS empty_product_id,

            COUNT(*) FILTER (
                WHERE sales IS NULL
            ) AS null_sales,

            COUNT(*) FILTER (
                WHERE profit IS NULL
            ) AS null_profit,

            COUNT(*) FILTER (
                WHERE quantity <= 0
            ) AS invalid_quantity

        FROM clean_transactions;
    """)

    with engine.connect() as connection:
        result = connection.execute(query).mappings().one()

    total_rows = result["total_rows"]

    checks = {
        "Row count matches": (
            expected_rows is None or total_rows == expected_rows
        ),
        "No empty Order ID": result["empty_order_id"] == 0,
        "No empty Product ID": result["empty_product_id"] == 0,
        "No NULL Sales": result["null_sales"] == 0,
        "No NULL Profit": result["null_profit"] == 0,
        "No invalid Quantity": result["invalid_quantity"] == 0,
    }

    print("Total rows:", total_rows)

    for check_name, status in checks.items():
        print(
            f"{check_name}:",
            "PASS" if status else "FAILED"
        )

    if all(checks.values()):
        print("\nValidation status: SUCCESS")
        return True

    print("\nValidation status: FAILED")
    return False


if __name__ == "__main__":
    validate_data(expected_rows=9994)