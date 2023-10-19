from Classes import dataaccess
from Classes.dataoperation import Curso, Disciplina, Conteudo, Aluno, Matricula, Notas, HistProva, Questao
from Classes.parse_latex import ParseLatex, QrCode
from datetime import datetime

class Student:


    def enroll_student(self, id, course_id):       
        course_disciplines = []
        try:
            for curso in Curso.select_curso(self, course_id):
                for discipline in Curso().select_disciplina_curso(curso[0]):
                    course_disciplines.append(discipline[0])
            
            for discipline in course_disciplines:
                Matricula.insert_matricula(self, id, discipline)    
            return "SUCESSO"
        except Exception as e:
            return e


class Exam:
    def generate_exam_by_aluno(self):

        print("Quando a prova será aplicada?")
        try:
            date = input("dd/mm/aaaa: ")
            date = datetime.strptime(date, '%d/%m/%Y')
        except ValueError:
            print("Data inválida!")
            #Main().inserirDados()
        
        list_matricula = []
        print("Deseja Gerar uma prova para qual aluno?")
        for aluno in Aluno().select_aluno():
            print("ID: " + str(aluno[0]) + " - " + str(aluno[1]))

        try:
            id_aluno = int(input("DIGITE O ID: "))
        except ValueError:
            print("Opcao invalida!")


        for matricula in Matricula().select_matricula_by_aluno(id_aluno):
             list_matricula.append(matricula[0])
        
        questionário = []
        alters = []
        gab = []
        for matricula in list_matricula:
            list_questão = Questao().select_questao_by_conteudo(matricula)
            for questao in list_questão:
                alternativas = questao[1].split(' -- ')
                # Formatar os dados no estilo desejado
                enunciado = questao[0]
                
                # Obtém o gabarito no formato desejado
                gabarito = [f"{i+1} - {letra}" for i, letra in enumerate('ABCDE') if "1" == questao[2].split(' -- ')[i]]
                q = []
                q.append(enunciado)
                questionário.append(q)
                alters.append(alternativas)
                gab.append(gabarito)

        HistProva().insert_historico(gab, date, id_aluno)

        idprova = HistProva().select_historico_by_data_and_aluno(date, id_aluno)[0][0]

        print("Gerando prova...")
        QrCode().generate_qrcode(idprova)
        prova = ParseLatex(questionário, alters, "Prova - "+str(idprova),  Disc, "Professor", "TESTE", len(questionário))
        prova.generate_latex()
        prova.generate_pdf()
        print("Prova gerada com sucesso!")

        pass