# To excute your code, run this main file
import uvicorn


if __name__ == "__main__":
    uvicorn.run("app.app:app", host="localhost", port=8000, reload=True)
