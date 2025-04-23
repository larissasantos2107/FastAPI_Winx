from core.configs import settings 
from sqlalchemy import Column, Integer, String

class WinxsModel(settings.DBBaseModel):
    __tablename__="Winx"
    
    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(256))
    poder: str = Column(String(256))
    mundo: str = Column(String(256))
    pertenceWinx: str = Column(String(255))
    foto: str = Column(String(256))
    
#parte 4