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
        query = "SELECT * FROM DISCIPLINA WHERE ID IN (SELECT DISCIPLINA_ID FROM CURSO_HAS_DISCIPLINA WHERE CURSO_ID = {})".format(id_curso)
        result = db.execute_query(query)
        db.disconnect()
        return result

#classe que irá manipular a tabela Disciplina que contém as seguintes colunas (id_disciplina, nome_disciplina)
class Disciplina:

    #função que insere uma disciplina no banco de dados e relaciona com o curso utilizando a tabela CURSO_HAS_DISCIPLINA
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
        

    #funçao que faz um link entre uma disciplina e um curso
    def insert_disciplina_curso(self, id_disciplina, id_curso):
        db = MySQLConnector()
        db.connect()
        query = "INSERT INTO CURSO_HAS_DISCIPLINA (DISCIPLINA_ID, CURSO_ID) VALUES ({}, {})".format(id_disciplina, id_curso)
        db.execute_insert(query)
        db.disconnect()


#classe que irá manipular a tabela Conteudo que contém as seguintes colunas (id_conteudo, nome_conteudo)
class Conteudo:
    
        #função que insere um conteúdo no banco de dados e relaciona com a disciplina utilizando a tabela conteudo_has_disciplina
        def insert_conteudo(self, nome_conteudo, id_disciplina):
            db = MySQLConnector()
            db.connect()
            query = "INSERT INTO CONTEUDO (nome_conteudo, DISCIPLINA_ID) VALUES ('{}', {})".format(nome_conteudo, id_disciplina)
            db.execute_insert(query)
            db.disconnect()
        
        #função que retorna todos os conteúdos cadastrados no banco de dados, se o conteudo do ID for diferente de None, retorna apenas os conteudos do ID da disciplina
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
                query = "SELECT * FROM CONTEUDO WHERE DISCIPLINA_ID = {}".format(id)
                result = db.execute_query(query)
                db.disconnect()
                return result
    
##classe que irá manipular a tabela Questao juntamente com as alternativas que contém as seguintes colunas (ID_QUESTAO, TEXTO_QUESTAO, NIVEL__QUESTAO, CONTEUDO_ID_CONTUDO) E (ID_ALTERNATIVA, QUESTAO_ID_QUESTAO, ALTER_TEXTO, ALTER_CORR).

class Questao:
    #FUNCAO QUE RECEBE UMA QUESTION_LIST E INSERE NO BANCO DE DADOS


    def insert_question_list(self, question_list, disciplina_id ,conteudo_id):
        db = MySQLConnector()
        db.connect()
        for question in question_list.question_list:
            query = "INSERT INTO QUESTAO (texto_questao, nivel_questao, DISCIPLINA_ID , CONTEUDO_ID) VALUES ("+question.statement.to_string()+", 1,{}, {})".format(disciplina_id, conteudo_id)
            db.execute_insert(query)
            for option in question.options.option_list:
                query = "INSERT INTO ALTERNATIVA (QUESTAO_ID, alter_texto, alter_corr) VALUES ("+option.to_string()+")"
                db.execute_insert(query)
        db.disconnect()


    def select_questao_by_disciplina(self, id_disciplina):
        db = MySQLConnector()
        db.connect()
        query = "SELECT questao.texto_questao as Questao, GROUP_CONCAT(alternativa.alter_texto SEPARATOR ' -- ') AS Alternativas"+(
        " FROM questao")+(
        " INNER JOIN alternativa ON questao.id = alternativa.questao_id")+(
        " where questao.conteudo_id = "+str(id_disciplina)+"")+(
        " GROUP BY questao.texto_questao;")
        result = db.execute_query(query)
        db.disconnect()
        return result
    
    def select_questao_by_conteudo(self, id_conteudo):
        db = MySQLConnector()
        db.connect()
        query = "SELECT questao.texto_questao as Questao, GROUP_CONCAT(alternativa.alter_texto SEPARATOR ' -- ') AS Alternativas"+(
        " FROM questao")+(
        " INNER JOIN alternativa ON questao.id = alternativa.questao_id")+(
        " where questao.conteudo_id = "+str(id_conteudo)+"")+(
        " GROUP BY questao.texto_questao;")
        result = db.execute_query(query)
        db.disconnect()
        return result