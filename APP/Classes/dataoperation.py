#Arquivo utilizado para realizar operações com os dados do banco de dados
from Classes.dataaccess import MySQLConnector


 #classe que irá manipular a tabela Curso  que contém as seguintes colunas (id_curso, nome_curso)
class Curso:

    #função que insere um curso no banco de dados
    def insert_curso(self, nome_curso):
        db = MySQLConnector()
        db.connect()
        query = "INSERT INTO CURSO (nome_curso) VALUES ('{}')".format(nome_curso)
        db.execute_insert(query)
        db.disconnect()
    
    #função que retorna todos os cursos cadastrados no banco de dados
    def select_curso(self, id=None):

        if id == None:
            db = MySQLConnector()
            db.connect()
            query = "SELECT * FROM CURSO"
            result = db.execute_query(query)
            db.disconnect()
            return result
        else:
            db = MySQLConnector()
            db.connect()
            query = "SELECT * FROM CURSO WHERE ID = {}".format(id)
            result = db.execute_query(query)
            db.disconnect()
            return result
        
    #funçao que retorna todas as disciplinas relacionadas a um curso
    def select_disciplina_curso(self, id_curso):
        db = MySQLConnector()
        db.connect()
        query = "SELECT * FROM DISCIPLINA WHERE id_disciplina IN (SELECT DISCIPLINA_id_disciplina FROM DISCIPLINA_HAS_CURSO WHERE CURSO_id_curso = {})".format(id_curso)
        result = db.execute_query(query)
        db.disconnect()
        return result

#classe que irá manipular a tabela Disciplina que contém as seguintes colunas (id_disciplina, nome_disciplina)
class Disciplina:

    #função que insere uma disciplina no banco de dados e relaciona com o curso utilizando a tabela disciplina_has_curso
    def insert_disciplina(self, nome_disciplina, id_curso):
        db = MySQLConnector()
        db.connect()
        query = "INSERT INTO DISCIPLINA (nome_disciplina) VALUES ('{}')".format(nome_disciplina)
        db.execute_insert(query)
        query = "INSERT INTO CURSO_HAS_DISCIPLINA (DISCIPLINA_ID, CURSO_ID) VALUES ((SELECT ID FROM DISCIPLINA WHERE nome_disciplina = '{}'), (SELECT id FROM CURSO WHERE id = {}))".format(nome_disciplina, id_curso)
        db.execute_insert(query)
        db.disconnect()
    
    #função que retorna todas as disciplinas cadastradas no banco de dados
    def select_disciplina(self, id=None):

        if id == None:
            db = MySQLConnector()
            db.connect()
            query = "SELECT * FROM DISCIPLINA"
            result = db.execute_query(query)
            db.disconnect()
            return result
        else:
            db = MySQLConnector()
            db.connect()
            query = "SELECT * FROM DISCIPLINA WHERE ID = {}".format(id)
            result = db.execute_query(query)
            db.disconnect()
            return result
        
    #função que retorna todos os conteúdos relacionados a uma disciplina
    def select_conteudo_disciplina(self, id_disciplina):
        db = MySQLConnector()
        db.connect()
        query = "SELECT * FROM CONTEUDO WHERE id_conteudo IN (SELECT CONTEUDO_id_conteudo FROM CONTEUDO_HAS_DISCIPLINA WHERE DISCIPLINA_id_disciplina = {})".format(id_disciplina)
        result = db.execute_query(query)
        db.disconnect()
        return result
        
#classe que irá manipular a tabela Conteudo que contém as seguintes colunas (id_conteudo, nome_conteudo)
class Conteudo:
    
        #função que insere um conteúdo no banco de dados e relaciona com a disciplina utilizando a tabela conteudo_has_disciplina
        def insert_conteudo(self, nome_conteudo, id_disciplina):
            db = MySQLConnector()
            db.connect()
            query = "INSERT INTO CONTEUDO (nome_conteudo, DISCIPLINA_ID) VALUES ('{}', {})".format(nome_conteudo, id_disciplina)
            db.execute_insert(query)
            db.disconnect()
        
        #função que retorna todos os conteúdos cadastrados no banco de dados
        def select_conteudo(self, id=None):

            if id == None:
                db = MySQLConnector()
                db.connect()
                query = "SELECT * FROM CONTEUDO"
                result = db.execute_query(query)
                db.disconnect()
                return result
            else:
                db = MySQLConnector()
                db.connect()
                query = "SELECT * FROM CONTEUDO WHERE ID = {}".format(id)
                result = db.execute_query(query)
                db.disconnect()
                return result
    
##classe que irá manipular a tabela Questao juntamente com as alternativas que contém as seguintes colunas (ID_QUESTAO, TEXTO_QUESTAO, NIVEL__QUESTAO, CONTEUDO_ID_CONTUDO) E (ID_ALTERNATIVA, QUESTAO_ID_QUESTAO, ALTER_TEXTO, ALTER_CORR).

class Questao:
    #FUNCAO QUE RECEBE UMA QUESTION_LIST E INSERE NO BANCO DE DADOS


    def insert_question_list(self, question_list, id_conteudo):
        db = MySQLConnector()
        db.connect()
        for question in question_list.question_list:
            query = "INSERT INTO QUESTAO (texto_questao, nivel_questao, CONTEUDO_ID) VALUES ("+question.statement.to_string()+", 1, {})".format(id_conteudo)
            db.execute_insert(query)
            for option in question.options.option_list:
                query = "INSERT INTO ALTERNATIVA (QUESTAO_ID, alter_texto, alter_corr) VALUES ("+option.to_string()+")"
                db.execute_insert(query)
        db.disconnect()