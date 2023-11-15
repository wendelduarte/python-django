from fastapi import FastAPI
from models.product import Product

app = FastAPI()

products = [
    Product(id=1, name='Coca-Cola', description='Uma bebida mundialmente conhecida', price=9.98),
    Product(id=2, name='Tenis Nike Air', description='Calçados', price=799.99),
    Product(id=3, name='Iphone', description='Tecnologia', price=3998.99),
    Product(id=4, name='Notebook', description='Tecnologia', price=4980.99),
]

@app.get('/api/products')
def get_products():
    return products