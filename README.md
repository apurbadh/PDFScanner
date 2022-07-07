# PDFScanner

### Requirements

First you need to install Python, you can go in <a href="https://www.python.org">Python</a> website to install python

<b>Note : </b> Tick the option to keep python in the environment variable if you are on windows

#### 1. Clone the repository
```
git clone https://github.com/apurbadh/PDFScanner
```

#### 2. Create a virtual environment (Optional)
```
python -m pip install virtalenv
virtualenv venv
```
<b>Windows</b>
```
./venv/Scripts/activate.ps1
```
<b>Linux / Mac</b>
```
source ./venv/bin/activate
```

#### 3. Specify the PDF file
```
cp .env.example .env
```
<b>Note : </b> Fill the given information in .env

#### 4. Install the required files
```
python -m pip install -r requirements.txt
```
<b>Note : </b> You might need <a href="https://www.java.com/en/">Java</a> for running this
#### 5. Run the python script
```
python main.py
```


### TLDR;
```
git clone https://github.com/apurbadh/PDFScanner
python -m pip install virtalenv
virtualenv venv
source ./venv/bin/activate
cp .env.example .env
python -m pip install -r requirements.txt
python main.py
```