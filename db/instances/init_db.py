import csv
import os
from pathlib import Path
from db.base import get_orders_db

db = get_orders_db()

# 1. Store table creation query in a variable, then execute
create_table_query = """
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        order_id TEXT UNIQUE,
        amount REAL,
        status TEXT,
        datetime TEXT
    )
"""
db.execute(create_table_query)

# Path resolution to local CSV
BASE_DIR = Path(__file__).resolve().parent.parent.parent
csv_file = BASE_DIR / "db_replica_local" / "order.csv"

# 2. Store insert query in a variable
insert_order_query = """
    INSERT OR IGNORE INTO orders
    (
        id,
        customer_id,
        order_id,
        amount,
        status,
        datetime
    )
    VALUES (?, ?, ?, ?, ?, ?)
"""

inserted_count = 0

# 3. Read CSV and execute insert query
with open(csv_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor = db.execute(insert_order_query, (
            row["id"],
            row["customer_id"],
            row["order_id"],
            row["amount"],
            row["status"],
            row["datetime"]
        ))

        if cursor.rowcount > 0:
            inserted_count += 1

db.commit()
db.close()

print("Database sync completed.")
print(f"Added {inserted_count} new orders. (Duplicates were skipped)")