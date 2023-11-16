#classe princeipal que realiza a chamada dos métodos da classe DataAccess
from Classes.string_question import FileManager
import Classes.question as question
from Classes.dataoperation import Curso, Disciplina, Conteudo, Questao, Aluno, Matricula, Notas, HistProva, Professor, Turma
from Classes.class_operation import Student
from Classes.parse_latex import ParseLatex, QrCode
import random
from datetime import datetime


class Main:

    def __init__(self, debug = False):
        if debug:
            print("Debug mode")
            pass

        else:

            self.idprofessor = None
            self.logado = False

            while True:
                if self.logado:
                    self.pagina_inicial()
                else:
                    self.loginProfessor()
    pass

    def pagina_inicial(self):
        print("Bem vindo ao TCCAPP! Professor: "+ str(Professor().select_professor(self.idprofessor)[0][1]))
        print("O que deseja fazer?")
        print("1 - inserir dados")
        print("2 - listar dados")
        print("3 - Gerar prova")
        print("9 - sair")
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
            self.gerar_prova_por_aluno()
        elif opcao == 9:
            exit()
        else:
            print("Opcao invalida!")
            self.pagina_inicial()

    def inserirDados(self):
        print("O que deseja Inserir?")
        print("1 - Inserir curso")
        print("2 - Inserir disciplina")
        print("3 - Inserir conteudo")
        print("4 - Linkar Curso a Disciplina")
        print("5 - Inserir questao")
        print("6 - Cadastrar aluno")
        print("7 - Matricular aluno")
        print("8 - Próxima página")
        print("9 - Voltar")

        try:
            opcao = int(input("Digite a opcao:"))
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
            self.cadastrar_aluno()
        elif opcao == 7:
            self.matricular_aluno()
        elif opcao == 8:
            self.inserirDados2()
        elif opcao == 9:
            self.pagina_inicial()
        else:   
            print("Opcao invalida!")
            self.inserirDados()
    
    def inserirDados2(self):
        print("O que deseja Inserir?")
        print("1 - Cadastrar nota")
        print("2 - Alterar status")
        print("3 - Cadastrar professor")
        print("4 - Cadastrar turma")
        print("5 - Registrar nota")
        print("6 - Alterar Status")
        print("7 - Adicionar aluno a uma turma")
        print("9 - Voltar")
        try:
            opcao = int(input("Digite a opcao:"))
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()
        if opcao == 1:
            self.cadastrar_nota()
        elif opcao == 2:
            self.alterar_status()
        elif opcao == 3:
            self.cadastrar_professor()
        elif opcao == 4:
            self.cadastrar_turma()
        elif opcao == 5:
            self.cadastrar_nota()
        elif opcao == 6:
            self.alterar_status()
        elif opcao == 7:
            self.matricular_aluno_turma()
        elif opcao == 9:
            self.pagina_inicial()

    def listarDados(self):
        print("1 - Listar cursos")
        print("2 - Listar disciplinas")
        print("3 - Listar conteudos")
        print("4 - Listar alunos")
        print("5 - Listar matriculas")
        print("6 - Listar notas")
        print("9 - Voltar")

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
            self.listar_aluno()
        elif opcao == 5:
            self.listar_matricula()
        elif opcao == 6:
            self.listar_notas()
        elif opcao == 9:
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
        print("Deseja inserir questões de qual curso?")
        for curso in Curso().select_curso():
            print("ID: " + str(curso[0]) + " - " + str(curso[1]))
        try:
            id_curso = int(input("DIGITE O ID: "))
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()
        
        print("Deseja inserir questões de qual disciplina?")
        for disciplina in Curso().select_disciplina_curso(id_curso):
            print("ID: " + str(disciplina[0]) + " - " + str(disciplina[1]))
        try:
            id_disciplina = int(input("DIGITE O ID: "))
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()
        
        print("Deseja inserir questões de qual conteudo?")
        for conteudo in Conteudo().select_conteudo(id_disciplina):
            print("ID: " + str(conteudo[0]) + " - " + str(conteudo[1]))

        try:
            id_conteudo = int(input("DIGITE O ID: "))
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

        print("Deseja linkar qual disciplina?")
        for disciplina in Disciplina().select_disciplina():
            print("ID: " + str(disciplina[0]) + " - " + str(disciplina[1]))


        try:
            id_disciplina = int(input("Digite o ID"))
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()

        print("Deseja linkar a disciplina a qual curso?")
        for curso in Curso().select_curso():
            print("ID: " + str(curso[0]) + " - " + str(curso[1]))

        
        try:
            id_curso = int(input("Digite o ID"))
        except ValueError:
            print("Opcao invalida!")
            print('\n\n')
            self.inserirDados()

        

        opcao = input('Deseja linkar a disciplina "'+
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

    def alterar_status(self):
        print("Qual aluno desja alterar o status? (DIGITE O ID: )")
        for aluno in Aluno().select_aluno():
            print("ID: " + str(aluno[0]) + " - " + str(aluno[1]))

        try:
            id_aluno = int(input())
        except ValueError:
            print("Opcao invalida!")

        print("Qual disciplina deseja alterar o status? (DIGITE O ID: )")

        for disciplina in Matricula().select_matricula_by_aluno(id_aluno):
            print("ID: " + str(Disciplina().select_disciplina(disciplina[3])[0][0]) + " - " + str(Disciplina().select_disciplina(disciplina[3])[0][1]))

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

    def cadastrar_aluno(self):
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

    def matricular_aluno(self):
        print("Qual aluno desja matricular? (DIGITE O ID: )")
        for aluno in Aluno().select_aluno():
            print("ID: " + str(aluno[0]) + " - " + str(aluno[1]))

        try:
            id_aluno = int(input())
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()
        
        print("Qual curso deseja matricular o aluno? (DIGITE O ID: )")

        for curso in Curso().select_curso():
            print("ID: " + str(curso[0]) + " - " + str(curso[1]))

        try:
            id_curso = int(input())
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()

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

    def cadastrar_nota(self):
        print("Qual aluno desja cadastrar a nota? (DIGITE O ID: )")
        for aluno in Aluno().select_aluno():
            print("ID: " + str(aluno[0]) + " - " + str(aluno[1]))

        try:
            id_aluno = int(input())
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()

        
        print("O Aluno está matriculado nas seguintes disciplinas:")

        for disciplina in Matricula().select_matricula_by_aluno(id_aluno):
            print("ID: " + str(Disciplina().select_disciplina(disciplina[3])[0][0]) + " - " + str(Disciplina().select_disciplina(disciplina[3])[0][1]))

        try:
            id_disciplina = int(input("A qual disciplina deseja cadastrar a nota? (DIGITE O ID: )"))
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()

        print("A Nota é referente a qual conteudo? (DIGITE O ID: )")
        for conteudo in Conteudo().select_conteudo(id_disciplina):
            print("ID: " + str(conteudo[0]) + " - " + str(conteudo[1]))
        
        try:
            id_conteudo = int(input())
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()

        nota = input("Digite a nota do aluno: ")

        print("Confirma os seguintes dados? \n Aluno: "+str(Aluno().select_aluno(id_aluno)[0][1])+"\n Disciplina: "+str(Disciplina().select_disciplina(id_disciplina)[0][1])+"\n Conteudo: "+str(Conteudo().select_conteudo_by_id(id_conteudo)[0][1])+"\n Nota: "+str(nota)+"\n (S/N)")
        opcao = input()
        if opcao == "S" or opcao == "s":
            print("Cadastrando a nota...")
            Notas().insert_nota(id_aluno, id_disciplina, id_conteudo, nota)
        else:
            print("Nota não cadastrada!")
            self.inserirDados()
            pass

    def listar_notas(self):
        print("Qual aluno desja listar as notas? (DIGITE O ID: )")
        for aluno in Aluno().select_aluno():
            print("ID: " + str(aluno[0]) + " - " + str(aluno[1]))

        try:
            id_aluno = int(input())
        except ValueError:
            print("Opcao invalida!")
            self.listarDados

        print("As notas do aluno são:")
        for nota in Notas().select_nota_by_aluno(id_aluno):
            print(
                "Disciplina: " + str(Disciplina().select_disciplina(nota[0])[0][1]) +
                "\nConteudo: " + str(Conteudo().select_conteudo(nota[0])[0][1]) +
                "\nNota: " + str(nota[1])+ "\n\n"
            )

        #self.listarDados()

    def listar_aluno(self):
        print("Os seguintes alunos foram encontrados:")
        for aluno in Aluno().select_aluno():
            print("ID: " + str(aluno[0]) + " - " + str(aluno[1]))
        self.listarDados()
        pass

    def listar_matricula(self):
        print("Deseja Listar as diciplinas matriculadas de qual aluno?")
        for aluno in Aluno().select_aluno():
            print("ID: " + str(aluno[0]) + " - " + str(aluno[1]))

        try:
            id_aluno = int(input("DIGITE O ID: "))
        except ValueError:
            print("Opcao invalida!")
            self.listarDados()

        print("As matriculas do aluno são:")
        for matricula in Matricula().select_matricula_by_aluno(id_aluno):
            print(
                "Disciplina: " + str(Disciplina().select_disciplina(matricula[0])[0][1]) +
                "\nStatus: " + str(matricula[1]) +
                "\nQuantidade de vezes reprovado: " + str(matricula[2])+ "\n\n"
            )

        #self.listarDados()

    def cadastrar_professor(self):
        nome_professor = input("Digite o nome do professor: ")
        login =  input("Digite o nome de usuário do professor: ")
        print("Confirma os seguintes dados? \n Nome: "+str(nome_professor)+"\n Login: "+str(login))
        opcao = input("(S/N): ")
        if opcao == "S" or opcao == "s":
            senha = input("Digite a senha do professor: ")
            print("Cadastrando o professor...")
            Professor().insert_professor(nome_professor, login, senha)
        else:
            print("Professor não cadastrado!")
            self.inserirDados()
            pass

    def cadastrar_turma(self):
        print("Deseja inserir uma turma em qual curso?")
        for curso in Curso().select_curso():
            print("ID: " + str(curso[0]) + " - " + str(curso[1]))
        try:
            id_curso = int(input("DIGITE O ID: "))
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()
        
        print("Qual deverá ser a matéria da turma?")
        for disciplina in Curso().select_disciplina_curso(id_curso):
            print("ID: " + str(disciplina[0]) + " - " + str(disciplina[1]))
        try:
            id_disciplina = int(input("DIGITE O ID: "))
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()

        print("Qual professor será responsável pela turma?")
        for professor in Professor().select_professor():
            print("ID: " + str(professor[0]) + " - " + str(professor[1]))
        try:
            id_professor = int(input("DIGITE O ID: "))
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()
        

        

        nome_turma = input("Digite o nome da turma: ")
        opcao = input('Deseja inserir a turma "'+ nome_turma+'" ao Curso "'+str(
            Curso().select_curso(id_curso)[0][1])+'"? (S/N): ')
        if opcao == "S" or opcao == "s":
            print("Inserindo a turma {}...".format(nome_turma))
            Turma().insert_turma(nome_turma,  id_professor, id_disciplina)
            self.inserirDados()
        else:
            print("Turma não inserida!")
            self.inserirDados()
            pass
        pass

    def selecionar_elementos_aleatorios(self, lista, num_elementos):
       # Embaralhe a lista original
        random.shuffle(lista)
        
        tuplas_selecionadas = set()
        
        for elemento in lista:
            # Itera sobre os elementos embaralhados
            for tupla in elemento:
                # Itera sobre as tuplas no elemento atual
                tuplas_selecionadas.add(tupla)  # Adiciona a tupla à lista selecionada
                if len(tuplas_selecionadas) >= num_elementos:
                    return tuplas_selecionadas  # Retorna a lista quando o número desejado é alcançado
        # Se o número desejado não for alcançado durante a iteração, retornar o que foi possível coletar
        return tuplas_selecionadas
    
    def gerar_prova_por_aluno(self):
        print("Quando a prova será aplicada?")
        date = input("dd/mm/aaaa: ")
        date_format = datetime.strptime(date, "%d/%m/%Y")
        matriz_prova = []
        lista_questoes = []

        print("Deseja Gerar uma prova para qual aluno?")
        for aluno in Aluno().select_aluno():
            print("ID: " + str(aluno[0]) + " - " + str(aluno[1]))
        
        try:
            id_aluno = int(input("DIGITE O ID: "))
        except ValueError:
            print("Opcao invalida!")
        
        for cont in Conteudo().select_conteudo_cursado(id_aluno):
            lista_questoes = Questao().select_questao_by_conteudo(cont[0])
            matriz_prova.append(lista_questoes)

        #for mat in Matricula().select_matricula_by_aluno(id_aluno):
        #    for disc in Disciplina().select_disciplina(mat[3]):
        #        for cont in Conteudo().select_conteudo(disc[0]):
        #            lista_questoes = Questao().select_questao_by_conteudo(cont[0])
        #            matriz_prova.append(lista_questoes)

        lista_prova = self.selecionar_elementos_aleatorios(matriz_prova, 10)
        questionário = []
        alters = []
        gab = []
        gabcod = ""

        for questao in lista_prova:
            alternativas = questao[1].split(' -- ')
            # Formatar os dados no estilo desejado
            enunciado = questao[0]
            alternativas_formatadas = f"[{']['.join(alternativas)}]"
            
            # Obtém o gabarito no formato desejado
            gabarito = [f"{i+1} - {letra}" for i, letra in enumerate("ABCDE") if "1" == questao[2].split(' -- ')[i]]
            q = []
            q.append(enunciado)
            questionário.append(q)
            alters.append(alternativas)
            gab.append(gabarito[0])
            gabcod = gabcod + gabarito[0] +" -- "
    

        QrCode("FUTURO METODO DE CORREÇÂO AUTOMATICA").generate_qrcode().save("qrcode.png")
        Disc = "Prova integrada"

        print(len(questionário))

        HistProva().insert_historico(gabcod, date_format, id_aluno)
        nome_prova = str(HistProva().select_last_id()[0][0]) + "-" + str(date_format.strftime("%d%m%Y"))
        prova = ParseLatex(questionário, alters, nome_prova,  Disc, "Data : " + date, "Aluno: "+ Aluno().select_aluno(id_aluno)[0][1], len(questionário))
        prova.generate_latex()
        try:
            prova.generate_pdf()
        except Exception as err:
            self.pagina_inicial()
            pass

    def gerar_prova_por_turma(self):
        print("Quando a prova será aplicada?")
        date = input("dd/mm/aaaa: ")
        date_format = datetime.strptime(date, "%d/%m/%Y")
        matriz_prova = []
        lista_questoes = []

        print("Deseja Gerar uma prova para qual turma?")
        for turma in Turma().select_turma_by_professor(int(self.idprofessor)):
            print("ID: " + str(turma[0]) + " - " + str(turma[1]))

        try:
            id_turma = int(input("DIGITE O ID: "))
        except ValueError:
            print("Opcao invalida!")

        for matricula in Turma().select_matricula_by_turma(id_turma):
            for id_aluno in Aluno().select_aluno(matricula[4]):
                for cont in Conteudo().select_conteudo_cursado(id_aluno[0]):
                    lista_questoes = Questao().select_questao_by_conteudo(cont[0])
                    matriz_prova.append(lista_questoes)

                #for mat in Matricula().select_matricula_by_aluno(id_aluno):
                #    for disc in Disciplina().select_disciplina(mat[3]):
                #        for cont in Conteudo().select_conteudo(disc[0]):
                #            lista_questoes = Questao().select_questao_by_conteudo(cont[0])
                #            matriz_prova.append(lista_questoes)

                lista_prova = self.selecionar_elementos_aleatorios(matriz_prova, 10)
                questionário = []
                alters = []
                gab = []
                gabcod = ""

                for questao in lista_prova:
                    alternativas = questao[1].split(' -- ')
                    # Formatar os dados no estilo desejado
                    enunciado = questao[0]
                    alternativas_formatadas = f"[{']['.join(alternativas)}]"
                    
                    # Obtém o gabarito no formato desejado
                    gabarito = [f"{i+1} - {letra}" for i, letra in enumerate("ABCDE") if "1" == questao[2].split(' -- ')[i]]
                    q = []
                    q.append(enunciado)
                    questionário.append(q)
                    alters.append(alternativas)
                    gab.append(gabarito[0])
                    gabcod = gabcod + gabarito[0] +" -- "
            

                QrCode(gab).generate_qrcode().save("qrcode.png")
                Disc = "Prova integrada"

                print(len(questionário))

                HistProva().insert_historico(gabcod, date_format, id_aluno)
                nome_prova = str(HistProva().select_last_id()[0][0]) + "-" + str(date_format.strftime("%d%m%Y"))
                prova = ParseLatex(questionário, alters, nome_prova,  Disc, "Data : " + date, "Aluno: "+ Aluno().select_aluno(id_aluno)[1], len(questionário))
                prova.generate_latex()
                try:
                    prova.generate_pdf()
                    self.pagina_inicial()
                except Exception as err:
                    self.pagina_inicial()
                    pass

        


    def matricular_aluno_turma(self):
        print("Qual aluno desja matricular?")
        for aluno in Aluno().select_aluno():
            print("ID: " + str(aluno[0]) + " - " + str(aluno[1]))

        try:
            id_aluno = int(input("DIGITE O ID: "))
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()
        
        print("Qual será disciplina?")
        for matricula in Matricula().select_matricula_by_aluno(id_aluno):
            print("ID: " + str(matricula[0]) + " - " + str(Disciplina().select_disciplina(matricula[3])[0][1]))

        try:
            matricula = int(input("DIGITE O ID: "))
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()
        
        print ("Qual turma?")
        id_disciplina = Matricula().select_matricula(matricula)[0][3]
        for turma in Turma().select_turma_by_disciplina(id_disciplina):
            print("ID: " + str(turma[0]) + " - " + str(turma[1]))

        try:
            id_turma = int(input("DIGITE O ID: "))
        except ValueError:
            print("Opcao invalida!")
            self.inserirDados()
        
        print("Confirma os seguintes dados? ")
        print("Aluno: "+str(Aluno().select_aluno(id_aluno)[0][1])+"\n"
              "Disciplina: "+str(Disciplina().select_disciplina(id_disciplina)[0][1])+"\n"
              "Turma: "+str(Turma().select_turma(id_turma)[0][1])+"\n")
        opcao = input("(S/N): ")
        if opcao == "S" or opcao == "s":
            print("Matriculando o aluno...")
            Matricula().insert_status(id_disciplina, id_aluno, "CURSANDO")
            Turma().insert_aluno_turma(matricula, id_turma)
            self.inserirDados()
        else:
            print("Aluno não matriculado!")
            self.inserirDados()
            pass

    def loginProfessor(self):
        print("Digite seu login: ")
        login = input()
        print("Digite sua senha: ")
        senha = input()
        
        try:
            usuario = Professor().select_professor_by_login(login)
        except Exception as err:
            print(err)

        if usuario == []:
            print("Login ou senha incorretos!")
            self.loginProfessor()

        elif usuario[0][3] == senha:
            print("Login realizado com sucesso!")
            self.idprofessor = Professor().select_professor_by_login(login)[0][0]
            self.logado = True
            self.pagina_inicial()


        else:
            print("Login ou senha incorretos!")
            self.loginProfessor()
        
        

Main(debug= False)


