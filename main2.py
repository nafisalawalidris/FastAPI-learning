from fastapi import FastAPI  # Importing FastAPI from the fastapi module
from pydantic import BaseModel  # Importing BaseModel from pydantic for data validation
from typing import Optional  # Importing Optional from typing for optional fields

# Creating an instance of the FastAPI class
app = FastAPI()

# Define a Pydantic model for the post
class Post(BaseModel):
    title: str  # The title of the post
    content: str  # The content of the post
    published: bool = True  # Whether the post is published (default is True)
    rating: Optional[int] = None  # The rating of the post (optional, default is None)

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
def create_posts(post: Post):
    # Print the rating of the new_post data to the console (for debugging)
    print(post.rating)  # Accessing the rating field of the post object
    # Print the entire post data to the console (for debugging)
    print(post.dict())
    # Return a JSON response with the new created post data
    return {"data": post.dict()}
