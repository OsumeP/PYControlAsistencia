from EnEnum import EnTipoDocumento
from MdBase import MdBase

class MdUsuario(MdBase):
    TipoDocumento = EnTipoDocumento.NA
    Documento = '000'
    PrimerNombre = ''
    SegundoNombre = ''
    PrimerApellido = ''
    SegundoApellido = ''
    Email = ''
    __NombreCompleto = ''

    def __init__(self, tipoDocumento, documento) -> None:
        super().__init__()
        self.TipoDocumento = tipoDocumento
        self.Documento = documento
