from base import get_orders_db




db = get_orders_db()
cursor = db.cursor()




query = "SELECT * FROM orders ORDER BY id DESC LIMIT 5"




cursor.execute(query)
rows = cursor.fetchall()


for row in rows:
   print(dict(row))

