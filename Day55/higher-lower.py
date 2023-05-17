from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
	return "<h1>Guess a number between 0 and 9</h1>"

rand_num = random.randint(0,9)

@app.route("/<int:number>")
def show_gif(number):
	if number < rand_num:
		return "<h1 style='color: blue'>Too low! Guess again</h1><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
	elif number > rand_num:
		return "<h1 style='color: red'>Too high! Guess again</h1><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'"
	else:
		return "<h1 style='color: green'>Nice work!</h1><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"