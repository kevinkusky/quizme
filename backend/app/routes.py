from flask import Blueprint, render_template, redirect
from app import app


@app.route('/')
def index():
    return render_template('page.html')


@app.route('/signin')
def signin():
    return render_template('signin.html')


@app.route('/me')
def home():
    return '<h1>Home Page</h1>'


@app.route('/quiz/<id>')
def take_quiz(id):
    return render_template('quiz.html', quiz = quiz)

