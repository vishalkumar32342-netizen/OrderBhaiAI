
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "instances" / "sqlite_orders.db"

def get_orders_db():
    conn = sqlite3.connect(
        DB_PATH,
        timeout=10
    )
    conn.row_factory = sqlite3.Row
    return conn





