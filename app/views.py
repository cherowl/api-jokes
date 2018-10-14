# -*- coding: utf-8 -*-

from app import app
import requests
# from authentication import User

@app.route('/')
def start():
    return "To start go to /login, sing in and create your database of jokes!\n"


@app.route('/login')
def login():
    '''
    Register a new user
    '''
    pass

@app.route('/logout')
def logout():
   pass

@app.route('/user/<name>')
def welcome_back(name):
    return "Welcome back, {}!\n".format(name)
    

@app.route('/user/<name>?/generate_joke')
# @login_required 
def generate_joke():
    '''
    Generate a joke using api: https://geek-jokes.sameerkumar.website/api
    '''
    response = None
    try: 
        response = requests.get("https://geek-jokes.sameerkumar.website/api")
    except: Exception('Geek Api isn\'t responding...')

    else:
        if response:
            return response.json()+"\n"