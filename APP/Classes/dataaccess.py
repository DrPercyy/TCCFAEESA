import mysql.connector

import mysql.connector

class MySQLConnector:
    """
    A class used to connect to a MySQL database and execute queries.

    Attributes
    ----------
    host : str
        The hostname of the MySQL server.
    user : str
        The username used to connect to the MySQL server.
    password : str
        The password used to connect to the MySQL server.
    database : str
        The name of the database to connect to.

    Methods
    -------
    connect()
        Connects to the MySQL server.
    disconnect()
        Disconnects from the MySQL server.
    execute_query(query, data=None)
        Executes a SELECT query on the MySQL server.
    execute_insert(query)
        Executes an INSERT query on the MySQL server.
    execute_update(query, data=None)
        Executes an UPDATE query on the MySQL server.
    execute_delete(query, data=None)
        Executes a DELETE query on the MySQL server.
    next_id(query)
        Get the next available ID for a given table.
    """
    def __init__(self, host='localhost', user='TCCAPP', password='TCC01', database='tccapp'):
        """
        Parameters
        ----------
        host : str, optional
            The hostname of the MySQL server. Default is 'localhost'.
        user : str, optional
            The username used to connect to the MySQL server. Default is 'TCCAPP'.
        password : str, optional
            The password used to connect to the MySQL server. Default is 'TCC01'.
        database : str, optional
            The name of the database to connect to. Default is 'tccapp'.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
    
    def connect(self):
        """
        Connects to the MySQL server.

        Returns
        -------
        str
            A message indicating whether the connection was successful or not.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return "Conexão estabelecida com sucesso!"
        except mysql.connector.Error as err:
            return f"Erro na conexão com o banco de dados: {err}"

    def disconnect(self):
        """
        Disconnects from the MySQL server.
        """
        if self.connection:
            self.connection.close()
            return "Conexão encerrada!" 

    def execute_query(self, query, data=None):
        """
        Executes a SELECT query on the MySQL server.

        Parameters
        ----------
        query : str
            The SELECT query to execute.
        data : tuple, optional
            A tuple containing the values to be inserted into the query. Default is None.

        Returns
        -------
        list
            A list of tuples containing the results of the query.
        """
        db = MySQLConnector()
        db.connect()
        try:
            cursor = self.connection.cursor()
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except mysql.connector.Error as err:
            self.connection.rollback()
            return f"Erro ao executar o select: {err}"

    def execute_insert(self, query):
        """
        Executes an INSERT query on the MySQL server.

        Parameters
        ----------
        query : str
            The INSERT query to execute.
        
        Returns
        -------
        int
            The ID of the last inserted row.
        """
        db = MySQLConnector()
        db.connect()
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            return "Insert executado com sucesso!"
        except mysql.connector.Error as err:
            self.connection.rollback()
            return f"Erro ao executar o insert: {err}"
    

    def execute_update(self, query, data=None):
        """
        Executes an UPDATE query on the MySQL server.

        Parameters
        ----------
        query : str
            The UPDATE query to execute.
        data : tuple, optional
            A tuple containing the values to be inserted into the query. Default is None.
        """
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
        """
        Executes a DELETE query on the MySQL server.

        Parameters
        ----------
        query : str
            The DELETE query to execute.
        data : tuple, optional
            A tuple containing the values to be inserted into the query. Default is None.
        """
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
    
    def next_id(self, query):
            """
            Get the next available ID for a given table.

            Args:
                query (str): The name of the table to get the next ID for.

            Returns:
                int: The next available ID for the given table.

            Raises:
                mysql.connector.Error: If there is an error executing the SQL query.
            """
            try:
                cursor = self.connection.cursor()
                cursor.execute("SHOW TABLE STATUS LIKE '" + query + "'")
                quant = cursor.fetchall()
                if quant[0][10] == None:
                    quant = 1
                else:
                    quant = quant[0][10]
                return quant
            except mysql.connector.Error as err:         
                self.connection.rollback()
                return f"Erro ao retornar o ID: {err}"

