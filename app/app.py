# import routes

from fastapi import FastAPI
from app.routes.Signup_route import signup
from app.routes.loging_route import loging

app = FastAPI()

app.include_router(signup)
app.include_router(loging)
