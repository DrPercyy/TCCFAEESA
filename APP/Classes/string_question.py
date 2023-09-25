

class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file_to_string(self):
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                file_contents = file.read()
            return file_contents
        except FileNotFoundError:
            return f"O arquivo '{self.file_name}' não foi encontrado."
        except Exception as e:
            return f"Ocorreu um erro ao ler o arquivo: {str(e)}"



# Exemplo de uso:
if __name__ == "__main__":
    file_manager = FileManager("QUESTOES/Habilidades_estudo/Questoes_comunicacao.txt")

    # Lê o arquivo e gera uma string
    file_content = file_manager.read_file_to_string()
    print("Conteúdo do arquivo:")
    print(file_content)


