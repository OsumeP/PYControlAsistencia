import sys
sys.path.append("Repository")
from ast import List
from ClDataBase import ClDataBase
from MdBase import MdBase
import pyodbc
from typing import (List, Self)
from MdUsuario import MdUsuario

class MdAsignatura(MdBase):
    Nombre: str

    def __init__(self,nombre: str) -> None:
        super().__init__()
        self.Nombre = nombre


    def ObtenerTodos() -> List[Self]:
        cursor = ClDataBase.OpenConnection()
        cursor.execute("SELECT * FROM MdAsignatura")
        cursorData = cursor.fetchall()
        listResult = list()
        for i in cursorData:
            listResult.append(MdAsignatura.__CargarRegistro(i))
        ClDataBase.CloseConnection(cursor)
        return listResult
    
    def ObtenerPorNombre(name: str) -> Self:
        cursor = ClDataBase.OpenConnection()
        cursor.execute(f"SELECT * FROM MdAsignatura WHERE Nombre={name}")
        objData = cursor.fetchone()
        ClDataBase.CloseConnection(cursor)
        return MdAsignatura.__CargarRegistro(objData)
    
    def ObtenerPorId(id: int) -> Self:
        cursor = ClDataBase.OpenConnection()
        cursor.execute(f"SELECT * FROM MdAsignatura WHERE Id={id}")
        objData = cursor.fetchone()
        ClDataBase.CloseConnection(cursor)
        return MdAsignatura.__CargarRegistro(objData)
    
    def InsertarRegistro(self) -> None:
        cursor = ClDataBase.OpenConnection()
        strInsert = f"""INSERT INTO MdAsignatura
           (Nombre)
     VALUES
           ('{self.Nombre}')"""
        cursor.execute(strInsert)
        cursor.commit()
        ClDataBase.CloseConnection(cursor)

    def ValidarAsignatura(self) -> bool: 
        cursor = ClDataBase.OpenConnection()
        strSearch = f"SELECT Id FROM MdAsignatura WHERE Nombre='{self.Nombre}'"
        cursor.execute(strSearch)
        objValor = cursor.fetchval()
        return objValor != None
    
    def ActualizarRegistro(self):
        cursor = ClDataBase.OpenConnection()
        strUpdate = f"""UPDATE MdAsignatura SET 
            Nombre= '{self.Nombre}'
            WHERE Id= {self.Id}"""  
        cursor.execute(strUpdate)
        cursor.commit()
        ClDataBase.CloseConnection(cursor)
    
    def EliminarRegistro(id):
        cursor = ClDataBase.OpenConnection()
        strDelete = f"""DELETE FROM MdAsignatura WHERE Id={id}"""
        cursor.execute(strDelete)
        cursor.commit()
        ClDataBase.CloseConnection(cursor)
    
    def __CargarRegistro(row: pyodbc.Row) -> Self:
        if row == None:
            return None
        objResult = MdAsignatura(row.Nombre)
        objResult.EstablecerId(row.Id)
        return objResult