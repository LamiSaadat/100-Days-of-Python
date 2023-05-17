# save this as app.py
from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper():
        return "<b>{}</b>"
    return wrapper

@app.route("/")
def hello():
    return "<h1 style='text-align: center'>Hello, World!</h1>\
        <p style='font-size: 50px'>This is a paragraph.</p>\
        <img src='https://media.giphy.com/media/j1DzWAerkPMaRPp4jN/giphy.gif' style='width: 400px'>"

@app.route("/bye")
@make_bold
def bye():
    return "Bye!"

#variable rules for URLs
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"

class User:
    def __init__(self,name) -> None:
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("lamisa")
new_user.is_logged_in = True
create_blog_post(new_user)