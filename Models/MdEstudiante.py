import pyodbc
from typing import (List, Self)
import sys
sys.path.append("Repository")
from MdUsuario import MdUsuario
from ClDataBase import ClDataBase

class MdEstudiante(MdUsuario):

    NumeroCarne : str
    Foto : bytearray
    Vector : any

    def __init__(self, tipoDocumento, documento) -> None:
        super().__init__(tipoDocumento, documento)

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
        return objResult
    
    def ObtenerTodos() -> List[Self]:
        cursor = ClDataBase.AbrirConexion()
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
    
    def ObtenerImg(self) -> bytearray:
        cursor = ClDataBase.OpenConnection()
        cursor.execute(f"SELECT * FROM MdEstudiante WHERE Id={self.id}")
        objData = cursor.fetchone()
        ClDataBase.CloseConnection(cursor)
        return objData.Foto
    
    #def ObtenerVector(self) -> bytearray:
        cursor = ClDataBase.OpenConnection()
        cursor.execute(f"SELECT * FROM MdEstudiante WHERE Id={self.id}")
        objData = cursor.fetchone()
        ClDataBase.CloseConnection(cursor)
        return objData.Vector
    
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
           ,NumeroCarne)
     VALUES
           ({self.TipoDocumento}
           ,'{self.Documento}'
           ,'{self.PrimerNombre}'
           ,'{self.SegundoNombre}'
           ,'{self.PrimerApellido}'
           ,'{self.SegundoApellido}'
           ,'{self.Email}'
           ,'{self.NumeroCarne}')"""
        cursor.execute(strInsert)
        cursor.commit()
        ClDataBase.CloseConnection(cursor)

    def EliminarRegistro(self):
        cursor = ClDataBase.OpenConnection()
        strDelete = f"""DELETE FROM MdEstudiante WHERE Id={self.Id}"""
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
            NumeroCarne= '{self.NumeroCarne}'
            WHERE Id= {self.Id}"""  
        cursor.execute(strUpdate)
        cursor.commit()
        ClDataBase.CloseConnection(cursor)

# aaa = MdEstudiante(1,'341241')
# aaa.PrimerNombre = 'Astrid'
# aaa.PrimerApellido = 'Sánchez'
# aaa.Email = 'test@test.com'
# aaa.NumeroCarne = '432345'
# aaa.Foto = bytearray([3])
# aaa.InsertarRegistro()
# bbb = MdEstudiante.ObtenerPorId(1)
# bbb.SegundoNombre = 'Test'
# bbb.ActualizarRegistro()