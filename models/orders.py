from pydantic import BaseModel

class Order(BaseModel):
    order_id: int
    user_id: int
    product:str
    quantity:int
