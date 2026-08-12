from fastapi import FastAPI

website = FastAPI()

@website.get("/home")
def home ():
    return "This is Home Function"

@website.get("/about")
def about ():
    return "This is About function"

@website.get("/blogs")
def blogs ():
    return "This is Blogs Function"

@website.get("/students")
def students():
    return{
    "success": True,
    "method": "GET",
    "message": "Student list fetched successfully",
    "meta": {
        "total": 0,
        "page": 1,
        "limit": 10,
        "pages": 0
    },
    "data": []
}