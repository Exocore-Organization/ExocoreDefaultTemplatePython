"""
== Default FastAPI Template ==

Created with care by: @ChoruOfficial (John Steve Costaños)

This template offers a solid and straightforward foundation.
It's designed to be a versatile starting point,
ready for you to build upon and customize for your projects.

#Btw this template is default only
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from paths_routes import generate_and_save_routes

PORT = 5000

app = FastAPI()

@app.get("/home")
def home():
    return JSONResponse({"message": "Welcome to the API"})

@app.post("/signin")
def signin():
    return JSONResponse({"message": "Signed in"})

@app.post("/signup")
def signup():
    return JSONResponse({"message": "Signed up"})

@app.get("/profile")
def profile():
    return JSONResponse({"message": "User profile"})

@app.delete("/logout")
def logout():
    return JSONResponse({"message": "Logged out"})

if __name__ == "__main__":
    import uvicorn
    generate_and_save_routes(app, port=PORT)
    uvicorn.run(app, host="0.0.0.0", port=PORT)
