from Classes import question, dataacces

dbcon = ('localhost', 'TCCAPP', 'TCC01', 'tccapp')

#db = dataacces.MySQLConnector(dbcon[0], dbcon[1], dbcon[2], dbcon[3])
#db.connect()

#print(db.execute_query("SELECT * FROM alternativas"))

#db = dataacces.MySQLConnector(dbcon[0], dbcon[1], dbcon[2], dbcon[3])
#db.connect()
#id = db.execute_query("select TEXTO_QUESTAO, ALTER_TEXTO from QUESTAO inner join alternativas on questao.ID_QUESTAO = ALTERNATIVAS.QUESTAO_ID_QUESTAO;")
#print(id[(0)][0])
#print(id[(0)][1])
#print(id[(1)][1])

question_string = "Qual é a\ncapital da França?\nA) Londres\nB) Berlim\nC) Paris\nD) Madri\nResposta: C\n--\n\n\nQual é a principal diferença entre um algoritmo e um programa de computador?\nA) Algoritmos só podem ser escritos em pseudocódigo.\nB) Programas de computador não são usados na resolução de problemas.\nC) Algoritmos são sempre mais eficientes que programas.\nD) Algoritmos são abstrações de alto nível, enquanto programas são implementações concretas.\nResposta: d"

question_list = question.OptionList.list_question(question_string)

questões = question_list.to_string()

#for i in range(len(question_list.question_list)):
#    print("Id: ",question_list.question_list[i].text.id, "Questão:", question_list.question_list[i].text.statement)
#    for j in range(len(question_list.question_list[i].options.options_list)):
#        print("FK:",question_list.question_list[i].options.options_list[j].fk_question, question_list.question_list[i].options.options_list[j].option_text ,question_list.question_list[i].options.options_list[j].correct_answer,")")
#        pass
#    print("\n\n")



