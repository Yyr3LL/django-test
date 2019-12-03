# Django project for university

### To run this project on your machine

Create virtual environment

    py -m venv env

Activate it 	

    source env/bin/activate 

Install dependencies

    pip install -r requirements.txt

Go to the project dir, make migrations and run the server

    cd lab/
    py manage.py makemigrations
    py manage.py migrate
    py manage.py runserver


