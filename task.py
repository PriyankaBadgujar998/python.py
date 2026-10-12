from fastapi import FastAPI

app = FastAPI()

@app.get("/contact")
def contact ():
     return "This is a contact page"

@app.get("/profile")
def profile():
    return "This is a profile page"

@app.get("/terms")
def terms():
    return "Terms and Conditions"

@app.get("/user/{username}")
def user(username):
    return f"Welcome {username}"

@app.get("/product/{product__id}")
def product(product_id):
     return f"Product ID is {product_id}"

@app.get("/shop/{category}/{item}")
def shop(category,item):
     return f"Category: {category}, Item: {item}"

@app.get("/files/{filepath:path}")
def files(filepath):
    return f"File path: {filepath}"

@app.get("/archive/{year}/{month}")
def archive(year, month):
    return f"Archive for {month}/{year}"

