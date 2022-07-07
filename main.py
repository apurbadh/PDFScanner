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

    parser = PDFParser(PATH)
    parser.parse()
    parser.export_csv("test.csv")



if __name__ == "__main__":
    main()