from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from model.users import Users, get_user
from fastapi import APIRouter, status, Response

router_users = APIRouter()


class UserPydantic(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    password: Optional[str] = None
    permission: Optional[str] = 'user'
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


@router_users.post("/add", status_code=status.HTTP_201_CREATED)
async def add_user(added_user: UserPydantic, response: Response):
    try:
        user_created = Users(
            name=added_user.name,
            password=added_user.password,
            permission=added_user.permission,
            created_at=datetime.now(),
        )
        user_created.add_user()

    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"success": False, "message": str(e)}
    return {"success": True, "data": "User created"}


class UpdatedUserPydantic(BaseModel):
    data: List[UserPydantic]
    

@router_users.put("/update", status_code=status.HTTP_200_OK)
async def update_user(updated_users: UpdatedUserPydantic, response: Response):
    try:
        lists = updated_users.data
        for updated_user in lists:
            if updated_user.id is None:
                response.status_code = status.HTTP_400_BAD_REQUEST
                return {"success": False, "message": "User id is required"}
            user_updated = Users(id=updated_user.id)
            
            existed = user_updated.exist_user()
            
            if existed is None or existed is False:
                response.status_code = status.HTTP_400_BAD_REQUEST
                return {"success": False, "message": "User not found"}
            
            if updated_user.name is not None:
                existed.name = updated_user.name
                
            if updated_user.password is not None:
                existed.password = updated_user.password
            
            if updated_user.permission is not None:
                existed.permission = updated_user.permission
                
            existed.update_user()
        
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"success": False, "message": str(e)}
    
    return {"success": True, "data": "User updated"}


@router_users.delete("/delete", status_code=status.HTTP_200_OK)
async def delete_user(deleted_id: int, response: Response):
    
    try:
        if deleted_id is None or deleted_id == 0:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"success": False, "message": "User id is required"}
        user_deleted = Users(id=deleted_id)
        if user_deleted.delete_user() is True:
            return {"success": True, "data": "User deleted"}
        
        response.status_code = status.HTTP_400_BAD_REQUEST
        
        return {"success": False, "message": "User not found"}
        
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"success": False, "message": str(e)}


@router_users.get("/query", status_code=status.HTTP_200_OK)
async def get_users(response: Response):
    try:
        resp = get_user()
        if len(resp) == 0:
            raise Exception("back empty")

    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"success": False, "message": str(e)}

    return {"success": True, "data": resp}
