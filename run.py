from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

show = True

@app.route('/', methods=['GET'])
def hideControls():
    return render_template('index.html', show=show)

@app.route('/', methods=['POST'])
def showControls():
    show = request.form.get('show') == 'show'
    return render_template('index.html', show=show)
