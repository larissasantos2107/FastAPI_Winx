from typing import Optional
from pydantic import BaseModel as SCBaseModel

class WinxShema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    poder: str
    mundo: str
    pertenceWinx: str
    foto: str

# parte 6