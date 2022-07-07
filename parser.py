import sys
from tabula import read_pdf

class PDFParser:

    def __init__(self, file):

        try:
            open(file)
        except FileNotFoundError:
            print("Error: The file you provided doesn't exist")
            print("Please check the .env file and try again")
            sys.exit(-1)

        self.file = file
        self.dataframe = None
        

    def parse(self):
        data = read_pdf(self.file, pages="all")
        df = data[0]

        df = df[df[0].notna()]

        df = df.dropna(how="all")
        df = df.dropna(axis=1, how="all")

        df = df.fillna('')

        while "Unnamed: 0" in df.columns:
            df.columns = df.iloc[0]
            df = df.iloc[1:]

        df.reset_index(drop=True, inplace=True)

        self.dataframe = df

        return df


    def export_csv(self, filename):

        self.dataframe.to_csv(filename)


        