from db.base import get_orders_db

def get_orders(
        customer_id=None,
        id=None,
        order_id=None,
        status=None,
        min_amount=None,
        max_amount=None,
        from_date=None,
        to_date=None
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

    if id is not None:
        query += " AND id = ?"
        params.append(id)

    if status is not None:
        query += "AND LOWER(status)= LOWER(?)"
        params.append(status)

    if min_amount is not None:
        query += "AND amount >= ?"
        params.append(min_amount)

    if max_amount is not None:
        query += "AND amount <= ?"
        params.append(max_amount)

    if from_date is not None:
        query += "AND DATE(datetime) >=DATE(?)"
        params.append(from_date)

    if to_date is not None:
        query += "AND DATE(datetime) <= DATE(?)"
        params.append(to_date)

    query += "ORDER BY id DESC"

    cursor = db.execute(query,params)
    rows = cursor.fetchall()

    db.close()

    return [dict(row) for row in rows]




def create_order(order):
    db = get_orders_db()

    query = """
        INSERT INTO orders
        (
            customer_id,
            order_id,
            amount,
            status,
            datetime
        )
        VALUES (?, ?, ?, ?, ?)
            """


    cursor = db.execute(
        query,
        (
            order.customer_id,
            order.order_id,
            order.amount,
            order.status,
            order.datetime
        )
    )

    db.commit()

    new_id = cursor.lastrowid

    db.close()

    return {
        "id": new_id,
        "customer_id": order.customer_id,
        "order_id":order.order_id,
        "amount":order.amount,
        "status":order.status,
        "datetime":order.datetime

    }

def update_order(order_id,order):
    db = get_orders_db()

    query = """
        UPDATE orders
        SET
            customer_id = ?,
            amount = ?,
            status = ?,
            datetime = ?
        WHERE order_id = ?
    """

    db.execute(
        query,
        (
            order.customer_id,
            order.amount,
            order.status,
            order.datetime,
            order_id
        )
    )

    db.commit()

    cursor = db.execute(
        """
        SELECT *
        FROM orders
        WHERE order_id = ?
        """,
        (order_id,)
    )

    row= cursor.fetchone()

    db.close()

    if row is None:
        return None

    return dict(row)

def delete_order(order_id):
    db = get_orders_db()

    query = """
    DELETE FROM orders WHERE order_id = ?"""

    cursor = db.execute(query, (order_id,))
    db.commit()

    deleted = cursor.rowcount
    db.close()

    if deleted ==0:
        return None

    return {
        "message": "order deleted successfully",
        "order_id": order_id
    }
