# DjangoBlog
Example project in Django. Very simple forum rather than blog, bad naming aside. Was created for studying framework purposes.

## Current features

 - Basic user registration and authorization
 - Very basic forum divided by categories, subcategories and topics
 - User profiles with profile pictures and ability to change them
 - Broken presentation
 
## Work in progress

 - Better presentation
 - Better UI for administration
 - Better security for authorization
 - Alert messages
 - Possible rework of database
 - 
## Installation
 - Clone this repository `git clone https://github.com/ZheZheDoshka/djangoBlog`
 - Go to repository  `cd *path*\djangoBlog\sampleBlog`
 - If you don't have virtualenv, install it  `pip install virtualenv`
 - Create new env `virtualenv venv`  
 - Enter it `source venv/bin/activate` 
 - Install requirement  `pip install -r requirements.txt` 
 - From environment, run following:
 -  - `manage.py makemigrations`
 -  - `manage.py migrate`
 - To start web app itself, run following
 -  - `manage.py runserver`
 - Alternatively, you can build and run docker container
 -  - `docker compose up --build`