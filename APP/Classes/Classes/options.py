from Classes import dataacces

dbcon = ('localhost', 'TCCAPP', 'TCC01', 'tccapp')

class Options: 
    def __init__(self,id_alternativas, fk_question, option_text, correct_answer):
        self.id_alternativas = id_alternativas
        self.fk_question = fk_question
        self.option_text = option_text
        self.correct_answer = correct_answer
        
    def set_options(id_alternativas,id_question, option, option_index, correct_answer):
        id_alternativas = id_alternativas
        fk_question = id_question
        option_text = option
        if option_index == ord(correct_answer) - ord("A"):
            correct_answer = 1
            pass
        else:
            correct_answer = 0
            pass
        return Options(id_alternativas, fk_question, option_text, correct_answer)
    
    def get_options(self):
        return self.fk_question, self.option_text, self.correct_answer
    
    

class OptionList:
    def __init__(self, options_list):
        self._options_list = options_list

    @property
    def options_list(self):
        return self._options_list

    @options_list.setter
    def options_list(self, new_options_list):
        self._options_list = new_options_list

    def list_options(id_question, options, correct_answer, id_alt):

        options_list = []
        for option in options:
            option_index = options.index(option)
            options_list.append(Options.set_options(id_alt, id_question, option, option_index, correct_answer))
            id_alt =id_alt+ 1
        return OptionList(options_list)
        