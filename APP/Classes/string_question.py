class FileManager:
    """
    A class for managing files.

    Attributes:
    file_name (str): The name of the file to be managed.

    Methods:
    read_file_to_string(): Reads the contents of a file and returns it as a string.
    """
    def __init__(self, file_name = None):
        self.file_name = file_name

    def read_file_to_string(self):
        """
        Reads the contents of a file and returns it as a string.

        Returns:
        str: The contents of the file as a string.

        Raises:
        FileNotFoundError: If the file specified by file_name is not found.
        Exception: If an error occurs while reading the file.
        """

        print("Digite o nome do arquivo que contém as questões:")
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


