# parte 7

from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.winx_models import WinxsModel
from schemas.winx_schemas import WinxShema
from core.deps import get_session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=WinxShema)
async def post_winx(winx: WinxShema, db: AsyncSession = Depends(get_session)):
    nova_winx = WinxsModel(nome = winx.nome,
                           poder = winx.poder,
                           mundo = winx.mundo,
                           pertenceWinx = winx.pertenceWinx,
                           foto = winx.foto)
    
    db.add(nova_winx)
    
    await db.commit()
    
    return nova_winx

@router.get("/", response_model=List[WinxShema])
async def