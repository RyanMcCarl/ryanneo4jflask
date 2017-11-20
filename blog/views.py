#from .models import User, get_todays_recent_posts
from .models import Word
from flask import Flask, request, session, redirect, url_for, render_template, flash

app = Flask(__name__)

@app.route('/')
def index():
    #posts = get_todays_recent_posts()
    return render_template('index.html')#, posts=posts)

@app.route('/word/<word>')
def word(word):
    return render_template('word.html', word=Word(word))
