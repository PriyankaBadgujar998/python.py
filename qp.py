# from fastapi import FastAPI

# app = FastAPI()
# data = [
#      {
#         "id": 1,
#         "name": "Aarav Sharma",
#         "email": "aarav.sharma@student.in",
#         "phone": "+91 98765 43210",
#         "city": "New Delhi",
#         "state": "Delhi",
           
#         },
#         {
#             "id": 2,
#             "name": "Priya Patel",
#             "email": "priya.patel@student.in",
#             "phone": "+91 98234 56781",
#             "city": "Ahmedabad",
#             "state": "Gujarat",
           
#         },
#         {
#             "id": 3,
#             "name": "Rohan Mehta",
#             "email": "rohan.mehta@student.in",
#             "phone": "+91 97654 32109",
#             "city": "Mumbai",
#             "state": "Maharashtra",
#         },
#         {
#             "id": 4,
#             "name": "Ananya Iyer",
#             "email": "ananya.iyer@student.in",
#             "phone": "+91 98456 78901",
#             "city": "Chennai",
#             "state": "Tamil Nadu",
           
#         },
#         {
#             "id": 5,
#             "name": "Vikram Singh",
#             "email": "vikram.singh@student.in",
#             "phone": "+91 98123 45670",
#             "city": "Jaipur",
#             "state": "Rajasthan",
    
#         },
#         {
#             "id": 6,
#             "name": "Sneha Reddy",
#             "email": "sneha.reddy@student.in",
#             "phone": "+91 99087 65432",
#             "city": "Hyderabad",
#             "state": "Telangana",
  
#         },
#         {
#             "id": 7,
#             "name": "Arjun Nair",
#             "email": "arjun.nair@student.in",
#             "phone": "+91 97432 10987",
#             "city": "Kochi",
#             "state": "Kerala",
   
#         },
#         {
#             "id": 8,
#             "name": "Kavya Desai",
#             "email": "kavya.desai@student.in",
#             "phone": "+91 98321 09876",
#             "city": "Pune",
#             "state": "Maharashtra",
       
#         },
#         {
#             "id": 9,
#             "name": "Rahul Gupta",
#             "email": "rahul.gupta@student.in",
#             "phone": "+91 96543 21098",
#             "city": "Lucknow",
#             "state": "Uttar Pradesh",
         
#         },
#         {
#             "id": 10,
#             "name": "Ishita Banerjee",
#             "email": "ishita.banerjee@student.in",
#             "phone": "+91 93321 87654",
#             "city": "Kolkata",
#             "state": "West Bengal",
          
#         }
# ]

  
# @app.get("/") 
# def home():
#   return "This is the homepage."

# @app.get("/users")
# def home():
#   return data
 

# @app.post("/create_user")
# def create_user(name,email,city,state):
#  data.append({
#    "id" : len(data)+1,
#    "name": name,
#    "email": email,
#    "city": city,
#    "state": state,

#  })
#  return{
#    "status": True,
#    "message": "user created successfully "
#  }

# @app.delete("/delete_user")
# def delete_user(id: int):

#     for x in data:
#         if x["id"] == id:
#             data.remove(x)
#             return {
#                 "status": True,
#                 "message": "User deleted successfully"
#             }

#     return {
#         "status": False,
#         "message": "Given ID is not found"
#     }

  
from fastapi import FastAPI

app = FastAPI()

data = [
    {"id": 1, "name": "Priyanka", "city": "Jaipur"},
    {"id": 2, "name": "Kavya", "city": "Pune"},
    {"id": 3, "name": "Aman", "city": "Delhi"}
]


@app.get("/")
def home():
    return "This is the homepage."


@app.get("/users")
def get_users():
    return data


@app.post("/create_user")
def create_user(name: str, city: str):
    data.append({
        "id": len(data)+1,
        "name": name,
        "city": city
    })

    return {
        "status": True,
        "message": "User created successfully"
    }


@app.delete("/delete_user")
def delete_user(id: int):
    for x in data:
        if x["id"] == id:
            data.remove(x)
            return {
                "status": True,
                "message": "User deleted successfully"
            }

    return {
        "status": False,
        "message": "Given ID is not found"
    }

@app.put("/update_user")
def update_user(id: int, name: str, city: str):

    for x in data:
        if x["id"] == id:
            x["name"] = name
            x["city"] = city

            return {
                "status": True,
                "message": "User updated successfully"
            }

    return {
        "status": False,
        "message": "Given ID is not found"
    }

