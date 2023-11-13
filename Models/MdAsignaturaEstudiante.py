import sys
sys.path.append("Repository")
from ast import List
from ClDataBase import ClDataBase
from MdBase import MdBase
from MdAsignatura import MdAsignatura
from MdEstudiante import MdEstudiante
import pyodbc
from typing import (List, Self)

class MdAsignaturaEstudiante(MdBase):
    Asignatura: MdAsignatura
    Estudiante: MdEstudiante

    def __init__(self, asignatura: MdAsignatura, estudiante: MdEstudiante) -> None:
        super().__init__()
        self.Asignatura = asignatura
        self.Estudiante = estudiante

    def InsertarRegistro(self) -> None:
        cursor = ClDataBase.OpenConnection()
        strInsert = f"""INSERT INTO MdAsignaturaEstudiante
           (Id_Asignatura
           ,Id_Estudiante)
     VALUES
           ({self.Asignatura.Id}
           ,{self.Estudiante.Id})"""
        cursor.execute(strInsert)
        cursor.commit()
        ClDataBase.CloseConnection(cursor)
    
    def EliminarRegistro(id):
        cursor = ClDataBase.OpenConnection()
        strDelete = f"""DELETE FROM MdAsignaturaEstudiante WHERE Id={id}"""
        cursor.execute(strDelete)
        cursor.commit()
        ClDataBase.CloseConnection(cursor)

    def EliminarRegistroIdEstudiante(idEstudiante, idAsignatura) -> None:
        cursor = ClDataBase.OpenConnection()
        strDelete = f"""DELETE FROM MdAsignaturaEstudiante WHERE Id_Estudiante={idEstudiante} AND Id_Asignatura={idAsignatura}"""
        cursor.execute(strDelete)
        cursor.commit()
        ClDataBase.CloseConnection(cursor)

    def ObtenerTodosPorIdAsignatura(id: int) -> List[Self]:
        cursor = ClDataBase.OpenConnection()
        cursor.execute(f"SELECT * FROM MdAsignaturaEstudiante WHERE Id_Asignatura={id}")
        cursorData = cursor.fetchall()
        listResult = list()
        for i in cursorData:
            listResult.append(MdAsignaturaEstudiante.__CargarRegistro(i))
        ClDataBase.CloseConnection(cursor)
        return listResult
    
    def ObtenerEstudiantesFaltantes(id: int) -> List[str]:
        cursor = ClDataBase.OpenConnection()
        cursor.execute(f"SELECT Id_Estudiante FROM MdAsignaturaEstudiante WHERE Id_Asignatura = {id}")
        cursorData = cursor.fetchall()
        ids = []
        listResult = []
        for i in cursorData:
            ids.append(i.Id_Estudiante)
        if len(ids) == 0:
            for i in MdEstudiante.ObtenerTodos():
               listResult.append(f"{i.Documento} {i.PrimerNombre} {i.PrimerApellido}")
            return listResult
        if len(ids) > 1:
            cursor.execute(f"SELECT CONCAT(Documento, ' ', PrimerNombre, ' ', PrimerApellido) FROM MdEstudiante WHERE Id NOT IN " + f"{tuple(ids)}")
        elif len(ids) == 1:
            cursor.execute(f"SELECT CONCAT(Documento, ' ', PrimerNombre, ' ', PrimerApellido) FROM MdEstudiante WHERE Id != {ids[0]}")
        cursorData = cursor.fetchall()
        for i in cursorData:
            listResult.append(i[0])
        ClDataBase.CloseConnection(cursor)
        return listResult
    
    def __CargarRegistro(row: pyodbc.Row) -> Self:
        if row == None:
            return None
        objAsignatura = MdAsignatura.ObtenerPorId(row.Id_Asignatura)
        objEstudiante = MdEstudiante.ObtenerPorId(row.Id_Estudiante)
        objResult = MdAsignaturaEstudiante(objAsignatura, objEstudiante)
        objResult.EstablecerId(row.Id)
        return objResult

    # def ValidarAsignatura(self) -> bool: 
    #     cursor = ClDataBase.OpenConnection()
    #     strSearch = f"SELECT Id FROM MdAsignatura WHERE Nombre='{self.Nombre}' AND Id != {self.Id}"
    #     cursor.execute(strSearch)
    #     objValor = cursor.fetchval()
    #     return objValor != None
    

    

    
