from fastapi import FastAPI, Body  # Importing FastAPI and Body from the fastapi module

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

# Define a route for the "/createposts" path with a POST method
@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    # Print the payload to the console (for debugging)
    print(payload)
    # Return a JSON response indicating successful post creation
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"}
