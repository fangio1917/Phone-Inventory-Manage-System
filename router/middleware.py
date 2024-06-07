from fastapi import Request, HTTPException
import jwt
from config import SECRET_KEY, ALGORITHM


# 验证token
async def AuthMiddleware(request: Request, call_next):
    auth_header = request.headers.get("Authorization")
    if auth_header is None:
        return HTTPException(status_code=401, detail="Unauthorized")
    
    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Unauthorized")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    response = await call_next(request)
    return response




