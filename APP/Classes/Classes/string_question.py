class FileManager:
    def __init__(self, file_name = None):
        self.file_name = file_name

    def read_file_to_string(self):
        self.file_name = input()
        #self.file_name = "D:\Docs\TCC rev2\QUESTOES\Laboratorio de Programacao I\Questoes estruturas de repeticao.txt"
        
        
        
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                file_contents = file.read()
            return file_contents
        except FileNotFoundError:
            return f"O arquivo '{self.file_name}' não foi encontrado."
        except Exception as e:
            return f"Ocorreu um erro ao ler o arquivo: {str(e)}"





