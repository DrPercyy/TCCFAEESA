#classe princeipal que realiza a chamada dos métodos da classe DataAccess
from Classes.dataaccess import MySQLConnector
import Classes.string_question as string_question
import Classes.question as question
from Classes.dataoperation import Curso, Disciplina, Conteudo, Questao


question_string = string_question.FileManager().read_file_to_string()
questoes = question.QuestionList.list_question(question_string)




#print(Curso().select_disciplina_curso(6))
#print(Curso().select_curso(6))
#print(Disciplina().select_disciplina())

#Conteudo().insert_conteudo("Numeros", 1)

#print(Disciplina().select_conteudo_disciplina(1))


Curso().insert_curso("Ciencia da Computacao")   
Disciplina().insert_disciplina("Laboratorio de Programacao I", 1)
Conteudo().insert_conteudo("Arranjos", 1)
Questao().insert_question_list(questoes, 1)