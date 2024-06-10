from EnEnum import EnTipoUsuario

class MdInicioSesion():
    Id: int
    Usuario: str
    Password: str
    TipoUsuario: EnTipoUsuario
    IsLogin: bool