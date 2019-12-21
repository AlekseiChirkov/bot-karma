# Project H

Teamwork practice

Prerequisites
-------------

- Python >= 3.5

Required packages:

- Django 2.1.5
- others are listed in requirements.txt

Usage
-----

- Clone the repository

        git clone https://github.com/dadaday/projecth.git
        cd projecth
        
- Install dependencies

        pip install -r requirements.txt
        

- Set required environment variables in settings.ini or .env


- Migrations

        cd project_folders
        python manage.py makemigrations
        python manage.py migrate
        
- Admin user

        python manage.py createsuperuser
