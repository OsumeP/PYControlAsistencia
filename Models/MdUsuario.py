from EnEnum import EnTipoDocumento
from EnEnum import EnTipoUsuario
from MdAdministrador import MdAdministrador
from MdBase import MdBase
from MdInicioSesion import MdInicioSesion

class MdUsuario(MdBase):
    TipoDocumento: EnTipoDocumento
    Documento: str
    PrimerNombre: str
    SegundoNombre: str
    PrimerApellido: str
    SegundoApellido: str
    Email: str
    Password: str
    Activo: bool

    __NombreCompleto:str

    def __init__(self, tipoDocumento: int, documento: str) -> None:
        super().__init__()
        self.TipoDocumento = tipoDocumento
        self.Documento = documento
    
    def ValidarUsuario(inicioSesion: MdInicioSesion) -> bool:
        from MdDocente import MdDocente
        from MdEstudiante import MdEstudiante
        if inicioSesion.TipoUsuario == EnTipoUsuario.Docente:
            return MdDocente.ValidarUsuario(inicioSesion)
        elif inicioSesion.TipoUsuario == EnTipoUsuario.Estudiante:
            return MdEstudiante.ValidarUsuario(inicioSesion)
        elif inicioSesion.TipoUsuario == EnTipoUsuario.Administrador:
            return MdAdministrador.ValidarUsuario(inicioSesion)
        
    def ObtenerTipoDocumentoStr(self) -> str:
        match self.TipoDocumento:
            case 0:
                return "NA"
            case 1:
                return "CC"
            case 2:
                return "CE"
            case 3:
                return "TI"
            case 4:
                return "PT"