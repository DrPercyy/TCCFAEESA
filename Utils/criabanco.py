from APP.Classes.string_question import FileManager
import APP.Classes.question as question
from APP.Classes.dataoperation import Curso, Disciplina, Conteudo, Questao, Aluno, Matricula, Notas
from APP.Classes.student import Student

print("Criando banco de dados...")
Curso().insert_curso("Ciência da Computação")#!
Curso().insert_curso("Engenharia de Software")#2
Curso().insert_curso("Sistemas de Informação")#3


Disciplina().insert_disciplina("Laboratório de Programação 1", 1)#1
Disciplina().insert_disciplina("Habilidades de Estudo e Comunicação", 1)#2
Disciplina().insert_disciplina("Modelos Lógicos Computacionais", 1)#3
Disciplina().insert_disciplina("Sistemas de Informação Organizacionais", 1)#4
Disciplina().insert_disciplina("Universo Computacional", 1)#5

Conteudo().insert_conteudo("Arranjos", 1)#1
Conteudo().insert_conteudo("Estruturas de Repetição", 1)#2
Conteudo().insert_conteudo("Estruturas de Seleção", 1)#3
Conteudo().insert_conteudo("Introdução a Linguagem Python", 1)#4
Conteudo().insert_conteudo("Introdução ao Algoritmo", 1)#5

Conteudo().insert_conteudo("Comunicação", 2)#6
Conteudo().insert_conteudo("Escrita Ciêntifica, Técnica e Profissional", 2)#7
Conteudo().insert_conteudo("Pesquisas Academicas", 2)#8
Conteudo().insert_conteudo("Técnicas de Estudo", 2)#9

Conteudo().insert_conteudo("Conectivos Lógicos", 3)#10
Conteudo().insert_conteudo("Equivalencias Tautológicas", 3)#11
Conteudo().insert_conteudo("Lógica", 3)#12
Conteudo().insert_conteudo("Tabela Verdade", 3)#13

Conteudo().insert_conteudo("Conceitos de Informação e Sistemas", 4)#14
Conteudo().insert_conteudo("Conceitos de Tecnologia da Informação", 4)#15
Conteudo().insert_conteudo("Sistemas de Informação de Negócio", 4)#16
Conteudo().insert_conteudo("Sistemas de Informação nas Organizaçôes", 4)#17

Conteudo().insert_conteudo("Armazenamento de Dados", 5)#18
Conteudo().insert_conteudo("Etica na Computação", 5)#19
Conteudo().insert_conteudo("Imersão no Universo computacional", 5)#20
Conteudo().insert_conteudo("Manipulação de Dados", 5)#21


print("FIM")