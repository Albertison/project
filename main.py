from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def glav_ekr():
    return render_template('glav_ekr.html', title='Главный экран')


@app.route('/mymaterials')
def mymaterials():
    return render_template('my materials.html', title='Мои материалы')
