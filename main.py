import os
import sys
from parser import PDFParser
from dotenv import dotenv_values

CONFIG = dotenv_values(".env")

try:
    PATH = os.path.join(os.getcwd(), CONFIG["FOLDER_NAME"], CONFIG["FILE_NAME"])

except KeyError:
    print("Error: The values in .env doesn't exist")
    print("Please create the .env file or fill 'FILE_NAME' and 'FOLDER_NAME' for location in it")
    sys.exit(-1)



def main():
    file = open(PATH, "rb")

    try:
        file = open(PATH, "rb")

    except FileNotFoundError:
        print("Error: The file doesn't exist in the given folder")
        print("Please change the .env and try again")
        sys.exit(-1)

    parser = PDFParser(file)
    parser.parse()
    parser.printData()





if __name__ == "__main__":
    main()