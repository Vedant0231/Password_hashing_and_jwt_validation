from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas.schema import Userinfo
from app.models.models import Userauth
from app.database.database import get_db
from app.utils.utils import verify_password, create_access_token, refresh_access_token
from sqlalchemy.orm import Session

loging = APIRouter()

# user logging by post method
@loging.post("/loging")
def loging_user(request: Userinfo, db: Session = Depends(get_db)):

    # check whether user name is present in database or not
    if not db.query(Userauth).filter(Userauth.name == request.name).count():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect name or password",
        )

    # if username is in the database , compair username and password
    else:
        user = db.query(Userauth.password).filter(Userauth.name == request.name).first()
        user_password = user.password

        # compair logging password with hash password
        if verify_password(request.password, user_password):
            access_token = create_access_token(user)
            refresh_token = refresh_access_token(user)

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
