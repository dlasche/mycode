#!/usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/correct')
def success():
    return 'Correct!'

@app.route('/answer', methods=['POST'])
def answer():
    if request.form.get('ans'):
        answer = request.form.get('ans')
        if answer == '42':
            return redirect('/correct')
        else:
            return redirect('/')
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2224)
