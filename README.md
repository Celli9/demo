# This is my first repository

Learning and practicing version control!

This is another sentence. 

Adding this content using the VS code text
editor (locally). 

## Setup
Clone the repo to download it from github. Perhaps onto the desktop.

Navigate to the repo from the command line.

```sh
cd ~/Users/alexanderbotticelli/Documents/GitHub/demo
```

## Usage

Example script
```sh
python app/my_script.py
```

Game of RPS
```sh
python app/rps.py

#alternative "modular style" command:
python -m app.rps
```

Testing:
```sh
pytest
```


Create virtual env:
```sh
conda create -n my-first-env-fall-2025 python=3.11
```
activate virtual env:
```sh
conda activate my-first-env-fall-2025
```
install package dependencies:

```sh
pip install -r requirements.txt
```

Stocks dashboard:

```sh
python -m app.stocks
```


## Configuration

Obtain a premium AlphaVantage API Key (using the form or from the prof) alphavantage.co/support/#api-key

Create a local ".env" file and store your api key as an environment variable in there:

```sh 
ALPHAVANTAGE_API_KEY = "________"

```

### Web App
```sh
# Mac OS #this flask app thing is an environment variable, so it goes in .env file:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```