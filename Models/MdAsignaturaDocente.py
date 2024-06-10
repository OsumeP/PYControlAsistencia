import sys
sys.path.append("Repository")
from ast import List
from ClDataBase import ClDataBase
from MdBase import MdBase
from MdAsignatura import MdAsignatura
from MdDocente import MdDocente
import pyodbc
from typing import (List, Self)

class MdAsignaturaDocente(MdBase):
    Asignatura: MdAsignatura
    Docente: MdDocente

    def __init__(self, asignatura: MdAsignatura, docente: MdDocente) -> None:
        super().__init__()
        self.Asignatura = asignatura
        self.Docente = docente

    def InsertarRegistro(self) -> None:
        cursor = ClDataBase.OpenConnection()
        strInsert = f"""INSERT INTO MdAsignaturaDocente
           (Id_Asignatura
           ,Id_Docente)
     VALUES
           ({self.Asignatura.Id}
           ,{self.Docente.Id})"""
        cursor.execute(strInsert)
        cursor.commit()
        ClDataBase.CloseConnection(cursor)
    
    def EliminarRegistro(id):
        cursor = ClDataBase.OpenConnection()
        strDelete = f"""DELETE FROM MdAsignaturaDocente WHERE Id={id}"""
        cursor.execute(strDelete)
        cursor.commit()
        ClDataBase.CloseConnection(cursor)

    def EliminarRegistroIdDocente(idEstudiante, idAsignatura) -> None:
        cursor = ClDataBase.OpenConnection()
        strDelete = f"""DELETE FROM MdAsignaturaDocente WHERE Id_Estudiante={idEstudiante} AND Id_Asignatura={idAsignatura}"""
        cursor.execute(strDelete)
        cursor.commit()
        ClDataBase.CloseConnection(cursor)

    def ObtenerTodosPorIdDocente(id: int) -> List[Self]:
        cursor = ClDataBase.OpenConnection()
        cursor.execute(f"SELECT * FROM MdAsignaturaDocente WHERE Id_Docente={id}")
        cursorData = cursor.fetchall()
        listResult = list()
        for i in cursorData:
            listResult.append(MdAsignaturaDocente.__CargarRegistro(i))
        ClDataBase.CloseConnection(cursor)
        return listResult
    
    def EliminarRegistroIdAsignatura(idDocente, idAsignatura) -> None:
        cursor = ClDataBase.OpenConnection()
        strDelete = f"""DELETE FROM MdAsignaturaDocente WHERE Id_Docente={idDocente} AND Id_Asignatura={idAsignatura}"""
        cursor.execute(strDelete)
        cursor.commit()
        ClDataBase.CloseConnection(cursor)
    
    def ObtenerAsignaturasFaltantes(id: int) -> List[str]:
        cursor = ClDataBase.OpenConnection()
        cursor.execute(f"SELECT Id_Asignatura FROM MdAsignaturaDocente WHERE Id_Docente = {id}")
        cursorData = cursor.fetchall()
        ids = []
        listResult = []
        for i in cursorData:
            ids.append(i.Id_Asignatura)
        if len(ids) == 0:
            for i in MdAsignatura.ObtenerTodos():
               listResult.append(f"{i.Nombre}")
            return listResult
        if len(ids) > 1:
            cursor.execute(f"SELECT Nombre FROM MdAsignatura WHERE Id NOT IN " + f"{tuple(ids)}")
        elif len(ids) == 1:
            cursor.execute(f"SELECT Nombre FROM MdAsignatura WHERE Id != {ids[0]}")
        cursorData = cursor.fetchall()
        for i in cursorData:
            listResult.append(i[0])
        ClDataBase.CloseConnection(cursor)
        return listResult
    
    def __CargarRegistro(row: pyodbc.Row) -> Self:
        if row == None:
            return None
        objAsignatura = MdAsignatura.ObtenerPorId(row.Id_Asignatura)
        objDocente = MdDocente.ObtenerPorId(row.Id_Docente)
        objResult = MdAsignaturaDocente(objAsignatura, objDocente)
        objResult.EstablecerId(row.Id)
        return objResult