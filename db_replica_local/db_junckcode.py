import csv
import os
import random
from datetime import datetime, timedelta

CSV_FILE = "order.csv"

os.makedirs("db_replica_local", exist_ok=True)

customers = range(1001, 1101)

statuses = [
    "Pending",
    "Completed",
    "Cancelled"
]

start_date = datetime(2026, 9, 1, 10, 0, 0)

with open(CSV_FILE, "w", newline="") as file:

    writer = csv.writer(file)

    # Header
    writer.writerow([
        "id",
        "customer_id",
        "order_id",
        "amount",
        "status",
        "datetime"
    ])

    # Generate 300 records
    for i in range(1, 301):

        customer_id = random.choice(list(customers))
        order_id = f"ORD{i:04d}"
        amount = round(random.uniform(100, 5000), 2)
        status = random.choice(statuses)

        order_datetime = start_date + timedelta(
            minutes=random.randint(0, 43200)
        )

        writer.writerow([
            i,
            customer_id,
            order_id,
            amount,
            status,
            order_datetime.strftime("%Y-%m-%d %H:%M:%S")
        ])

print("300 orders created successfully")