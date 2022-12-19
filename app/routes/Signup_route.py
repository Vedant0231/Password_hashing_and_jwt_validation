from fastapi import APIRouter, Depends, Request, HTTPException, status
from app.schemas.schema import Usersauth, Displayuser
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.models.models import Userauth
from app.utils.utils import password_hash, JWTBearer, decodeJWT
from typing import List

signup = APIRouter()

# secure router for total users
@signup.get("/alluser",dependencies=[Depends(JWTBearer())])
def alluser(request: Request, db:Session = Depends(get_db)):

    access_token = request.headers["Authorization"][7:]
    decoded = decodeJWT(access_token)
    print(decoded)
    db_users = db.query(Userauth).all()

    return db_users


# user signup by post method
@signup.post("/user_signup", response_model=Displayuser)
def signupp(resquest: Usersauth, db: Session = Depends(get_db)):

    # convert plain password with hash password
    newuser = Userauth(id=resquest.id, name=resquest.name, password=password_hash(resquest.password))
    db.add(newuser)
    db.commit()
    db.refresh(newuser)

    return newuser
