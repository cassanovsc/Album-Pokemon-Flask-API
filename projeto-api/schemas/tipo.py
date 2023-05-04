from pydantic import BaseModel


class TipoSchema(BaseModel):
    """ Define como um novo tipo a ser inserido deve ser representado
    """
    tipo_id: int = 1
    nome: str = "Grama"
