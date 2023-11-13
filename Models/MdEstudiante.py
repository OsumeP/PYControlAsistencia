import sys

from MdInicioSesion import MdInicioSesion
sys.path.append("Repository")
sys.path.append("FaceRecognition")
import pyodbc
from typing import (List, Self)
from MdUsuario import MdUsuario
from ClDataBase import ClDataBase

class MdEstudiante(MdUsuario):

    NumeroCarne : str
    Foto : bytes
    Vector : bytes

    def __init__(self, tipoDocumento, documento) -> None:
        super().__init__(tipoDocumento, documento)
        self.Foto = None
        self.Vector = None

    def __CargarRegistro(row: pyodbc.Row) -> Self:
        if row == None:
            return None
        objResult = MdEstudiante(row.TipoDocumento, row.Documento)
        objResult.EstablecerId(row.Id)
        objResult.PrimerNombre = row.PrimerNombre
        objResult.SegundoNombre = row.SegundoNombre
        objResult.PrimerApellido = row.PrimerApellido
        objResult.SegundoApellido = row.SegundoApellido
        objResult.Email = row.Email
        objResult.NumeroCarne = row.NumeroCarne
        objResult.Foto = row.Foto
        objResult.Vector = row.Vector
        return objResult
    
    def ObtenerTodos() -> List[Self]:
        cursor = ClDataBase.OpenConnection()
        cursor.execute("SELECT * FROM MdEstudiante")
        cursorData = cursor.fetchall()
        listResult = list()
        for i in cursorData:
            listResult.append(MdEstudiante.__CargarRegistro(i))
        ClDataBase.CloseConnection(cursor)
        return listResult
    
    def ObtenerPorId(id: int) -> Self:
        cursor = ClDataBase.OpenConnection()
        cursor.execute(f"SELECT * FROM MdEstudiante WHERE Id={id}")
        objData = cursor.fetchone()
        ClDataBase.CloseConnection(cursor)
        return MdEstudiante.__CargarRegistro(objData)
    
    def ObtenerPorDocumento(documento: str) -> Self:
        cursor = ClDataBase.OpenConnection()
        cursor.execute(f"SELECT * FROM MdEstudiante WHERE Documento='{documento}'")
        objData = cursor.fetchone()
        ClDataBase.CloseConnection(cursor)
        return MdEstudiante.__CargarRegistro(objData)
    
    def CargarFoto(self) -> None:
        cursor = ClDataBase.OpenConnection()
        cursor.execute(f"SELECT Foto FROM MdEstudiante WHERE Id={self.id}")
        objData = cursor.fetchone()
        ClDataBase.CloseConnection(cursor)
        self.Foto = objData.Foto

    def CargarVector(self) -> None:
        cursor = ClDataBase.OpenConnection()
        cursor.execute(f"SELECT Vector FROM MdEstudiante WHERE Id={self.id}")
        objData = cursor.fetchone()
        ClDataBase.CloseConnection(cursor)
        self.Vector = objData.Vector
    
    def InsertarRegistro(self) -> None:
        cursor = ClDataBase.OpenConnection()
        strInsert = f"""INSERT INTO MdEstudiante
           (TipoDocumento
           ,Documento
           ,PrimerNombre
           ,SegundoNombre
           ,PrimerApellido
           ,SegundoApellido
           ,Email
           ,Password
           ,Activo
           ,NumeroCarne
           ,Foto
           ,Vector)
     VALUES
           ({self.TipoDocumento}
           ,'{self.Documento}'
           ,'{self.PrimerNombre}'
           ,'{self.SegundoNombre}'
           ,'{self.PrimerApellido}'
           ,'{self.SegundoApellido}'
           ,'{self.Email}'
           ,'123'
           ,1
           ,'{self.NumeroCarne}'
           ,?
           ,?)"""
        cursor.execute(strInsert, pyodbc.Binary(self.Foto), pyodbc.Binary(self.Vector))
        cursor.commit()
        ClDataBase.CloseConnection(cursor)

    def EliminarRegistro(id):
        cursor = ClDataBase.OpenConnection()
        strDelete = f"""DELETE FROM MdEstudiante WHERE Id={id}"""
        cursor.execute(strDelete)
        cursor.commit()
        ClDataBase.CloseConnection(cursor)

    def ActualizarRegistro(self):
        cursor = ClDataBase.OpenConnection()
        strUpdate = f"""UPDATE MdEstudiante SET 
            TipoDocumento= {self.TipoDocumento},
            Documento= '{self.Documento}',
            PrimerNombre= '{self.PrimerNombre}',
            SegundoNombre= '{self.SegundoNombre}', 
            PrimerApellido= '{self.PrimerApellido}', 
            SegundoApellido= '{self.SegundoApellido}', 
            Email= '{self.Email}', 
            NumeroCarne= '{self.NumeroCarne}',
            Foto=?,
            Vector=?
            WHERE Id= {self.Id}"""  
        cursor.execute(strUpdate, pyodbc.Binary(self.Foto), pyodbc.Binary(self.Vector))
        cursor.commit()
        ClDataBase.CloseConnection(cursor)
    
    def ValidarUsuario(mdInicioSesion : MdInicioSesion) -> bool:
        cursor = ClDataBase.OpenConnection()
        strSearch = f"SELECT Id FROM MdEstudiante WHERE Documento='{mdInicioSesion.Usuario}' AND Password='{mdInicioSesion.Password}' AND Activo=1"
        cursor.execute(strSearch)
        objValor = cursor.fetchval()
        return objValor != None
    
    def ValidarRepeticion(self) -> bool:
        cursor = ClDataBase.OpenConnection()
        strSearch = f"SELECT Id FROM MdEstudiante WHERE Documento='{self.Documento}' AND Id!={self.Id}"
        cursor.execute(strSearch)
        objValor = cursor.fetchval()
        return objValor != None
    
    def AsignarFotoVector(self):
        from MdFaceRecognition import MdFaceRecognition
        reconocedor = MdFaceRecognition(self)
        reconocedor.CapturarRostro()
    
    def SubirFoto(self, filePath: str):
        from MdFaceRecognition import MdFaceRecognition
        reconocedor = MdFaceRecognition(self)
        reconocedor.AnalizarImagen(filePath)
