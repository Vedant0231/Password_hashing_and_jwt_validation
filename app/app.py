# import routes

from fastapi import FastAPI
from app.routes.Signup_route import signup
from app.routes.login_route import login

app = FastAPI()

app.include_router(signup)
app.include_router(login)
