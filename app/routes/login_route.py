from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas.schema import Userinfo
from app.models.models import Userauth
from app.database.database import get_db
from app.utils.utils import verify_password, create_access_token, refresh_access_token
from sqlalchemy.orm import Session

login = APIRouter()

# user logging by post method
@login.post("/loging")
def login_user(request: Userinfo, db: Session = Depends(get_db)):

    # check whether user name is present in database or not
    if not db.query(Userauth).filter(Userauth.name == request.name).count():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect name or password",
        )

    # if username is in the database , compare username and password
    else:
        user = db.query(Userauth).filter(Userauth.name == request.name).first()
        user_password = user.password

        # compare logging password with hash password
        if verify_password(request.password, user_password):
            access_token = create_access_token(user.name)
            refresh_token = refresh_access_token(user.name)

            # returning token
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
            }

        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect name or password",
            )
