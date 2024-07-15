from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def glav_ekr():
    return render_template('glav_ekr.html', title='Главный экран')


@app.route('/mymaterials')
def mymaterials():
    return render_template('my materials.html', title='Мои материалы')


@app.route('/pririode_taiasha_v_sebe')
def pririode_taiasha_v_sebe():
    return render_template('pririode_taiasha_v_sebe.html', title='Природа, таящая в себе')


@app.route('/pririode_taiasha_v_sebe_glava_1_spisok_romid')
def pririode_taiasha_v_sebe_glava_1_spisok_romid():
    return render_template('pririode_taiasha_v_sebe_glava_1_spisok_romid.html', title='Список')


@app.route('/pririode_taiasha_v_sebe_glava_1_romid_1')
def pririode_taiasha_v_sebe_glava_1_romid_1():
    return render_template('pririode_taiasha_v_sebe_glava_1_romid_1.html', title='Ромид 1')


@app.route('/pririode_taiasha_v_sebe_glava_1_romid_2')
def pririode_taiasha_v_sebe_glava_1_romid_2():
    return render_template('pririode_taiasha_v_sebe_glava_1_romid_2.html', title='Ромид 1')
