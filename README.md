# Web Mafia
This project serves as the successor to the original web mafia game that was written purely in Python with Django.

The goal is to streamline the functionality of the service, by making use of a decoupled architecture consisting of a standalone backend written as a Django REST API, and an independant front end written with React.

## Goals
[] Setup project skeleton
[] Port over API functionality
[] Create UI components for Game Host
[] Create UI components for players
[] Implement web sockets communication for lobby and role distribution

# Development setup
It is recommended that you set up a virtual env using Python to keep your dependencies managed in one place. To do this, run `python -m venv env_name` (select a suitable name other than env_name). On mac/linux, you can activate the virtual env by running `source env_name/bin/activate`. on Windows, run `env_name\Scripts\activate`

Then install the necessary dependencies using `pip install -r requirements.txt`

Next, you need to create the database for the service locally. You can do this by running `python manage.py makemigrations` and then `python manage.py migrate` from inside of ./webmafia

To set up the react project, you need to run `npm install` from inside of ./webmafia.

# Running locally
To run the Django server, run `python manage.py runserver` from inside of ./webmafia2

To run the React app for access to the front end, run `npm run dev` from inside of ./webmafia