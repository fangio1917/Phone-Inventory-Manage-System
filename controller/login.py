from fastapi import APIRouter, status, Response
from model.users import Users, get_user
from .users import UserPydantic
from datetime import datetime, timedelta
import jwt
from config import SECRET_KEY, ALGORITHM

router_login = APIRouter()


def create_token(username: str) -> str:
    expiration = datetime.utcnow() + timedelta(hours=1)
    to_encode = {"exp": expiration, "sub": username}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router_login.post("/back-end/login", status_code=status.HTTP_200_OK)
async def login(user: UserPydantic, response: Response):
    try:
        login_user = Users(
            name=user.name,
        )
        res = login_user.login()
        if res is None:
            raise Exception("User not found")
        if res is None:
            raise Exception("User not found")
        if res.password != user.password:
            raise Exception("Password is incorrect")

        token = create_token(login_user.name)

        return {"success": True, "message": "Login successful", "Authorization": token}

    except Exception as e:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"success": False, "message": str(e)}





