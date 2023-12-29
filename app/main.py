from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/api/v1/hello-world")
def hello_world():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app")
