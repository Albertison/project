from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def glav_ekr():
    return render_template('glav_ekr.html', title='Главный экран')


@app.route('/mymaterials')
def mymaterials():
    return render_template('my materials.html', title='Мои материалы')


@app.route('/dnevnic')
def dnevnic():
    return render_template('my dnevnic.html', title='Дневник')


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
    return render_template('pririode_taiasha_v_sebe_glava_1_romid_2.html', title='Ромид 2')


@app.route('/pririode_taiasha_v_sebe_glava_1_romid_3')
def pririode_taiasha_v_sebe_glava_1_romid_3():
    return render_template('pririode_taiasha_v_sebe_glava_1_romid_3.html', title='Ромид 3')


@app.route('/pririode_taiasha_v_sebe_glava_1_romid_4')
def pririode_taiasha_v_sebe_glava_1_romid_4():
    return render_template('pririode_taiasha_v_sebe_glava_1_romid_4.html', title='Ромид 4')


@app.route('/pririode_taiasha_v_sebe_glava_1_romid_5')
def pririode_taiasha_v_sebe_glava_1_romid_5():
    return render_template('pririode_taiasha_v_sebe_glava_1_romid_5.html', title='Ромид 5')


@app.route('/pririode_taiasha_v_sebe_glava_1_romid_6')
def pririode_taiasha_v_sebe_glava_1_romid_6():
    return render_template('pririode_taiasha_v_sebe_glava_1_romid_6.html', title='Ромид 6')


@app.route('/pririode_taiasha_v_sebe_glava_1_romid_7')
def pririode_taiasha_v_sebe_glava_1_romid_7():
    return render_template('pririode_taiasha_v_sebe_glava_1_romid_7.html', title='Ромид 7')


@app.route('/pririode_taiasha_v_sebe_glava_1_romid_8')
def pririode_taiasha_v_sebe_glava_1_romid_8():
    return render_template('pririode_taiasha_v_sebe_glava_1_romid_8.html', title='Ромид 8')


@app.route('/pririode_taiasha_v_sebe_glava_1_spisok_romid_2')
def pririode_taiasha_v_sebe_glava_1_spisok_romid_2():
    return render_template('pririode_taiasha_v_sebe_glava_1_spisok_romid_2.html', title='Список 2')


@app.route('/pririode_taiasha_v_sebe_glava_2_romid_1')
def pririode_taiasha_v_sebe_glava_2_romid_1():
    return render_template('pririode_taiasha_v_sebe_glava_2_romid_1.html', title='Ромид 1')


@app.route('/pririode_taiasha_v_sebe_glava_2_romid_2')
def pririode_taiasha_v_sebe_glava_2_romid_2():
    return render_template('pririode_taiasha_v_sebe_glava_2_romid_2.html', title='Ромид 2')


@app.route('/pririode_taiasha_v_sebe_glava_2_romid_3')
def pririode_taiasha_v_sebe_glava_2_romid_3():
    return render_template('pririode_taiasha_v_sebe_glava_2_romid_3.html', title='Ромид 3')


@app.route('/pririode_taiasha_v_sebe_glava_2_romid_4')
def pririode_taiasha_v_sebe_glava_2_romid_4():
    return render_template('pririode_taiasha_v_sebe_glava_2_romid_4.html', title='Ромид 4')


@app.route('/pririode_taiasha_v_sebe_glava_2_romid_5')
def pririode_taiasha_v_sebe_glava_2_romid_5():
    return render_template('pririode_taiasha_v_sebe_glava_2_romid_5.html', title='Ромид 5')


@app.route('/pririode_taiasha_v_sebe_glava_2_romid_6')
def pririode_taiasha_v_sebe_glava_2_romid_6():
    return render_template('pririode_taiasha_v_sebe_glava_2_romid_6.html', title='Ромид 6')


@app.route('/pririode_taiasha_v_sebe_glava_2_romid_7')
def pririode_taiasha_v_sebe_glava_2_romid_7():
    return render_template('pririode_taiasha_v_sebe_glava_2_romid_7.html', title='Ромид 7')


@app.route('/pririode_taiasha_v_sebe_glava_2_romid_8')
def pririode_taiasha_v_sebe_glava_2_romid_8():
    return render_template('pririode_taiasha_v_sebe_glava_2_romid_8.html', title='Ромид 8')


@app.route('/pririode_taiasha_v_sebe_glava_2_romid_9')
def pririode_taiasha_v_sebe_glava_2_romid_9():
    return render_template('pririode_taiasha_v_sebe_glava_2_romid_9.html', title='Ромид 9')


@app.route('/pririode_taiasha_v_sebe_glava_2_romid_10')
def pririode_taiasha_v_sebe_glava_2_romid_10():
    return render_template('pririode_taiasha_v_sebe_glava_2_romid_10.html', title='Ромид 10')


@app.route('/pririode_taiasha_v_sebe_glava_2_romid_11')
def pririode_taiasha_v_sebe_glava_2_romid_11():
    return render_template('pririode_taiasha_v_sebe_glava_2_romid_11.html', title='Ромид 11')


@app.route('/pririode_taiasha_v_sebe_glava_2_romid_12')
def pririode_taiasha_v_sebe_glava_2_romid_12():
    return render_template('pririode_taiasha_v_sebe_glava_2_romid_12.html', title='Ромид 12')