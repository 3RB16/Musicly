# Musicly

a collaborative music playing app in which we will integrate our application with the third party Spotify API. 

## Installation

install Python 

```bash
  For windows - Download latest version from the official website: 
        https://www.python.org/downloads/
```
    
## Run Locally

Clone Musicly

```bash
  git clone https://github.com/3RB16/Musicly.git
```

Go to the project directory

```bash
  cd Musicly
```
install Virtual Enviorentment

```bash
  python -m venv env
```

Acitve Virtual Enviorentment

```bash
  env/Scripts/activate
```

Install poetry

```bash
  python -m pip install poetry
```

Install dependencies

```bash
  poetry install
```

Start the server

```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
```
