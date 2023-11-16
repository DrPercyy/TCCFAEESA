#Arquivo direcionado a transformar as questões em uma prova fisica de multipla escolha
from pylatex import MiniPage, Document, Section, Command, Figure , Package, Tabular
from pylatex.utils import italic, bold
import qrcode


class ParseLatex:
    def __init__(self, questoes, gabarito, nome_prova, nome_disciplina, data_prova, nome_aluno, numero_questoes):
        self.questoes = questoes
        self.gabarito = gabarito
        self.nome_prova = nome_prova
        self.nome_disciplina = nome_disciplina
        self.data_prova = data_prova
        self.nome_aluno = nome_aluno
        self.numero_questoes = numero_questoes
        self.document = Document(documentclass='exam', document_options=['addpoints', 'answers'])
        self.document.packages.append(Package('graphicx'))

    def generate_latex(self):
        self.document.append(Command('ID Prova: ', str(000)))
        self.generate_header()
        self.document.append(Command('centering'))
        self.document.append(Section("Questionário", numbering=False))
        self.generate_questions()
        self.document.append(Section("Gabarito", numbering=False))
        self.generate_gabarito()
        self.generate_footer()
        self.document.generate_tex(self.nome_prova)

    def generate_header(self):
        with self.document.create(Figure(position='htbp')) as logo_table:
            logo_table.append(Command('centering'))
            with logo_table.create(Tabular('p{5.5in}')) as table:
                table.add_row([bold(self.nome_aluno + ' - ' + self.data_prova)])
                table.add_hline()
                table.add_row([bold(self.nome_prova + ' - ' + self.nome_disciplina)])
            with self.document.create(MiniPage(width=r'1\textwidth')) as qrcode:
                qrcode.append(Command('includegraphics[width=0.2\\textwidth]{qrcode.png}'))
                qrcode.append(Command('label{fig:qrcode}'))
                
    def generate_gabarito(self):
        
            for j in range(self.numero_questoes):
                if j == 0 or j % 5 == 0 :
                    with self.document.create(Tabular("|c|c|")) as table:
                        table.add_hline()
                        table.add_row(["Questão", "Resposta"])
                        table.add_hline()
                table.add_row([str(j + 1), ""])
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

    def generate_pdf(self):
        self.document.generate_pdf(self.nome_prova+".tex", clean_tex=False, compiler='pdflatex')


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


