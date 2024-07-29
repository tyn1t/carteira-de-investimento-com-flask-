from flask import Blueprint, render_template, redirect, url_for, request


cadastro = Blueprint('cadastro', __name__)

@cadastro.route('/cadastro', methods=['GET','POST'])
def Cadastro():
    if request.method == 'POST':
        btn_action = request.form .get('btn-action')
        if btn_action == 'cadastro':
            return redirect(url_for('home.Home'))
        elif btn_action == 'login':
            return redirect(url_for('login.Login'))
    return render_template('cadastro.html')