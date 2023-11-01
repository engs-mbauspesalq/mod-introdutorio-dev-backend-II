from fastapi import FastAPI
from models.products import Product

app = FastAPI()

@app.get('/')
def say():
    return {'Fast':'API'}

@app.get('/{name}')
def say_hi(name:str):
    if not name:
        pass
    return {'Hello':name}

data = [
    Product(id=1, name='Tenis Nike Air', description='Calçados', price=799.99),
    Product(id=2, name='Iphone', description='Tecnologia', price=3998.99),
    Product(id=3, name='Notebook', description='Tecnologia', price=4980.99),
]

@app.get('/api/products')
def get_products():
    return data