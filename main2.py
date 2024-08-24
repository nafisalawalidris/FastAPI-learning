from fastapi import FastAPI, HTTPException, status, Response  # Added Response import for return type in delete function
from pydantic import BaseModel  # Importing BaseModel from pydantic for data validation
from typing import Optional  # Importing Optional from typing for optional fields
from random import randrange  # Importing randrange for generating random IDs

# Creating an instance of the FastAPI class
app = FastAPI()

# Define a Pydantic model for the post
class Post(BaseModel):
    title: str  # The title of the post
    content: str  # The content of the post
    published: bool = True  # Whether the post is published (default is True)
    rating: Optional[int] = None  # The rating of the post (optional, default is None)
    
class UpdatePost

# A list to store posts (in-memory storage for simplicity)
my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "favourite foods", "content": "I like pizza", "id": 2}
]

# Function to find a post by its ID
def find_post(id: int):
    for post in my_posts:
        if post['id'] == id:
            return post

# Defining a GET endpoint at the root URL ("/")
@app.get("/")
def root():
    return {"message": "Hello World"}

# Define a route for the "/posts" path with a GET method
@app.get("/posts")
def get_posts():
    return {"data": my_posts}

# Define a route for the "/posts" path with a POST method
@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

# Define a route for retrieving a specific post by ID
@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if post:
        return {"post_detail": post}
    raise HTTPException(status_code=404, detail="Post not found")

# Define a route for deleting a specific post by ID
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # Find the index of the post with the given ID
    for index, post in enumerate(my_posts):
        if post['id'] == id:
            my_posts.pop(index)  # Remove the post from the list
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    # If the post is not found, raise a 404 error
    raise HTTPException(status_code=404, detail="Post not found")

@app.put("/posts/{id}")
def update_post(id:int, post: Post):
    print 
    return{"message"; "Updated post"}
