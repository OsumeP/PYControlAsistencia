import pyodbc

class ClDataBase():

    def __SetupConnection() -> str:
        OdbcDriver = 'ODBC Driver 17 for SQL Server'
        Servidor = '(Local)'
        BaseDatos = 'BDControlAsistencia'
        Usuario = 'sa'
        Password = 'CC80737015'
        return f'DRIVER={{{OdbcDriver}}};SERVER={Servidor};DATABASE={BaseDatos};UID={Usuario};PWD={Password}'

    def OpenConnection() -> pyodbc.Cursor:
        connectionString = ClDataBase.__SetupConnection()
        conn = pyodbc.connect(connectionString)
        return conn.cursor()
    
    def CloseConnection(cursor : pyodbc.Cursor) -> None:
        conn = cursor.connection
        cursor.close()
        conn.close()
        

