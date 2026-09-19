from fastapi import FastAPI
from models.orders import Order





app = FastAPI()

orders =[]

#GET
@app.get("/orders")
def get_orders():
    return orders

#POST
@app.post("/orders")
def create_order(order:Order):
    orders.append(order)
    return {
        "message":"order created successfully",
        "order":order

    }

#PUT
@app.put("/orders/{order_id}")
def update_order(order_id:int,updated_order:Order):

    for order in orders:
        if order.order_id == order_id:

            order.user_id = updated_order.user_id
            order.product = updated_order.product
            order.quantity = updated_order.quantity


            return {
                "message":"order updated successfully",
                "order":order
            }
    return{"message":"order not found"}

#DELETE
@app.delete("/orders/{order_id}")
def delete_order(order_id:int):

    for order in orders:
        if order.order_id==order_id:
            orders.remove(order)

            return {
                "message":"order deleted successfully"

            }
    return{"message":"order not found"}

