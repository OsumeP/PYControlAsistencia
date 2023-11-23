import sys
from typing import List, Self
sys.path.append("Repository")
import pyodbc
from ClDataBase import ClDataBase
from MdClase import MdClase
from MdBase import MdBase
from MdEstudiante import MdEstudiante

class MdAsistencia(MdBase):
    Id: int
    Estudiante: MdEstudiante
    Clase: MdClase
    Asistencia: bool

    def __init__(self, Estudiante: MdEstudiante, Clase: MdClase, Asistencia: bool) -> None:
        super().__init__()
        self.Estudiante = Estudiante
        self.Clase = Clase
        self.Asistencia = Asistencia

    def InsertarRegistro(self) -> None:
        cursor = ClDataBase.OpenConnection()
        strInsert = f"""INSERT INTO MdAsistencia
           (Id_Asignatura
           ,Id_Docente
           ,Asistencia)
     VALUES
           ({self.Clase.Id}
           , {self.Estudiante.Id}
           ,{self.Asistencia})"""
        cursor.execute(strInsert)
        cursor.commit()
        ClDataBase.CloseConnection(cursor)

    def ObtenerTodos() -> List[Self]:
        cursor = ClDataBase.OpenConnection()
        cursor.execute("SELECT * FROM MdAsistencia")
        cursorData = cursor.fetchall()
        listResult = list()
        for i in cursorData:
            listResult.append(MdAsistencia.__CargarRegistro(i))
        ClDataBase.CloseConnection(cursor)
        return listResult
    
    def ObtenerPorId(id: int) -> Self:
        cursor = ClDataBase.OpenConnection()
        cursor.execute(f"SELECT * FROM MdAsistencia WHERE Id={id}")
        objData = cursor.fetchone()
        ClDataBase.CloseConnection(cursor)
        return MdAsistencia.__CargarRegistro(objData)
    
    def __CargarRegistro(row: pyodbc.Row) -> Self:
        if row == None:
            return None
        objDocente = MdEstudiante.ObtenerPorId(row.Id_Estudiante)
        objAsignatura = MdClase.ObtenerPorId(row.Id_Clase)
        objResult = MdAsistencia(objDocente, objAsignatura, row.Asistencia)
        objResult.EstablecerId(row.Id)
        return objResult