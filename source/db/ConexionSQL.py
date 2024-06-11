import pyodbc as sql

class ConexionSQL:

    app = '{SQL Server}'
    server = "DESKTOP-FEUFP03\\SQLEXPRESS"
    db = 'BarrioSeguro'
    user = 'adminuser'
    password = '1234'

    def ExecuteConnection(self):
        try:
            connection = sql.connect(f"DRIVER={self.app};SERVER={self.server};DATABASE={self.db};UID={self.user};PWD={self.password}")
        except Exception as e:
            print(e)
            
        return connection
