from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def glav_ekr():
    return render_template('glav_ekr.html', title='Главный экран')
