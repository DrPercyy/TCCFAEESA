from Classes import question

question_string = "Qual é a\ncapital da França?\nA) Londres\nB) Berlim\nC) Paris\nD) Madri\nResposta: C\n--\n\n\nQual é a principal diferença entre um algoritmo e um programa de computador?\nA) Algoritmos só podem ser escritos em pseudocódigo.\nB) Programas de computador não são usados na resolução de problemas.\nC) Algoritmos são sempre mais eficientes que programas.\nD) Algoritmos são abstrações de alto nível, enquanto programas são implementações concretas.\nResposta: d\n--\nA capital da França é Paris\nA) Verdadeiro\nB) Falseo\nResposta: A"

question_list = question.OptionList.list_question(question_string)



#question = question.parse_multiple_choice_question(question_string)

print("\n\n")

for i in range(len(question_list.question_list)):
    print("Id: ",question_list.question_list[i].text.id, "Questão:", question_list.question_list[i].text.statement)
    for j in range(len(question_list.question_list[i].options.options_list)):
        print("FK:",question_list.question_list[i].options.options_list[j].fk_question, " Opção",j+1,": "  ,question_list.question_list[i].options.options_list[j].option_text, " Verdadeira?: ",question_list.question_list[i].options.options_list[j].correct_answer)
        pass
    print("\n\n")



