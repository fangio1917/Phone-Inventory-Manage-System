from fastapi import APIRouter
from controller.users import router_users
from controller.inventory import router_inventory


router_api = APIRouter()

router_api.include_router(router_users, prefix="/users")
router_api.include_router(router_inventory, prefix="/inventory")
