# This Procfile is used to specify the command that Heroku should run to start your application
# The 'gunicorn' command is used as the WSGI HTTP server to serve your FastAPI application
# -w 4 specifies 4 worker processes
# -k uvicorn.workers.UvicornWorker uses Uvicorn's worker class to handle ASGI applications

web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app