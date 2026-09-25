from fastapi import FastAPI, HTTPException
from models.orders import  OrderResponse, OrderCreate, OrderUpdate
from crud.orders import get_orders, create_order, update_order, delete_order






app = FastAPI()



#GET
@app.get("/orders",response_model=list[OrderResponse])
def read_orders(
        customer_id: int | None = None,
        id: int | None = None,
        order_id: str | None = None,
        status:str | None=None,
        min_amount:float | None = None,
        max_amount:float | None = None,
        from_date:str | None = None,
        to_date:str | None = None
):
    return get_orders(
        customer_id,
        id,
        order_id,
        status,
        min_amount,
        max_amount,
        from_date,
        to_date
    )
@app.post("/orders",response_model=OrderResponse)
def add_order(order:OrderCreate):
    new_order = create_order(order)

    if new_order is None:
        raise HTTPException(
            status_code=409,
            detail="Order ID already exists"
        )

    return new_order


@app.put("/orders/{order_id}", response_model=OrderResponse)
def edit_order(order_id:str,order:OrderUpdate):
    updated_order =  update_order(order_id, order)

    if updated_order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )
    return updated_order


@app.delete("/orders/{order_id}")
def remove_order(order_id: str):
    deleted_order = delete_order(order_id)

    if deleted_order is None:
        raise HTTPException(
            status_code=404,
            detail="order not found"
        )

    return deleted_order



#POST
'''@app.post("/orders",response_model=OrderResponse)
def create_order(order:OrderCreate):

    new_order = {
        "order_id":len(orders)+1,
        "user_id":order.user_id,
        "product":order.product,
        "quantity":order.quantity
    }
    orders.append(new_order)
    return new_order''''''

#PUT
@app.put("/orders/{order_id}", response_model=OrderResponse)
def update_order(order_id:int,order:OrderCreate):

    for existing_order in orders:
        if existing_order["order_id"] == order_id:

            existing_order["user_id"]= order.user_id
            existing_order["product"]= order.product
            existing_order["quantity"] = order.quantity


            return existing_order


    raise HTTPException(
        status_code=404,
        detail="Order not found"
    )

#DELETE
@app.delete("/orders/{order_id}",response_model=DeleteResponse)
def delete_order(order_id:int):

    for order in orders:
        if order.order_id==order_id:
            orders.remove(order)

            return {
                "message":"order deleted successfully"

            }
    raise HTTPException(
        status_code=404,
        detail="Order not found"
    )'''

