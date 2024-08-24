from fastapi import FastAPI, HTTPException, status, Response  # Import necessary FastAPI classes for creating API, handling exceptions, and defining status codes
from pydantic import BaseModel  # Import BaseModel from Pydantic for data validation and serialization
from typing import Optional  # Import Optional from typing for optional fields
from random import randrange  # Import randrange from random module to generate random IDs for posts

# Create an instance of the FastAPI class
app = FastAPI()

# Define a Pydantic model for the post, which ensures data validation and structure
class Post(BaseModel):
    title: str  # The title of the post (required)
    content: str  # The content of the post (required)
    published: bool = True  # Indicates whether the post is published (default is True)
    rating: Optional[int] = None  # Optional rating field for the post, default is None

# An in-memory list to store posts; each post is a dictionary for simplicity
my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "favourite foods", "content": "I like pizza", "id": 2}
]

# Function to find a post by its ID
def find_post(id: int):
    for post in my_posts:  # Iterate over all posts
        if post['id'] == id:  # Check if the post ID matches the given ID
            return post  # Return the post if found

# Function to find the index of a post by its ID, useful for updating or deleting posts
def find_index_post(id: int):
    for index, post in enumerate(my_posts):  # Enumerate provides index and post
        if post['id'] == id:  # Check if the post ID matches the given ID
            return index  # Return the index of the post if found
    return None  # Return None if no post is found with the given ID

# Define a GET endpoint at the root URL ("/") that returns a simple message
@app.get("/")
def root():
    return {"message": "Hello World"}

# Define a route for the "/posts" path with a GET method to retrieve all posts
@app.get("/posts")
def get_posts():
    return {"data": my_posts}  # Return the list of all posts

# Define a route for the "/posts" path with a POST method to create a new post
@app.post("/posts")
def create_posts(post: Post):  # The post parameter is of type Post (Pydantic model)
    post_dict = post.dict()  # Convert the Pydantic model to a dictionary
    post_dict['id'] = randrange(0, 10000000)  # Generate a random ID for the new post
    my_posts.append(post_dict)  # Add the new post to the list of posts
    return {"data": post_dict}  # Return the newly created post data

# Define a route for retrieving a specific post by ID using the GET method
@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)  # Find the post by its ID
    if post:
        return {"post_detail": post}  # Return post details if found
    # Raise an HTTP 404 error if the post is not found
    raise HTTPException(status_code=404, detail="Post not found")

# Define a route for deleting a specific post by ID using the DELETE method
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)  # Find the index of the post by its ID
    if index is not None:  # Check if the post exists
        my_posts.pop(index)  # Remove the post from the list
        return Response(status_code=status.HTTP_204_NO_CONTENT)  # Return a 204 status code indicating successful deletion
    # Raise an HTTP 404 error if the post is not found
    raise HTTPException(status_code=404, detail="Post not found")

# Define a route for updating a specific post by ID using the PUT method
@app.put("/posts/{id}")
def update_post(id: int, post: Post):  # The post parameter is of type Post (Pydantic model)
    index = find_index_post(id)  # Find the index of the post by its ID
    if index is None:  # Check if the post exists
        # Raise an HTTP 404 error if the post is not found
        raise HTTPException(status_code=404, detail="Post not found")

    # Update the post with the new data
    post_dict = post.dict()  # Convert the Pydantic model to a dictionary
    post_dict['id'] = id  # Ensure the post ID remains the same
    my_posts[index] = post_dict  # Replace the existing post with the updated post

    return {"data": post_dict}  # Return the updated post data


