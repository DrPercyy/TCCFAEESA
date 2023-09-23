from Classes import statement
from Classes import options
from Classes import dataacces

dbcon= ('localhost', 'root', 'tcc01', 'tccapp')
class Question:

  def __init__(self, text, options):
    self.text = text
    self.options = options

def parse_multiple_choice_question(id, question, id_alt):
    lines = question.split('\n')
    while lines[0] == '' or lines [-1] == '':
      if lines[-1] == '':
        lines.pop()
      if lines[0] == '':
        lines.pop(0)
    # Combine todas as linhas até a última que começa com um caractere diferente de letra maiúscula seguido de parênteses e espaço
    correct_answer = lines[-1][-1].upper()
    lines.pop()
    text_lines = []
    options_lines = []
    for line in lines:
        if not line[0].isupper() or not line[1:3] == ') ':
            text_lines.append(line)
        else:
            options_lines.append(line[3:])
    
    text_question = '\n'.join(text_lines)
    text_options = options_lines
    question_statement = statement.Statement.set_statement(id, text_question)
    question_options = options.OptionList.list_options(question_statement.id, text_options, correct_answer, id_alt)
      
    return Question(question_statement, question_options)

def get_question(self):
    return self.text, self.options

class OptionList:
    def __init__(self, question_list):
        self._question_list = question_list

    @property
    def question_list(self):
        return self._question_list

    @question_list.setter
    def question_list(self, new_question_list):
        self._question_list = new_question_list

    def list_question(question_doc):
        question_list= []
        questions = question_doc.split("--")
        db = dataacces.MySQLConnector(dbcon[0], dbcon[1], dbcon[2], dbcon[3])
        db.connect()
        idreturn = db.execute_query("SHOW TABLE STATUS LIKE 'QUESTAO'")
        id_alt = db.execute_count("SELECT *FROM alternativas;")
        id_alt =id_alt+ 1
        id = idreturn[0][10]
        for question in questions:
           question_list.append(parse_multiple_choice_question(id, question, id_alt))
           id = id + 1

        return OptionList(question_list)
    
    def to_string(self):
        for i in range(len(self.question_list)):
            print("Id: ",self.question_list[i].text.id, "Questão:", self.question_list[i].text.statement)
            for j in range(len(self.question_list[i].options.options_list)):
                print("ID: ",self.question_list[i].options.options_list[j].id_alternativas ,"FK:",self.question_list[i].options.options_list[j].fk_question, self.question_list[i].options.options_list[j].option_text ,self.question_list[i].options.options_list[j].correct_answer)
                pass
            print("\n\n")
        pass