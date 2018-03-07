# MEME-ORY

A simple game of pairs with trending Memes. And Grumpy Cat.

Built with Flask, Python, JavaScript and SQLite.

### Motivation

Final Project for CS50's Introduction to Computer Science online course.

### Prerequisites

Playing the game with Memes requires [imgur API keys](https://apidocs.imgur.com/).
To provide the keys you can either make a config file "settings.cfg" with the following content:

```
API_KEY = 'YOUR_KEY'
API_SECRET = 'YOUR_SECRET_KEY'
```

or provide the keys to your Terminal:

```
export API_KEY=YOUR_KEY
export API_SECRET=YOUR_SECRET_KEY
```

### Installing

To get the game running, create an virtualenv with python 3 in the same directory as the project files.

```
python3 -m venv <myenvname>
```

activate virtualenv
```
source bin/activate
```

install required packages for python
```
pip install -r requirements.txt
```

set environment variable for flask app
```
export FLASK_APP=application.py
```

run flask
```
flask run
```

Now have fun playing!


## Authors

* **Laura Bender** 




