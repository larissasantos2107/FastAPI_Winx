from fastapi import APIRouter

from api.v1.endpoints import winx

api_router = APIRouter()

api_router.include_router(winx.router, prefix="/winx", tags=["Winx"])

# parte 8py