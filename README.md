# The Greig-Duncan Folk Song Collection

The main purpose of this web application is to store and display The Greig-Duncan Folk Song Collection. All data was provided by Dr. McKean in 8 volumes with hundreds of musical notations. The link to the data: https://www.dropbox.com/sh/k4qcsdi19vu8thl/AACJB0q9AKmo6k-rYiYGDevwa?dl=0 

Since the dataset is huge and requires a storage of several terabytes, only a few songs from the volumes are presented on the website, which is enough to demonstrate the functionality and all features of the project.

The website is deployed on Heroku and should be accessed through this web hosting service. If needed, the project can be launched locally. To do so, prepare own virtual environment and install everything from the requirements.txt file. The app was developed and tested on Windows machines in Sublime Text and Codio.

**_The core features_**

The tools to add new songs with static files (images) and to edit already existed one. Any song can have a detailed description and multiple images, whose images display music notations.

In order to use these tools, a user need to login as an admin and with the Django admin form add a new song. The Django dashboard can be accessed through the navigation bar by clicking on the Admin link or through the direct link https://stark-mesa-89039.herokuapp.com/admin/login/?next=/admin/

A new song will be added to the main page and displayed in a catalog with other songs. It is possible to click on the song and see all information about it. Images are placed in a carousel from Bootstrap and can be switched by sliders.

The site has a multi-search function with different filters. All filters can be applied to search separately or all together to create a more precise query. The search field is placed on the right side of the navigation bar.

**_The app development_**

*Pair and mob programming*

The project was developed by a group of five students. Teams of two and three students were working on different activities based on Sprint tasks. On a weekly basis we had mob programming sessions to solve any appearing problems and explain new solutions/decisions to each other.

*Testing*

Unit testing was used to test all functions and the functionality

*Git*  

The version control system was used to create this project. It allowed our team to collaborate and use back-ups if required. Every team member was working on own branch and after a review meeting we merged all work. The git log is providing all history of the development.

*Heroku* 

The project is deployed on Heroku.

The website link: https://stark-mesa-89039.herokuapp.com/

Authorisation details for admin:
-Username: admin
-Password: admin

*Data and storage*

The provided data is in TIFF format and every single file is around 80 Mbs, which is too heavy to store and to upload/display on the website. We reformatted files to the PNG format and dramatically decreased the size of images. This way it is more efficient to work with the files. To store all our static files, we used an Amazon S3 bucket, since Heroku cannot keep large files.

*Security*

All secret keys for Django and Amazon S3 Bucket are stored in the separate .env file. The file is stored in the gitignore, so it is hidden from everybody. Also, it is required to add Config Vars with the secret keys on Heroku.

Create a new .env file with this data and add to the root directory:
Django - SECRET_KEY = 'django-insecure-^e)j=n8!xz@!@lmiz&8^=$i^#_!0r@(1&(pyyi9-2lts1d0&pz'
S3 Busket - AWS_ACCESS_KEY_ID = 'AKIAZSRGGY2T2EFPLFHV'
S3 Busket - AWS_SECRET_ACCESS_KEY = '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'


**_Requirements' List:_**

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
