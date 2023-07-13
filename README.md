# DjangoBlog
Example project in Django. Very simple forum rather than blog, bad naming aside. Was created for studying framework purposes.

## Current features

 - Basic user registration and authorization
 - Very basic forum divided by categories, subcategories and topics
 - Broken presentation
 
## Work in progress
 - User profiles
 - Better presentation
 - Better UI for administration
 - Better security for authorization
 - Alert messages
 - Possible rework of database
 - 
## Installation
Clone this repository `git clone https://github.com/ZheZheDoshka/djangoBlog`
Go to repository  `cd *path*djangoBlog\sampleBlog`
If you don't have virtualenv, install it  `pip install virtualenv`
Create new env `virtualenv venv`  
Enter it `source venv/bin/activate` 
Install requirement  `pip install -r requirements.txt` 
From environment, run following:
`manage.py makemigrations`
`manage.py migrate`
`manage.py runserver`