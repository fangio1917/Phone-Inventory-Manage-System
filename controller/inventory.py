from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
from fastapi import APIRouter, status, Response
from model.inventory import get_inventories, Inventories


class InventoryPydantic(BaseModel):
    id: Optional[int] = None
    phone: Optional[str] = None
    manufacturer: Optional[str] = None
    count: Optional[int] = None
    local: Optional[str] = None
    date: Optional[datetime] = None
    price: Optional[float] = None

    
    
router_inventory = APIRouter()


@router_inventory.post("/add", status_code=status.HTTP_201_CREATED)
async def add_inventories(a_inventories: InventoryPydantic, response: Response):
    try:
        
        added_inventories = Inventories(**a_inventories.dict())
        
        added_inventories.add_inventory()
        
        return {"success": True, "message": "inventories added successfully"}
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"success": False, "message": str(e)}
        
        
@router_inventory.get("/query", status_code=status.HTTP_200_OK)
async def get_inventory(response: Response):
    try:
        
        queried_inventories = get_inventories()
        if len(queried_inventories) == 0:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"success": False, "message": "No inventoriess found"}
        
        return {"success": True, "message": "inventories found", "data": queried_inventories}
    
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"success": False, "message": str(e)}
    
    
class UpdatedInventory(BaseModel):
    data: List[InventoryPydantic]


@router_inventory.put("/update", status_code=status.HTTP_200_OK)
async def update_inventories(lists: UpdatedInventory, response: Response):
    try:
        for u_inventories in lists.data:
            
            updated_inventories = Inventories(
                id=u_inventories.id,
            )
            existed = updated_inventories.exist_inventories()
            if existed is False or existed is None:
                response.status_code = status.HTTP_404_NOT_FOUND
                return {"message": "inventories not found"}
            
            if u_inventories.phone is not None:
                existed.phone = u_inventories.phone
            if u_inventories.manufacturer is not None:
                existed.manufacturer = u_inventories.manufacturer
            if u_inventories.count is not None:
                existed.count = u_inventories.count
            if u_inventories.local is not None:
                existed.local = u_inventories.local
            if u_inventories.date is not None:
                existed.date = u_inventories.date
            if u_inventories.price is not None:
                existed.price = u_inventories.price
                
            if not existed.update_inventories():
                response.status_code = status.HTTP_400_BAD_REQUEST
                return {"success": False, "message": "inventories not updated"}
            
        return {"success": True, "message": "inventories updated successfully"}
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"success": False, "message": str(e)}
    
        
@router_inventory.delete("/delete", status_code=status.HTTP_200_OK)
async def delete_inventories(deleted_id: int, response: Response):
    
    try:
        deleted_inventories = Inventories(
            id=deleted_id
        )
        deleted = deleted_inventories.delete_inventories()
        
        if deleted is True:
            return {"success": True, "message": "inventories deleted successfully"}
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"success": False, "message": "inventories not deleted"}
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"success": False, "message": str(e)}
        