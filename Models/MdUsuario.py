from EnEnum import EnTipoDocumento
from MdBase import MdBase

class MdUsuario(MdBase):
    TipoDocumento: int
    Documento: str
    PrimerNombre: str
    SegundoNombre: str
    PrimerApellido: str
    SegundoApellido: str
    Email: str
    __NombreCompleto:str

    def __init__(self, tipoDocumento, documento) -> None:
        super().__init__()
        self.TipoDocumento = tipoDocumento
        self.Documento = documento
