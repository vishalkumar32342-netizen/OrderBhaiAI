from db.base import get_orders_db

def get_orders(
        customer_id=None,
        order_id=None,
        status=None,
        min_amount=None,
        max_amount=None
):
    db = get_orders_db()



    query = """ SELECT * FROM orders WHERE 1=1 """

    params = []

    if customer_id is not None:
        query += " AND customer_id = ?"
        params.append(customer_id)

    if order_id is not None:
        query += "AND order_id = ?"
        params.append(order_id)

    if status is not None:
        query += "AND LOWER(status)= LOWER(?)"
        params.append(status)

    if min_amount is not None:
        query += "AND amount >= ?"
        params.append(min_amount)

    if max_amount is not None:
        query += "AND amount <= ?"
        params.append(max_amount)

    query += "ORDER BY id DESC"

    cursor = db.execute(query,params)
    rows = cursor.fetchall()

    db.close()

    return [dict(row) for row in rows]




