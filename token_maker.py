from datetime import datetime, timedelta

import jwt

from config import SECRET_KEY, ALGORITHM

# 生成JWT
username = "xxx"

expiration = datetime.utcnow() + timedelta(hours=1000)
to_encode = {"exp": expiration, "sub": username}
encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

print(encoded_jwt)
