import mysql.connector

dbcon= ('localhost', 'root', 'tcc01', 'tccapp')

class MySQLConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexão estabelecida com sucesso!")
            return "Conexão estabelecida com sucesso!"
        except mysql.connector.Error as err:
            print(f"Erro na conexão com o banco de dados: {err}")
            return f"Erro na conexão com o banco de dados: {err}"

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexão encerrada!")

    def execute_query(self, query, data=None):
        try:
            cursor = self.connection.cursor()
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except mysql.connector.Error as err:
            self.connection.rollback()
            print( f"Erro ao executar o select: {err}")
            return f"Erro ao executar o select: {err}"

    def execute_insert(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Insert executado com sucesso!")
            return cursor.lastrowid
        except mysql.connector.Error as err:
            self.connection.rollback()
            print(f"Erro ao executar o insert: {err}")
            return f"Erro ao executar o insert: {err}"
    

    def execute_update(self, query, data=None):
        try:
            cursor = self.connection.cursor()
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            self.connection.commit()
        except mysql.connector.Error as err:
            self.connection.rollback()
            return f"Erro ao executar o update: {err}"
        
    def execute_delete(self, query, data=None):
        try:
            cursor = self.connection.cursor()
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            self.connection.commit()
        except mysql.connector.Error as err:
            self.connection.rollback()
            return f"Erro ao executar o delete: {err}"
    
    def execute_count(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            cursor.fetchall()
            return cursor.rowcount
        except mysql.connector.Error as err:
            self.connection.rollback()
            return f"Erro ao executar o count: {err}"
        
  