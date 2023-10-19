#classe princeipal que realiza a chamada dos métodos da classe DataAccess
from Classes.string_question import FileManager
import Classes.question as question
from Classes.dataoperation import Curso, Disciplina, Conteudo, Questao, Aluno, Matricula, Notas
from Classes.class_operation import Student, Exam
from Classes.parse_latex import ParseLatex, QrCode
import random, qrcode


class Main:

    def __init__(self, debug = False):
        if debug:
            print("Debug mode")
            pass

        else:

            while True:
                self.pagina_inicial()
    pass

    def pagina_inicial(self):
        print("Bem vindo ao TCCAPP!")
        print("O que deseja fazer?")
        print("1 - inserir dados")
        print("2 - listar dados")
        print("3 - sair")
        try:
            opcao = int(input())
        except ValueError:
            print("Opcao invalida!")
            self.pagina_inicial()

        if opcao == 1:
            self.inserirDados()
        elif opcao == 2:
            self.listarDados()
        elif opcao == 3:
            exit()
        else:
            print("Opcao invalida!")
            self.pagina_inicial()

    def inserirDados(self):
        print("1 - Inserir curso")
        print("2 - Inserir disciplina")
        print("3 - Inserir conteudo")
        print("4 - Linkar Curso a Disciplina")
        print("5 - Inserir questao")
        print("6 - Voltar")

        try:
            opcao = int(input())
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()

        if opcao == 1:
            self.inserirCurso()
        elif opcao == 2:
            self.inserirDisciplina()
        elif opcao == 3:
            self.inserirConteudo()
        elif opcao == 4:
            self.LinkarCursoDisciplina()
        elif opcao == 5:
            self.InserirQuestao()
        elif opcao == 6:
            self.pagina_inicial()
        else:   
            print("Opcao invalida!")
            self.inserirDados()
    
    def listarDados(self):
        print("1 - Listar cursos")
        print("2 - Listar disciplinas")
        print("3 - Listar conteudos")
        print("4 - Voltar")

        try:
            opcao = int(input())
        except ValueError:
            print("Opcao invalida!")
            self.listarDados()

        if opcao == 1:
            self.listarCursos()
        elif opcao == 2:
            self.listarDisciplinas()
        elif opcao == 3:
            self.listarConteudos()
        elif opcao == 4:
            self.pagina_inicial()
        else:
            print("Opcao invalida!")
            self.listarDados()

    def inserirCurso(self):
        nome_curso = input("Digite o nome do curso: ")
        opcao = input('Deseja inserir o curso "{}"? (S/N): '.format(nome_curso))
        if opcao == "S" or opcao == "s":
            print("Inserindo o curso {}...".format(nome_curso))
            Curso().insert_curso(nome_curso)
            self.inserirDados()
        else:
            print("Curso não inserido!")
            self.inserirDados()

    def inserirDisciplina(self):
        for curso in Curso().select_curso():
            print("ID: " + str(curso[0]) + " - " + str(curso[1]))
        try:
            id_curso = int(input("A qual curso deseja inserir a disciplina? (DIGITE O ID): "))
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()
        nome_disciplina = input("Digite o nome da disciplina: ")
        opcao = input('Deseja inserir a disciplina "'+ nome_disciplina+'" ao Curso "'+str(
            Curso().select_curso(id_curso)[0][1])+'"? (S/N): ')
        if opcao == "S" or opcao == "s":
            print("Inserindo a disciplina {}...".format(nome_disciplina))
            Disciplina().insert_disciplina(nome_disciplina, id_curso)
            self.inserirDados()
        else:
            print("Disciplina não inserida!")
            self.inserirDados()
    
    def inserirConteudo(self):

        for curso in Curso().select_curso():
            print("ID: " + str(curso[0]) + " - " + str(curso[1]))
        try:
            id_curso = int(input("A qual curso deseja inserir o conteudo? (DIGITE O ID): "))
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()


        for disciplina in Curso().select_disciplina_curso(id_curso):
            print("ID: " + str(disciplina[0]) + " - " + str(disciplina[1]))
        
        try:
            id_disciplina = int(input("A qual disciplina deseja inserir o conteudo? (DIGITE O ID) "))
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()
        

        nome_conteudo = input("Digite o nome do conteudo: ")

        opcao = input('Deseja inserir o conteudo "' + nome_conteudo + '" à disciplina '+str(
            Disciplina().select_disciplina(id_disciplina)[0][1]).format(nome_conteudo)+'"? (S/N) ')

        if opcao == "S" or opcao == "s":
            print("Inserindo o conteudo {}...".format(nome_conteudo))
            Conteudo().insert_conteudo(nome_conteudo, id_disciplina)

            self.inserirDados()
            pass

        else:
            print("Conteudo não inserido!")
            self.inserirDados()
            pass
        pass
        
    def InserirQuestao(self):
        for curso in Curso().select_curso():
            print("ID: " + str(curso[0]) + " - " + str(curso[1]))
        try:
            id_curso = int(input("A qual curso deseja inserir as questões? (DIGITE O ID): "))
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()
        
        for disciplina in Curso().select_disciplina_curso(id_curso):
            print("ID: " + str(disciplina[0]) + " - " + str(disciplina[1]))
        try:
            id_disciplina = int(input("A qual disciplina deseja inserir as questões? (DIGITE O ID): "))
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()
        

        for conteudo in Conteudo().select_conteudo(id_disciplina):
            print("ID: " + str(conteudo[0]) + " - " + str(conteudo[1]))

        try:
            id_conteudo = int(input("A qual conteudo deseja inserir as questões? (DIGITE O ID): "))
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()

        print("Digite o diretório do arquivo que contém as questões:")
        arquivo = FileManager().read_file_to_string()
        questoes = question.QuestionList.list_question(arquivo)

        print("As seguintes questões foram encontradas:")
        print(questoes.to_string())

        
        opcao = input("Deseja inserir as questões? (S/N): ")
        if opcao == "S" or opcao == "s":
            print("Inserindo as questões...")
            Questao().insert_question_list(questoes,id_disciplina ,id_conteudo)
            self.inserirDados()
        else:
            print("Questões não inseridas!")
            self.inserirDados()
            pass
        pass

    def LinkarCursoDisciplina(self):

        for disciplina in Disciplina().select_disciplina():
            print("ID: " + str(disciplina[0]) + " - " + str(disciplina[1]))


        try:
            id_disciplina = int(input("Escolha qual disciplina deseja linkar ao curso: "))
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()


        for curso in Curso().select_curso():
            print("ID: " + str(curso[0]) + " - " + str(curso[1]))

        
        try:
            id_curso = int(input("A qual curso deseja linkar a disciplina?: "))
        except ValueError:
            print("Opcao invalida!")
            print('\n\n')
            self.inserirDados()

        

        opcao = input('Deseja linkar o conteudo a disciplina "'+
              str(Disciplina().select_disciplina(
                  id_disciplina)[0][1])+
                  '" ao curso "'+
                  str(Curso().select_curso(
                      id_curso)[0][1])+'"? (S/N):')
        

        if opcao == "S" or opcao == "s":
            Disciplina().insert_disciplina_curso(id_disciplina, id_curso)
        else:
            print("Disciplina não linkada!")
        pass

    def listarCursos(self):
        print("Os seguintes cursos foram encontrados:")
        for curso in Curso().select_curso():
            print("ID: " + str(curso[0]) + " - " + str(curso[1]))
        self.listarDados()
        pass

    def listarDisciplinas(self):
        for curso in Curso().select_curso():
            print("ID: " + str(curso[0]) + " - " + str(curso[1]))
        try:
            id_curso = int(input("Deseja ver as disciplinas de qual curso? (DIGITE O ID): "))
        except ValueError:
            print("Opcao invalida!")
            self.listarDados()
        
        print("As seguintes disciplinas foram encontradas:")
        for disciplina in Curso().select_disciplina_curso(id_curso):
            print("ID: " + str(disciplina[0]) + " - " + str(disciplina[1]))

        self.listarDados()

    def listarConteudos(self):
        for curso in Curso().select_curso():
            print("ID: " + str(curso[0]) + " - " + str(curso[1]))

        try:
            id_curso = int(input("Deseja ver os conteudos de qual curso? (DIGITE O ID): "))
        except ValueError:
            print("Opcao invalida!")
            self.listarDados()
        

        for disciplina in Curso().select_disciplina_curso(id_curso):
            print("ID: " + str(disciplina[0]) + " - " + str(disciplina[1]))

        try:
            id_disciplina = int(input("Deseja ver os conteudos de qual disciplina? (DIGITE O ID): "))
        except ValueError:
            print("Opcao invalida!")
            self.listarDados()
        
        print("Os seguintes conteudos foram encontrados:")
        for conteudo in Conteudo().select_conteudo(id_disciplina):
            print("ID: " + str(conteudo[0]) + " - " + str(conteudo[1]))

        self.listarDados()

        self.pagina_inicial()
        pass 



        

Main(debug= False)
def alterar_status():
    print("Qual aluno desja alterar o status? (DIGITE O ID: )")
    for aluno in Aluno().select_aluno():
        print("ID: " + str(aluno[0]) + " - " + str(aluno[1]))

    try:
        id_aluno = int(input())
    except ValueError:
        print("Opcao invalida!")

    print("Qual disciplina deseja alterar o status? (DIGITE O ID: )")

    for disciplina in Matricula().select_matricula_by_aluno(id_aluno):
        print("ID: " + str(Disciplina().select_disciplina(disciplina[0])[0][0]) + " - " + str(Disciplina().select_disciplina(disciplina[0])[0][1]))

    try:
        id_disciplina = int(input())
    except ValueError:
        print("Opcao invalida!")

    print("Qual o novo status? (APROVADO/REPROVADO/CURSANDO)")
        
    status = input()

    if status == "REPROVADO":
        quant = Matricula().select_quantidade_reprovados(id_disciplina, id_aluno)[0][0]
        if quant == None:
            quant = 1
            Matricula().set_quantidade_reprovados(quant, id_disciplina, id_aluno)
        else:
            quant = quant + 1
            Matricula().set_quantidade_reprovados(quant, id_disciplina, id_aluno)

    if status == "APROVADO":
        quant = Matricula().select_quantidade_reprovados(id_disciplina, id_aluno)[0][0]
        if quant == None:
            quant = 0
            Matricula().set_quantidade_reprovados(quant, id_disciplina, id_aluno)

    try:
        Matricula().insert_status(id_disciplina, id_aluno, status)
    except Exception as err:
        print(err)

def cadastrar_aluno():
    print("Digite o nome do aluno:")
    nome_aluno = input()
    print('Deseja inserir o aluno "{}"? (S/N)'.format(nome_aluno))
    opcao = input()
    if opcao == "S" or opcao == "s":
        print("Inserindo o aluno {}...".format(nome_aluno))
        Aluno().insert_aluno(nome_aluno)
    else:
        print("Aluno não inserido!")
        self.inserirDados()

def matricular_aluno():
    print("Qual aluno desja matricular? (DIGITE O ID: )")
    for aluno in Aluno().select_aluno():
        print("ID: " + str(aluno[0]) + " - " + str(aluno[1]))

    try:
        id_aluno = int(input())
    except ValueError:
        print("Opcao invalida!")
    
    print("Qual curso deseja matricular o aluno? (DIGITE O ID: )")

    for curso in Curso().select_curso():
        print("ID: " + str(curso[0]) + " - " + str(curso[1]))

    try:
        id_curso = int(input())
    except ValueError:
        print("Opcao invalida!")

    print('Deseja inserir a disciplina "'+ Aluno().select_aluno(id_aluno)[0][1]+'" no Curso "'+str(
            Curso().select_curso(id_curso)[0][1])+'" ? (S/N)')
    
    opcao = input()
    if opcao == "S" or opcao == "s":
        print("Matriculando o aluno...")
        Student().enroll_student(id_aluno, id_curso)
    else:
        print("Aluno não matriculado!")
        self.inserirDados()
        pass

def cadastrar_nota():
    print("Qual aluno desja cadastrar a nota? (DIGITE O ID: )")
    for aluno in Aluno().select_aluno():
        print("ID: " + str(aluno[0]) + " - " + str(aluno[1]))

    try:
        id_aluno = int(input())
    except ValueError:
        print("Opcao invalida!")

    
    print("O Aluno está matriculado nas seguintes disciplinas:")

    for disciplina in Matricula().select_matricula_by_aluno(id_aluno):
        print("ID: " + str(Disciplina().select_disciplina(disciplina[0])[0][0]) + " - " + str(Disciplina().select_disciplina(disciplina[0])[0][1]))

    try:
        id_disciplina = int(input("A qual disciplina deseja cadastrar a nota? (DIGITE O ID: )"))
    except ValueError:
        print("Opcao invalida!")

    print("A Nota é referente a qual conteudo? (DIGITE O ID: )")
    for conteudo in Conteudo().select_conteudo(id_disciplina):
        print("ID: " + str(conteudo[0]) + " - " + str(conteudo[1]))
    
    try:
        id_conteudo = int(input())
    except ValueError:
        print("Opcao invalida!")

    nota = input("Digite a nota do aluno: ")

    print("Confirma os seguintes dados? \n Aluno: "+str(Aluno().select_aluno(id_aluno)[0][1])+"\n Disciplina: "+str(Disciplina().select_disciplina(id_disciplina)[0][1])+"\n Conteudo: "+str(Conteudo().select_conteudo(id_conteudo)[0][1])+"\n Nota: "+str(nota)+"\n (S/N)")
    opcao = input()
    if opcao == "S" or opcao == "s":
        print("Cadastrando a nota...")
        Notas().insert_nota(id_aluno, id_disciplina, id_conteudo, nota)
    else:
        print("Nota não cadastrada!")
        self.inserirDados()
        pass

def listar_notas():
    print("Qual aluno desja listar as notas? (DIGITE O ID: )")
    for aluno in Aluno().select_aluno():
        print("ID: " + str(aluno[0]) + " - " + str(aluno[1]))

    try:
        id_aluno = int(input())
    except ValueError:
        print("Opcao invalida!")

    print("As notas do aluno são:")
    for nota in Notas().select_nota_by_aluno(id_aluno):
        print(
            "Disciplina: " + str(Disciplina().select_disciplina(nota[0])[0][1]) +
            "\nConteudo: " + str(Conteudo().select_conteudo(nota[0])[0][1]) +
            "\nNota: " + str(nota[1])+ "\n\n"
        )

    #self.listarDados()

def listar_aluno():
    print("Os seguintes alunos foram encontrados:")
    for aluno in Aluno().select_aluno():
        print("ID: " + str(aluno[0]) + " - " + str(aluno[1]))
    self.listarDados()
    pass

def listar_matricula():
    print("Deseja Listar as diciplinas matriculadas de qual aluno?")
    for aluno in Aluno().select_aluno():
        print("ID: " + str(aluno[0]) + " - " + str(aluno[1]))

    try:
        id_aluno = int(input("DIGITE O ID: "))
    except ValueError:
        print("Opcao invalida!")

    print("As matriculas do aluno são:")
    for matricula in Matricula().select_matricula_by_aluno(id_aluno):
        print(
            "Disciplina: " + str(Disciplina().select_disciplina(matricula[0])[0]) +
            "\nStatus: " + str(matricula[1]) +
            "\nQuantidade de vezes reprovado: " + str(matricula[2])+ "\n\n"
        )

    #self.listarDados()



#cadastrar_aluno()
#matricular_aluno()
alterar_status()
#cadastrar_nota()
#listar_matricula()

#Exam().generate_exam_by_aluno()



#listinha = Questao().select_questao_by_conteudo(1)
##print(listinha)
##for questao in listinha:
##    alter = questao[1].split(' -- ')
##    print(questao[0])
##    for i in range(len(alter)):
##        print(alter[i] + " - " + questao[2].split(' -- ')[i])
#
#questionário = []
#alters = []
#gab = []
#
#for questao in listinha:
#    alternativas = questao[1].split(' -- ')
#    # Formatar os dados no estilo desejado
#    enunciado = questao[0]
#    alternativas_formatadas = f"[{']['.join(alternativas)}]"
#    
#    # Obtém o gabarito no formato desejado
#    gabarito = [f"{i+1} - {letra}" for i, letra in enumerate('ABCDE') if "1" == questao[2].split(' -- ')[i]]
#    q = []
#    q.append(enunciado)
#    questionário.append(q)
#    alters.append(alternativas)
#    gab.append(gabarito)
#    #print(f"Enunciado: {enunciado}")
#    #print(f"Alternativas: {alternativas_formatadas}")
#    #print(f"Gabarito: {gabarito}\n")
#
##print(questionário)
##print(alters)
##print(gabarito)
#
#QrCode(gab).generate_qrcode().save("qrcode.png")
#Disc = Disciplina().select_disciplina(1)[0][1]
#
#print(len(questionário))
#
#prova = ParseLatex(questionário, alters, "Prova",  Disc, "ALUNO", "Julio Cesar", len(questionário))
#prova.generate_latex()
#prova.generate_pdf()
#

