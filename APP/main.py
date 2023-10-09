#classe princeipal que realiza a chamada dos métodos da classe DataAccess
from Classes.string_question import FileManager
import Classes.question as question
from Classes.dataoperation import Curso, Disciplina, Conteudo, Questao

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
        print("Digite o nome do curso:")
        nome_curso = input()
        print('Deseja inserir o curso "{}"? (S/N)'.format(nome_curso))
        opcao = input()
        if opcao == "S" or opcao == "s":
            print("Inserindo o curso {}...".format(nome_curso))
            Curso().insert_curso(nome_curso)
            self.inserirDados()
        else:
            print("Curso não inserido!")
            self.inserirDados()

    def inserirDisciplina(self):
        print("A qual curso deseja inserir a disciplina? (DIGITE O ID: )")
        for curso in Curso().select_curso():
            print("ID: " + str(curso[0]) + " - " + str(curso[1]))
        try:
            id_curso = int(input())
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()
        print("Digite o nome da disciplina:")
        nome_disciplina = input()
        print('Deseja inserir a disciplina "'+ nome_disciplina+'" no Curso "'+str(
            Curso().select_curso(id_curso)[0][1])+'" ? (S/N)')
        opcao = input()
        if opcao == "S" or opcao == "s":
            print("Inserindo a disciplina {}...".format(nome_disciplina))
            Disciplina().insert_disciplina(nome_disciplina, id_curso)
            self.inserirDados()
        else:
            print("Disciplina não inserida!")
            self.inserirDados()
    
    def inserirConteudo(self):

        print("A qual curso deseja inserir o conteudo? (DIGITE O ID: )")
        for curso in Curso().select_curso():
            print("ID: " + str(curso[0]) + " - " + str(curso[1]))
        try:
            id_curso = int(input())
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()

        print("A qual disciplina deseja inserir o conteudo? (DIGITE O ID: )")

        for disciplina in Curso().select_disciplina_curso(id_curso):
            print("ID: " + str(disciplina[0]) + " - " + str(disciplina[1]))
        
        try:
            id_disciplina = int(input())
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()
        

        print("Digite o nome do conteudo:")
        nome_conteudo = input()

        print('Deseja inserir o conteudo "' + nome_conteudo + '" à disciplina'+str(
            Disciplina().select_disciplina(id_disciplina)[0][1]).format(nome_conteudo)+'"? (S/N)')
        opcao = input()

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
        print("A qual curso deseja inserir as questões? (DIGITE O ID: )")
        for curso in Curso().select_curso():
            print("ID: " + str(curso[0]) + " - " + str(curso[1]))
        try:
            id_curso = int(input())
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()
        
        print("A qual disciplina deseja inserir as questões? (DIGITE O ID: )")
        for disciplina in Curso().select_disciplina_curso(id_curso):
            print("ID: " + str(disciplina[0]) + " - " + str(disciplina[1]))
        try:
            id_disciplina = int(input())
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()
        

        print("A qual conteudo deseja inserir as questões? (DIGITE O ID: )")

        for conteudo in Conteudo().select_conteudo(id_disciplina):
            print("ID: " + str(conteudo[0]) + " - " + str(conteudo[1]))

        try:
            id_conteudo = int(input())
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()

        print("Digite o diretório do arquivo que contém as questões:")
        arquivo = FileManager().read_file_to_string()
        questoes = question.QuestionList.list_question(arquivo)

        print("As seguintes questões foram encontradas:")
        print(questoes.to_string())

        print("Deseja inserir as questões? (S/N)")
        
        opcao = input()
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
        print ("Escolha qual disciplina deseja linkar ao curso:")

        for disciplina in Disciplina().select_disciplina():
            print("ID: " + str(disciplina[0]) + " - " + str(disciplina[1]))


        try:
            id_disciplina = int(input())
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()

        
        print("A qual curso deseja linkar a disciplina?")


        for curso in Curso().select_curso():
            print("ID: " + str(curso[0]) + " - " + str(curso[1]))

        
        try:
            id_curso = int(input())
        except ValueError:
            print("Opcao invalida!")
            print('\n\n')
            self.inserirDados()

        
        print('Deseja linkar o conteudo a disciplina "'+
              str(Disciplina().select_disciplina(
                  id_disciplina)[0][1])+
                  '" ao curso "'+
                  str(Curso().select_curso(
                      id_curso)[0][1])+'" ? (S/N)')
        

        opcao = input()
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
        print("Deseja ver as disciplinas de qual curso? (DIGITE O ID: )")
        for curso in Curso().select_curso():
            print("ID: " + str(curso[0]) + " - " + str(curso[1]))
        try:
            id_curso = int(input())
        except ValueError:
            print("Opcao invalida!")
            self.listarDados()
        
        print("As seguintes disciplinas foram encontradas:")
        for disciplina in Curso().select_disciplina_curso(id_curso):
            print("ID: " + str(disciplina[0]) + " - " + str(disciplina[1]))

        self.listarDados()

    def listarConteudos(self):
        print("Deseja ver os conteudos de qual curso? (DIGITE O ID: )")
        for curso in Curso().select_curso():
            print("ID: " + str(curso[0]) + " - " + str(curso[1]))

        try:
            id_curso = int(input())
        except ValueError:
            print("Opcao invalida!")
            self.listarDados()
        

        print("Deseja ver os conteudos de qual disciplina? (DIGITE O ID: )")
        for disciplina in Curso().select_disciplina_curso(id_curso):
            print("ID: " + str(disciplina[0]) + " - " + str(disciplina[1]))

        try:
            id_disciplina = int(input())
        except ValueError:
            print("Opcao invalida!")
            self.listarDados()
        
        print("Os seguintes conteudos foram encontrados:")
        for conteudo in Conteudo().select_conteudo(id_disciplina):
            print("ID: " + str(conteudo[0]) + " - " + str(conteudo[1]))

        self.listarDados()

        self.pagina_inicial()
        pass 



        

Main(debug= True)


texto = Questao().select_questao_by_disciplina(1)




print(texto[0][1].split('--')[2])



