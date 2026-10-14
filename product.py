from fastapi import FastAPI

app = FastAPI()

class ProductModel:
    def __init__(self, id: int, title: str, category: str, price: int):
        self.id = id
        self.title = title
        self.category = category
        self.price = price



products = [
    ProductModel(1, "Laptop", "Electronics", 45000),
    ProductModel(2, "Mobile", "Electronics", 20000),
    ProductModel(3, "Shoes", "Fashion", 1500),
    ProductModel(4, "Watch", "Accessories", 2500),
    ProductModel(5, "Book", "Education", 500),
    ProductModel(6, "Headphones", "Electronics", 1800),
    ProductModel(7, "T-Shirt", "Fashion", 800),
    ProductModel(8, "Backpack", "Accessories", 1200),
    ProductModel(9, "Keyboard", "Electronics", 1000),
    ProductModel(10, "Notebook", "Education", 100)
]

data = []

for product in products:
    data.append({
        "id": product.id,
        "title": product.title,
        "category": product.category,
        "price": product.price
    })

@app.get("/")
def home():
    return "This is the homepage."


@app.get("/products")
def get_products():
    return data

@app.get("/get_by_id")
def get_product(id: int):
    for x in data:
        if x["id"] == id:
            return x

    return {"message": "Product not found"}



@app.post("/create")
def create_product(title: str, category: str, price:int):
    data.append({
        "id": len(data) + 1,
        "title": title,
        "category": category,
        "price": price
    })

    return {
        "status": True,
        "message": "Product created successfully"
    }
@app.put("/update")
def update_product(id: int, title: str, category: str, price: int):
    for x in data:
        if x["id"] == id:
            x["title"] = title
            x["category"] = category
            x["price"] = price

            return {
                "status": True,
                "message": "Product updated successfully"
            }

    return {
        "status": False,
        "message": "Product not found"
    }

@app.delete("/delete")
def delete_product(id: int):
    for x in data:
        if x["id"] == id:
            data.remove(x)

            return {
                "status": True,
                "message": "Product deleted successfully"
            }

    return {
        "status": False,
        "message": "Product not found"
    }