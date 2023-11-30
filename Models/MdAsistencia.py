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
    Asistencia: int

    def __init__(self, Clase: MdClase, Asistencia = False, Estudiante: MdEstudiante = None) -> None:
        super().__init__()
        self.Clase = Clase
        if Asistencia == False:
            self.Asistencia = 0
        else:
            self.Asistencia = 1
        if Estudiante != None:
            self.Estudiante = Estudiante

    def GenerarRegistrosClase(self, ids: list[int]):
        for i in ids:
            self.Estudiante = MdEstudiante.ObtenerPorId(i)
            self.InsertarRegistro()

    def InsertarRegistro(self) -> None:
        cursor = ClDataBase.OpenConnection()
        strInsert = f"""INSERT INTO MdAsistencia
           (Id_Estudiante
           ,Id_Clase
           ,Asistencia)
     VALUES
           ({self.Estudiante.Id}
           , {self.Clase.Id}
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
    
    def ObtenerPorClase(idClase: int) -> list[Self]:
        cursor = ClDataBase.OpenConnection()
        strCommand =f"SELECT * FROM MdAsistencia WHERE Id_Clase={idClase}"
        cursor.execute(strCommand)
        objData = cursor.fetchall()
        listResult = []
        for row in objData:
            listResult.append(MdAsistencia.__CargarRegistro(row))
        ClDataBase.CloseConnection(cursor)
        return listResult
    
    def ActualizarRegistro(self):
        cursor = ClDataBase.OpenConnection()
        strUpdate = f"""UPDATE MdAsistencia SET 
            Asistencia = 1
            WHERE Id= {self.Id}"""  
        cursor.execute(strUpdate)
        cursor.commit()
        ClDataBase.CloseConnection(cursor)

    def ObtenerDatosPorEstudiante(Id: int) -> list[pyodbc.Row]:
        cursor = ClDataBase.OpenConnection()
        strSearch = f"SELECT Id_Docente, Id_Asignatura, FechaInicio, FechaFinal, Asistencia FROM MdClase A INNER JOIN MdAsistencia B ON A.Id = B.Id_Clase WHERE B.Id_Estudiante = {Id}"
        cursor.execute(strSearch)
        rows = cursor.fetchall()
        return rows

    def ObtenerPorId(id: int) -> Self:
        cursor = ClDataBase.OpenConnection()
        cursor.execute(f"SELECT * FROM MdAsistencia WHERE Id={id}")
        objData = cursor.fetchone()
        ClDataBase.CloseConnection(cursor)
        return MdAsistencia.__CargarRegistro(objData)
    
    def __CargarRegistro(row: pyodbc.Row) -> Self:
        if row == None:
            return None
        Estudiante = MdEstudiante.ObtenerPorId(row.Id_Estudiante)
        Clase = MdClase.ObtenerPorId(row.Id_Clase)
        objResult = MdAsistencia(Clase, row.Asistencia, Estudiante)
        objResult.EstablecerId(row.Id)
        return objResult