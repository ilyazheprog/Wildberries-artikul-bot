from api.products import router as products_r
from api.subscribe import router as subscribes_r
from fastapi import APIRouter

global_router = APIRouter(prefix="/api/v1")
global_router.include_router(products_r)
global_router.include_router(subscribes_r)
