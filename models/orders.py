from pydantic import BaseModel

'''class Order(BaseModel):
    order_id: int
    user_id: int
    product:str
    quantity:int'''

#Request schema
'''class OrderCreate(BaseModel):
    user_id:int
    product:str
    quantity:int'''



#Response schema
class OrderResponse(BaseModel):
    id:int
    customer_id:int
    order_id:str
    amount:float
    status:str
    datetime:str


#DeleteResponse schema
'''class DeleteResponse(BaseModel):
    message:str'''
