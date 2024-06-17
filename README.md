# MaykinMedia-test

[![Python Latest version](https://img.shields.io/badge/python-3.8.5-blue.svg)](https://www.python.org/downloads/release/python-385/)
[![Django Latest version](https://img.shields.io/badge/django-3.1.2-blue.svg)](https://www.djangoproject.com/download/)
[![Django Rest Framework Latest version](https://img.shields.io/badge/django_rest_framework-3.12.1-blue.svg)](https://www.django-rest-framework.org/)

This is an app dedicated to an internship application test in order to land an internship at Maykin Media. The app is build in Django and follows a list of bulletpoints provided in the case files.
```bash
  git clone https://github.com/Xander172006/MaykinMedia-test.git
```
Once the project is cloned, you need to run the following commands in the **installation** section below.
<br />
<br />

## Installation
By installing the following packages and libraries, you can ensure the app runs smoothly.
Ensure that you have installed the latest version of Python and Django.
```bash
  pip install -r requirements.txt
```
<br />

create a new .env file to store the username credentials and urls for the project:

```markdown
MaykinMedia-test/
├── opdracht/
│   └── demo/
│       ├── demo/
│       ├── internship_test/
│       ├── (.env)
│       ├── db.sqlite3
│       └── manage.py
│
├── .gitignore
├── Case Maykin Media - Django (nederlands).pdf
└── README.md
```
<br />


## usage

Make sure you have a database user and create a database named `maykin_media_test`. Then follow these credentials to connect to the database:
```env
CITY_URL=city_url
HOTEL_URL=hotel_url
USERNAME=username
PASSWORD=password
```

Afterwards, make sure you run the migration commands to create the tables and insert the data within them.
```bash
  python manage.py migrate
  python manage.py import_data
```
<br />

Finally you will be able to visit the home page using the `/home` route.
<br />

## Contributors

![Xander Poggenklaas](https://img.shields.io/badge/Xander_Poggenklaas-Developer-blue)

[<img src="https://github.com/Xander172006.png" width="65px" height="65px" style="border-radius: 50px"/>](Xander172006)
