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

    #Função que seleciona todas as questões de uma disciplina
    def select_questao_by_disciplina(self, id_disciplina):
        db = MySQLConnector()
        db.connect()
        query = "SELECT questao.texto_questao as Questao, GROUP_CONCAT(alternativa.alter_texto SEPARATOR ' -- ') AS Alternativas, GROUP_CONCAT(alternativa.ALTER_CORR SEPARATOR ' -- ') AS Correcoes "+(
        " FROM questao")+(
        " INNER JOIN alternativa ON questao.id = alternativa.questao_id")+(
        " where questao.disciplina_id = "+str(id_disciplina)+"")+(
        " GROUP BY questao.texto_questao;")
        result = db.execute_query(query)
        db.disconnect()
        return result
    
    #Função que seleciona todas as questões de um conteúdo
    def select_questao_by_conteudo(self, id_conteudo):
        db = MySQLConnector()
        db.connect()
        query = "SELECT questao.texto_questao as Questao, GROUP_CONCAT(alternativa.alter_texto SEPARATOR ' -- ') AS Alternativas, GROUP_CONCAT(alternativa.ALTER_CORR SEPARATOR ' -- ') AS Correcoes "+(
        " FROM questao")+(
        " INNER JOIN alternativa ON questao.id = alternativa.questao_id")+(
        " where questao.conteudo_id = "+str(id_conteudo)+"")+(
        " GROUP BY questao.texto_questao;")
        result = db.execute_query(query)
        db.disconnect()
        return result
    

#classe que irá manipular a tabela Aluno que contém as seguintes colunas (id_aluno, nome_aluno)
class Aluno:

    #função que insere um aluno no banco de dados
    def insert_aluno(self, nome_aluno):
        db = MySQLConnector()
        db.connect()
        query = "INSERT INTO ALUNO (NOME) VALUES ('{}')".format(nome_aluno)
        db.execute_insert(query)
        db.disconnect()
   
    #função que retorna todos os alunos cadastrados no banco de dados, se o id do aluno for diferente de None, retorna apenas o aluno do ID
    def select_aluno(self, id=None):            
            if id == None:
                db = MySQLConnector()
                db.connect()
                query = "SELECT * FROM ALUNO"
                result = db.execute_query(query)
                db.disconnect()
                return result
            else:
                db = MySQLConnector()
                db.connect()
                query = "SELECT * FROM ALUNO WHERE ID = {}".format(id)
                result = db.execute_query(query)
                db.disconnect()
                return result

    #função que retorna o aluno pelo nome        
    def select_aluno_by_nome(self, nome_aluno):
        db = MySQLConnector()
        db.connect()
        query = "SELECT * FROM ALUNO WHERE NOME_ALUNO = '{}'".format(nome_aluno)
        result = db.execute_query(query)
        db.disconnect()
        return result
    
    #função que retorna todos os alunos matriculados em uma disciplina
    def select_aluno_by_disciplina(self, id_disciplina):
        db = MySQLConnector()
        db.connect()
        query = "SELECT * FROM ALUNO WHERE ID IN (SELECT ALUNO_ID FROM MATRICULA WHERE DISCIPLINA_ID = {})".format(id_disciplina)
        result = db.execute_query(query)
        db.disconnect()
        return result
    

#classe que irá manipular a tabela Matricula que contém as seguintes colunas (id_matricula, aluno_id, disciplina_id, conteudo_id, status, quantidade_reprovados)
class Matricula:

    #função que insere uma matricula no banco de dados
    def insert_matricula(self, id_aluno, id_disciplina):
        db = MySQLConnector()
        db.connect()
        query = "INSERT INTO MATRICULA (ALUNO_ID, DISCIPLINA_ID) VALUES ({}, {})".format(id_aluno, id_disciplina)
        db.execute_insert(query)
        db.disconnect()
    
    #função que retorna todas as matriculas cadastradas no banco de dados, se o id da matricula for diferente de None, retorna apenas a matricula do ID
    def select_matricula(self, id=None):
        if id == None:
            db = MySQLConnector()
            db.connect()
            query = "SELECT * FROM MATRICULA"
            result = db.execute_query(query)
            db.disconnect()
            return result
        else:
            db = MySQLConnector()
            db.connect()
            query = "SELECT * FROM MATRICULA WHERE ID = {}".format(id)
            result = db.execute_query(query)
            db.disconnect()
            return result
    
    #função que retorna todas as matriculas de um aluno
    def select_matricula_by_aluno(self, id_aluno):
        db = MySQLConnector()
        db.connect()
        query = "SELECT * FROM MATRICULA WHERE ALUNO_ID = {}".format(id_aluno)
        result = db.execute_query(query)
        db.disconnect()
        return result
    
    #função que retorna todas as matriculas de uma disciplina
    def insert_status(self, disciplina_id, aluno_id, status):
        try:
            db = MySQLConnector()
            db.connect()
            query = "UPDATE MATRICULA SET STATUS = '{}' WHERE DISCIPLINA_ID = {} AND ALUNO_ID = {}".format(status, disciplina_id, aluno_id)
            db.execute_insert(query)
            db.disconnect()
        except Exception as e:
            return e

    #função que retorna a quantidade de reprovações de uma matricula
    def set_quantidade_reprovados(self, quant, disciplina_id, aluno_id):
        db = MySQLConnector()
        db.connect()
        query = "UPDATE MATRICULA SET QUANT_REPROVADO = {} WHERE DISCIPLINA_ID = {} AND ALUNO_ID = {}".format(quant, disciplina_id, aluno_id)
        db.execute_insert(query)
        db.disconnect()
    
    def select_quantidade_reprovados(self, disciplina_id, aluno_id):
        db = MySQLConnector()
        db.connect()
        query = "SELECT QUANT_REPROVADO FROM MATRICULA WHERE DISCIPLINA_ID = {} AND ALUNO_ID = {}".format(disciplina_id, aluno_id)
        result = db.execute_query(query)
        db.disconnect()
        return result

    #função que retorna uma matricula pelo status
    def select_matricula_by_status(self, status):
        db = MySQLConnector()
        db.connect()
        query = "SELECT * FROM MATRICULA WHERE STATUS = {}".format(status)
        result = db.execute_query(query)
        db.disconnect()
        return result


#class que irá manipular a tabela Notas que contém as seguintes colunas (id_nota, aluno_id, disciplina_id, conteudo_id, nota)
class Notas:

    #função que insere uma nota no banco de dados
    def insert_nota(self, id_aluno, id_disciplina, conteudo_id, nota):
        db = MySQLConnector()
        db.connect()
        query = "INSERT INTO NOTAS (ALUNO_ID, DISCIPLINA_ID, CONTEUDO_ID, NOTA) VALUES ({}, {}, {}, {})".format(id_aluno, id_disciplina, conteudo_id, nota)
        db.execute_insert(query)
        db.disconnect()

    #função que retorna todas as notas de um aluno
    def select_nota_by_aluno(self, id_aluno):
        db = MySQLConnector()
        db.connect()
        query = "SELECT * FROM NOTAS WHERE ALUNO_ID = {}".format(id_aluno)
        result = db.execute_query(query)
        db.disconnect()
        return result
    
    #função que retorna todas as notas de uma disciplina de um aluno ou de todos os alunos
    def select_nota_by_disciplina(self, id_disciplina, id_aluno):
        if id_aluno == None:
            db = MySQLConnector()
            db.connect()
            query = "SELECT * FROM NOTAS WHERE DISCIPLINA_ID = {}".format(id_disciplina)
            result = db.execute_query(query)
            db.disconnect()
            return result
        else:
            db = MySQLConnector()
            db.connect()
            query = "SELECT * FROM NOTAS WHERE DISCIPLINA_ID = {} AND ALUNO_ID = {}".format(id_disciplina, id_aluno)
            result = db.execute_query(query)
            db.disconnect()
            return result
    
    #função que retorna todas as notas de um conteudo de um aluno ou de todos os alunos
    def select_nota_by_conteudo(self, id_conteudo, id_aluno):
        if id_aluno == None:
            db = MySQLConnector()
            db.connect()
            query = "SELECT * FROM NOTAS WHERE CONTEUDO_ID = {}".format(id_conteudo)
            result = db.execute_query(query)
            db.disconnect()
            return result
        else:
            db = MySQLConnector()
            db.connect()
            query = "SELECT * FROM NOTAS WHERE CONTEUDO_ID = {} AND ALUNO_ID = {}".format(id_conteudo, id_aluno)
            result = db.execute_query(query)
            db.disconnect()
            return result
 
    
#class que irá manipular a tabela Historico de Provas que contém as seguintes colunas (id, gab_cod, data_prova, aluno_id)
class HistProva:

    #função que insere um historico de prova no banco de dados
    def insert_historico(self, gabarito, data_prova, id_aluno):
        db = MySQLConnector()
        db.connect()
        query = "INSERT INTO HIST_PROVA (GAB_COD, DATA_PROVA, ALUNO_ID) VALUES ('{}', '{}', {})".format(gabarito, data_prova, id_aluno)
        db.execute_insert(query)
        db.disconnect()
    
    #função que retorna todas as provas de um aluno
    def select_historico_by_aluno(self, id_aluno):
        db = MySQLConnector()
        db.connect()
        query = "SELECT * FROM HIST_PROVA WHERE ALUNO_ID = {}".format(id_aluno)
        result = db.execute_query(query)
        db.disconnect()
        return result
    
    #função que retorna todas as provas de uma data
    def select_historico_by_data(self, data_prova):
        db = MySQLConnector()
        db.connect()
        query = "SELECT * FROM HIST_PROVA WHERE DATA_PROVA = '{}'".format(data_prova)
        result = db.execute_query(query)
        db.disconnect()
        return result
    
    def select_historico_by_data_and_aluno(self, data_prova, id_aluno):
        db = MySQLConnector()
        db.connect()
        query = "SELECT * FROM HIST_PROVA WHERE DATA_PROVA = '{}' AND ALUNO_ID = {}".format(data_prova, id_aluno)
        result = db.execute_query(query)
        db.disconnect()
        return result

    #função que retorna todas uma prova pelo ID
    def select_historico_by_id(self, id):
        db = MySQLConnector()
        db.connect()
        query = "SELECT * FROM HIST_PROVA WHERE ID = {}".format(id)
        result = db.execute_query(query)
        db.disconnect()
        return result