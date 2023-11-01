from pydantic import BaseModel

class Product(BaseModel):
    """"
    id, name, description, price
    """
    id:int
    name:str
    description:str
    price:float