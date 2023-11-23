import sys
from typing import List, Self
sys.path.append("Repository")
import pyodbc
from ClDataBase import ClDataBase
from MdAsignatura import MdAsignatura
from MdBase import MdBase
from MdDocente import MdDocente
from datetime import datetime


class MdClase(MdBase):
    Id: int
    Docente: MdDocente
    Asignatura: MdAsignatura
    FechaInicial: datetime
    FechaFinal: datetime

    def __init__(self, Docente: MdDocente, Asignatura: MdAsignatura, FechaInicial: datetime) -> None:
        super().__init__()
        self.Docente = Docente
        self.Asignatura = Asignatura
        self.FechaInicial = FechaInicial.strftime('%Y-%m-%d %H:%M:%S')

    def InsertarRegistro(self) -> None:
        cursor = ClDataBase.OpenConnection()
        strInsert = f"""INSERT INTO MdClase
           (Id_Asignatura
           ,Id_Docente
           ,FechaInicio
           ,FechaFinal)
     VALUES
           ({self.Asignatura.Id}
           , {self.Docente.Id}
           ,'{self.FechaInicial}'
           ,'{self.FechaFinal}')"""
        cursor.execute(strInsert)
        cursor.commit()
        ClDataBase.CloseConnection(cursor)

    def ObtenerTodos() -> List[Self]:
        cursor = ClDataBase.OpenConnection()
        cursor.execute("SELECT * FROM MdClase")
        cursorData = cursor.fetchall()
        listResult = list()
        for i in cursorData:
            listResult.append(MdClase.__CargarRegistro(i))
        ClDataBase.CloseConnection(cursor)
        return listResult
    
    def ObtenerPorId(id: int) -> Self:
        cursor = ClDataBase.OpenConnection()
        cursor.execute(f"SELECT * FROM MdClase WHERE Id={id}")
        objData = cursor.fetchone()
        ClDataBase.CloseConnection(cursor)
        return MdClase.__CargarRegistro(objData)
    
    def __CargarRegistro(row: pyodbc.Row) -> Self:
        if row == None:
            return None
        objDocente = MdDocente.ObtenerPorId(row.Id_Docente)
        objAsignatura = MdAsignatura.ObtenerPorId(row.Id_Asignatura)
        objResult = MdClase(objDocente, objAsignatura, row.FechaInicio)
        objResult.FechaFinal = row.FechaFinal
        objResult.EstablecerId(row.Id)
        return objResult