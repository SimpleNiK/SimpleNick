import flask
from flask import Flask, render_template
import random

wheather = [
            'Завтра будет солнечно, +40',
            'Завтра будет пасмурно, возможен дождь',
            'Завтра будет гроза, обильный ливень.'
                                                     ]
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/me')
def me():
    return render_template('me.html')

@app.route('/wheather')
def whether():
    return render_template('whether.html', wheather = random.choice(wheather))

app.run(debug = True, port = 8080)