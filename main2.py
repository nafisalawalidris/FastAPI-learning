from fastapi import FastAPI  # Importing FastAPI from the fastapi module

# Creating an instance of the FastAPI class
app = FastAPI()

# Defining a GET endpoint at the root URL ("/")
@app.get("/")
def root():
    # Returning a JSON response with a "message" key and "Hello World" as the value
    return {"message": "Hello World"}

# Define a route for the "/posts" path
@app.get("/posts")
def get_posts():
    # Return a JSON response with placeholder data for posts
    return {"data": "This is your posts"}

# Define a route for the "/createposts" path
@app.post("/createposts")
def create_posts():
    # Return a JSON response indicating successful post creation
    return {"message": "successfully created posts"}
