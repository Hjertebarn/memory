# MEME-ORY

A simple game of pairs with trending Memes. And Grumpy Cat.

Built with Flask, Python, JavaScript and SQLite.

## Motivation

Final Project for CS50's Introduction to Computer Science online course.

## Prerequisites

Playing the game with Memes requires [imgur API keys](https://apidocs.imgur.com/).
In order to provide the keys you can either make a config file "settings.cfg" with the following content:

```
API_KEY = 'YOUR_KEY'
API_SECRET = 'YOUR_SECRET_KEY'
```

or provide the keys as environment variables:

```
export API_KEY=YOUR_KEY
export API_SECRET=YOUR_SECRET_KEY
```

## Installing

To get the game running, create an virtual environment with python 3 in the same directory as the project.

```
python3 -m venv <myenvname>
```

activate virtualenv:
```
source bin/activate
```

install required packages for python:
```
pip install -r requirements.txt
```

set environment variable for flask app:
```
export FLASK_APP=application.py
```

start flask:
```
flask run
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) and have fun playing!


## Authors

* Laura Bender




