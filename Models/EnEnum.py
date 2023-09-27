from enum import Enum

class EnTipoDocumento(Enum):
    NA = 0
    CC = 1
    CE = 2
    TI = 3
    PT = 4

class EnTipoUsuario(Enum):
    Administrador = 0
    Docente = 1
    Estudiante = 2