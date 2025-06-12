from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def home():
    return "Welcome to AI Career Finder App - Xplore"