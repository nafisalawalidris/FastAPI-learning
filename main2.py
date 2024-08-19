from fastapi import FastAPI  # Importing FastAPI from the fastapi module

# Creating an instance of the FastAPI class
app = FastAPI()

# Defining a GET endpoint at the root URL ("/")
@app.get("/")
async def root():
    # Returning a JSON response with a "message" key and "Hello World" as the value
    return {"message": "Hello World"}
