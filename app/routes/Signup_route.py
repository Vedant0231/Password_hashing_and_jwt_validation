from fastapi import APIRouter, Depends
from app.schemas.schema import Usersauth, Displayuser
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.models.models import Userauth
from app.utils.utils import password_hash
from typing import List

signup = APIRouter()

# total users
@signup.get("/alluser", response_model=list[Displayuser])
def user(db: Session = Depends(get_db)):
    alluser = db.query(Userauth).all()

    return alluser


# user signup by post method
@signup.post("/user_signup", response_model=Displayuser)
def signupp(resquest: Usersauth, db: Session = Depends(get_db)):

    # convert plain password with hash password
    newuser = Userauth(
        id=resquest.id, name=resquest.name, password=password_hash(resquest.password)
    )
    db.add(newuser)
    db.commit()
    db.refresh(newuser)

    return newuser
