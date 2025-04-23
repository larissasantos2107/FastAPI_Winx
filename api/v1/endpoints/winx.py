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
async def get_winx(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(WinxsModel)
        result = await session.execute(query)
        winx: List[WinxsModel] = result.scalars().all()
        
        return winx
    
@router.get("/{winx_id}", response_model=WinxShema)
async def get_winx(winx_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(WinxsModel).filter(WinxsModel.id == winx_id)
        result = await session.execute(query)
        winx = result.scalar_one_or_none()
        
        if winx:
            return winx
        else:
            raise HTTPException(detail="Winx não encontrado", status_code=status.HTTP_404_NOT_FOUND)
        
        
@router.put("/{winx_id}", response_model=WinxShema, status_code=status.HTTP_202_ACCEPTED)
async def put_winx(winx_id: int, winx: WinxShema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(WinxsModel).filter(WinxsModel.id == winx_id)
        result = await session.execute(query)
        winx_up = result.scalar_one_or_none()
        
        if winx_up:
            winx_up.nome = winx.nome
            winx_up.poder = winx.poder
            winx_up.mundo = winx.mundo
            winx_up.pertenceWinx = winx.pertenceWinx
            winx_up.foto = winx.foto
            
            await session.commit()
            return winx_up
        else:
            raise HTTPException(detail="Winx não encontrado", status_code=status.HTTP_404_NOT_FOUND)
        

@router.delete("/{winx_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_winx(winx_id:int, db: AsyncSession =  Depends(get_session)):
    async with db as session:
        query = select(WinxsModel).filter(WinxsModel.id == winx_id)
        result = await session.execute(query)
        winx_del = result.scalar_one_or_none()
        
        if winx_del:
            await session.delete(winx_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Winx não encontrado", status_code=status.HTTP_404_NOT_FOUND)