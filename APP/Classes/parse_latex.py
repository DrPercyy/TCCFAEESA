#Arquivo direcionado a transformar as questões em uma prova fisica de multipla escolha
from pylatex import MiniPage, Document, Section, Subsection, Command, Figure, NoEscape, Package, Tabular, MultiColumn, MultiRow, LongTabu, Tabu, Center, FlushLeft, FlushRight, NewPage, NewLine, VerticalSpace, HorizontalSpace, LineBreak, TextColor
from pylatex.utils import italic, bold, NoEscape 
import qrcode


class ParseLatex:
    def __init__(self, questoes, gabarito, nome_prova, nome_disciplina, nome_professor, nome_aluno, numero_questoes):
        self.questoes = questoes
        self.gabarito = gabarito
        self.nome_prova = nome_prova
        self.nome_disciplina = nome_disciplina
        self.nome_professor = nome_professor
        self.nome_aluno = nome_aluno
        self.numero_questoes = numero_questoes
        self.document = Document(documentclass='exam', document_options=['addpoints', 'answers'])
        self.document.packages.append(Package('graphicx'))

    def generate_latex(self):
        self.document.append(Command('ID Prova: ', str(000)))
        self.generate_header()
        self.document.append(Command('centering'))
        self.document.append(Section("Gabarito", numbering=False))
        self.generate_gabarito()
        self.document.append(Section("Questionário", numbering=False))
        self.generate_questions()
        self.generate_footer()
        self.document.generate_tex(self.nome_prova)

    def generate_header(self):
        with self.document.create(Figure(position='htbp')) as logo_table:
            logo_table.append(Command('centering'))
            with logo_table.create(Tabular('p{5.5in}')) as table:
                table.add_row([bold(self.nome_prova + ' - ' + self.nome_disciplina)])
                table.add_hline()
                table.add_row([bold(self.nome_professor + ' - ' + self.nome_aluno)])
            with self.document.create(MiniPage(width=r'1\textwidth')) as qrcode:
                qrcode.append(Command('includegraphics[width=0.2\\textwidth]{qrcode.png}'))
                qrcode.append(Command('label{fig:qrcode}'))
                
            

    def generate_gabarito(self):
        with self.document.create(Tabular("|c|c|")) as table:
            table.add_hline()
            table.add_row(["Questão", "Resposta"])
            table.add_hline()

            for i in range(1, self.numero_questoes + 1):
                table.add_row([str(i), ""])
                table.add_hline()

    def generate_questions(self):
        self.document.append(Command('begin', 'questions'))
        for i in range(self.numero_questoes):
            self.document.append(Command('question', self.questoes[i]))
            self.document.append(Command('begin', 'choices'))
            for j in range(len(self.gabarito[i])):
                self.document.append(Command('choice', self.gabarito[i][j]))
            self.document.append(Command('end', 'choices'))
        self.document.append(Command('end', 'questions'))

    def generate_footer(self):
        self.document.append(Command('end', 'document'))


class QrCode:
    def __init__(self, data):
        self.data = data

    def generate_qrcode(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(self.data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        return img


questoes = [["Em programação, o que é um vetor?"],["O que é um loop em programação?"],["O que é um condicional em programação?"]]

gabarito = [
    [
        "Um tipo de dado usado apenas para armazenar números inteiros.",
        "Uma variável que só pode conter caracteres de texto.",
        "Uma estrutura de dados que armazena uma coleção de elementos do mesmo tipo.",
        "Uma função que calcula a média de um conjunto de números.",
        "Um operador matemático."
        ], 
    [
        "Uma instrução que realiza uma única ação e termina a execução.",
        "Uma estrutura de controle que permite repetir um bloco de código várias vezes.",
        "Um tipo de dado usado para armazenar números decimais.",
        "Uma função que encontra o valor máximo em uma lista.",
        "Um operador lógico."
        ], 
    [
        "Uma instrução que realiza uma única ação e termina a execução.",
        "Uma estrutura de controle que permite repetir um bloco de código várias vezes.",
        "Uma estrutura de controle que executa um bloco de código com base em uma condição.",
        "Uma função que calcula a raiz quadrada de um número.",
        "Um operador de comparação."
        ]]

nome_prova = 'Prova 1'

nome_disciplina = 'Matemática'

nome_professor = 'Professor'

nome_aluno = 'Aluno'

numero_questoes = 3

respostas = '''
                1 - C \n
                2 - B \n
                3 - C \n'''

QrCode(respostas).generate_qrcode().save('qrcode.png')

latex = ParseLatex(questoes, gabarito, nome_prova, nome_disciplina, nome_professor, nome_aluno, numero_questoes)
latex.generate_latex()

latex.document.generate_pdf('Prova 1', clean_tex=False)
