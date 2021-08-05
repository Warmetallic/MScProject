# The Greig-Duncan Folk Song Collection

The main purpose of this web application is to store and display The Greig-Duncan Folk Song Collection. All data was provided by Dr. McKean in 8 volumes with hundreds of musical notations. The link to the data: https://www.dropbox.com/sh/k4qcsdi19vu8thl/AACJB0q9AKmo6k-rYiYGDevwa?dl=0 

Since the dataset is huge and requires a storage of several terabytes, only a few songs from the volumes are presented on the website, which is enough to demonstrate the functionality and all features of the project.

The website is deployed on Heroku and should be accessed through this web hosting service. If needed, the project can be launched locally. To do so, prepare own virtual environment and install everything from the requirements.txt file. The app was developed and tested on Windows machines in Sublime Text and Codio.


# The core features

The tools to add new songs with static files (images) and to edit already existed one. Any song can have a detailed description and multiple images, whose images display music notations.

In order to use these tools, a user need to login as an admin and with the Django admin form add a new song. The Django dashboard can be accessed through the navigation bar by clicking on the Admin link or through the direct link https://stark-mesa-89039.herokuapp.com/admin/login/?next=/admin/

A new song will be added to the main page and displayed in a catalog with other songs. It is possible to click on the song and see all information about it. Images are placed in a carousel from Bootstrap and can be switched by sliders.

The site has a multi-search function with different filters. All filters can be applied to search separately or all together to create a more precise query. The search field is placed on the right side of the navigation bar.


# User creation

First of all, it is required to create an admin user to access the Django dashboard. In order to do so, type |py manage.py createsuperuser|. Enter details (username, password and email). After that, it is possible to login into the dashboard and use the admin tools (create/edit/delete songs,images and users). In the dashboard Admin can create new users by click “ADD” button under the “AUTHENTICATION AND AUTHORIZATION’’. This will work only in the local environment. If needed to create Admin for Heroku, use this command instead |heroku run --app stark-mesa-89039 python manage.py makemigrations|.


# Song creation

New songs can be added or edited only by the admin user through the dashboard. In the dashboard click on Songs and choose ADD. Fill all fields and press SAVE.


# The app development

*Pair and mob programming*

The project was developed by a group of five students. Teams of two and three students were working on different activities based on Sprint tasks. On a weekly basis we had mob programming sessions to solve any appearing problems and explain new solutions/decisions to each other.


*Testing*

Unit testing was used to test all functions and the functionality


*Git*  

The version control system was used to create this project. It allowed our team to collaborate and use back-ups if required. Every team member was working on own branch and after a review meeting we merged all work. The git log is providing all history of the development.


*Heroku* 

The project is deployed on Heroku.

The website link: https://stark-mesa-89039.herokuapp.com/


*Data and storage*

The provided data is in TIFF format and every single file is around 80 Mbs, which is too heavy to store and to upload/display on the website. We reformatted files to the PNG format and dramatically decreased the size of images. This way it is more efficient to work with the files. To store all our static files, we used an Amazon S3 bucket, since Heroku cannot keep large files.


*Security*

All security keys for Django and Amazon S3 Bucket are placed in the env file. This file is added to gitignore, so no one can obtain the data. For a new team of developers it is a need to create own env file with new keys by using Decouple(python library).


# Additional programs

To prepare data from songs' files we are using Tesseract. This library converts images to text and stores all data into the separate file. After that, it is easy to store text data into the Django admin form. 

Tesseract instructions:

1 Prepare tiff files from Dropbox

2 Make a screenshot of every tiff file (this way an image will be in a png format, which is much lighter than tiff)

3 Crop new images

4 Store images into a separate folder

5 Open the program (Alpha-2021\folksongs\management\commands\songtxt.py)

6 Set a path to the folder with images

7 Run the program (py songtext.py)


# Commands for the local development: 

1 git clone https://github.com/UoA-CS5942/Alpha-2021.git

2 cd Alpha-2021

3 python/pip -V (checks a version)

4 pip install virtualenv (install the virtual environment)

5 virtualenv . (download everything here)

6 . ./Scripts/activate (to turn off - deactivate)

7 pip install django (install everything from the requirements list provided below)

8 py manage.py createsuperuser (create the admin user)

9 py manage.py makemigrations (packaging models into a database)

10 py manage.py migrate (apply all migrations)

11 py manage.py runserver (runs the project)


# Commands for Heroku

1 heroku login (login to your account)

2 heroku run --app stark-mesa-89039 python manage.py createsuperuser (create the admin user)

3 heroku run --app stark-mesa-89039 python manage.py makemigrations (packaging models into a database)

4 heroku run --app stark-mesa-89039 python manage.py migrate (apply all migrations)


# Requirements' List:

appdirs==1.4.4

asgiref==3.3.4

astroid==2.5.6

behave==1.2.6

bitarray==2.1.3

boto3==1.17.107

botocore==1.20.107

cffi==1.14.5

colorama==0.4.4

distlib==0.3.2

dj-database-url==0.5.0

Django==3.2.4

django-cors-headers==3.7.0

django-heroku==0.3.1

django-storages==1.11.1

django-utils-six==2.0

djangorestframework==3.12.4

filelock==3.0.12

gunicorn==20.1.0

img2pdf==0.4.1

isort==5.9.1

jmespath==0.10.0

lazy-object-proxy==1.6.0

lxml==4.6.3

mccabe==0.6.1

parse==1.19.0

parse-type==0.5.2

pdfreader==0.1.10

pikepdf==2.12.2

Pillow==8.2.0

psycopg2==2.9.1

pycparser==2.20

pycryptodome==3.10.1

pylint==2.8.3

pyPdf==1.13

PyPDF2==1.26.0

pytesseract==0.3.7

python-dateutil==2.8.1

python-decouple==3.4

pytz==2021.1

s3transfer==0.4.2

six==1.16.0

sqlparse==0.4.1

toml==0.10.2

urllib3==1.26.6

virtualenv==20.4.7

whitenoise==5.2.0

wrapt==1.12.1
