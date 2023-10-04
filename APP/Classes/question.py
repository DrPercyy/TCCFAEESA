from Classes import dataaccess

class Statement:
    def __init__(self, id, text):
        self.id = id
        self.text =  text

    def set_statement(id, text):
        id = id
        text = text
        return Statement(id, text) 
    
    def statement(self):
        return self.id, self.text
    
    def to_string(self):
        return f"'{self.text}'"


class QuestionList:
    def __init__(self, question_list):
        self.question_list = question_list
    
    @property
    def question_list(self):
        return self._question_list
    
    @question_list.setter
    def question_list(self, new_question_list):
        self._question_list = new_question_list

    def list_question(question_doc):
        question_list= []
        questions = question_doc.split("--")
        db = dataaccess.MySQLConnector()
        db.connect()

        id = db.next_id("QUESTAO")

        for question in questions:
           question_list.append(ParseQuestion.parse_multiple_choice_question(id, question))
           id = id + 1

        return QuestionList(question_list)
    


class ParseQuestion:
    def __init__(self, statement, options):
        self.statement = statement
        self.options = options
    
    @property
    def statement(self):
        return self._statement
    
    @statement.setter
    def statement(self, new_statement):
        self._statement = new_statement
    
    @property
    def options(self):
        return self._options
    
    @options.setter
    def options(self, new_options):
        self._options = new_options
    
    def get_question(self):
        return self.statement, self.options
    
    def parse_multiple_choice_question(id, question):
        lines = question.split("\n")
        while "" in lines:
            lines.remove("")

        correct_answer = lines[-1][-1].upper()
        lines[-1] = lines[-1][:-1]
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
        question_statement = Statement.set_statement(id, text_question)
        question_options = OptionList.list_options(question_statement.id, text_options, correct_answer)

        return ParseQuestion(question_statement, question_options)


class OptionList:
    def __init__(self, option_list):
        self._option_list = option_list
    
    @property
    def option_list(self):
        return self._option_list
    
    @option_list.setter
    def option_list(self, new_option_list):
        self._option_list = new_option_list
    
    def list_options(id, options, correct_answer):
        option_list = []
        db = dataaccess.MySQLConnector()
        db.connect()
        id_alt = db.next_id("ALTERNATIVA")
        for option in options:
            option_index = options.index(option)
            option_list.append(Options.set_options(id, option, option_index, correct_answer))
            id_alt = id_alt + 1
        return OptionList(option_list)
    

class Options:
    def __init__(self, fk, option_text, option_index, correct_answer):
        self.fk = fk
        self.option_text = option_text
        self.option_index = option_index
        self.correct_answer = correct_answer
    
    def set_options(fk, option_text, option_index, correct_answer):
        id = fk
        option_text = option_text
        if option_index == ord(correct_answer) - ord('A'):
            correct_answer = 1
            pass
        else:
            correct_answer = 0
            pass

        return Options(id, option_text, option_index, correct_answer)
    
    def get_options(self):
        return self.id, self.option_text, self.option_index, self.correct_answer
    
    def get_correct_answer(self):
        return self.correct_answer
    
    def get_option_text(self):
        return self.option_text
    
    def get_option_index(self):
        return self.option_index
    
    def get_id(self):
        return self.id
    
    def get_question_id(self):
        return self.question_id
    
    def to_string(self):
        return f"{self.fk} , '{self.option_text}', {self.correct_answer}"