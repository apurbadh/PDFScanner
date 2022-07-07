from .parser import PDFParser
from dotenv import dotenv_values
import os

CONFIG = dotenv_values(".env")
PATH = os.path.join(os.getcwd(), CONFIG["FOLDER_NAME"], CONFIG["FILE_NAME"])


def main():
    
    file = open(PATH, "rb")
    parser = PDFParser(file)
    parser.parse()





if __name__ == "__main__":
    main()