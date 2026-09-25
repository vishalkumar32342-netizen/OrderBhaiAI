from pydantic import BaseModel,Field

'''class Order(BaseModel):
    order_id: int
    user_id: int
    product:str
    quantity:int'''

#Request schema
class OrderCreate(BaseModel):
    customer_id:int =Field(gt=0)
    order_id:str = Field(min_length=1)
    amount:float = Field(gt=0)
    status:str = Field(min_length=1)
    datetime:str = Field(min_length=1)


class OrderUpdate(BaseModel):
    customer_id:int =Field(gt=0)
    amount:float = Field(gt=0)
    status:str  = Field(min_length=1)
    datetime:str = Field(min_length=1)






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
