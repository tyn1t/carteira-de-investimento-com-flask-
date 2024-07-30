from flask import Blueprint, render_template, redirect, url_for, request
from models import db, Usuario

cadastro = Blueprint('cadastro', __name__)

@cadastro.route('/cadastro', methods=['GET','POST'])
def Cadastro():
    if request.method == 'POST':
        btn_action = request.form.get('btn-action')
        if btn_action == 'cadastro':
            if request.form.get('Email') == request.form.get('Email_2') and (
                request.form.get('password') ==  request.form.get('password_2')):
                
                nome = request.form.get('name')
                email = request.form.get('Email')
                password = request.form.get('password')
                    
                usuario_novo = Usuario(name=nome, email=email, password=password)
                
                db.session.add(usuario_novo)
                db.session.commit()
                
                return redirect(url_for('home.Home'))
            else:
                return redirect(url_for('cadastro.Cadastro'))
        elif btn_action == 'login':
            return redirect(url_for('login.Login'))
    
    return render_template('cadastro.html')