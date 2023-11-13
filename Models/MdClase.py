from MdAsignatura import MdAsignatura
from MdBase import MdBase
from MdDocente import MdDocente
from datetime import date


class MdClase(MdBase):
    Id: int
    Docente: MdDocente
    Asignatura: MdAsignatura
    FechaInicial: date
    FechaFinal: date
