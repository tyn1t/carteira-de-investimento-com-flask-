from flask import Blueprint, render_template, url_for, redirect, request 
from database.models.models import Usuario, check_password_hash


login = Blueprint('login', __name__)

@login.route('/login', methods=['POST', 'GET'])
def Login():
    """LOgin do usuaro ja cadastro """
    if request.method == 'POST':
        action =  request.form.get('btn-action')
        if action == 'login':
            name = request.form.get('name')
            email = request.form.get('Email')
            if ((Usuario.query.filter(Usuario.email == email)) and Usuario.query.filter(Usuario.name == name)):
                
                Password = request.form.get('password') 
                
                
                usuario = Usuario.query.filter_by(email=email).first()

                if  usuario.check_password(Password):
                    return   'ok'
                
               #return redirect(url_for('home.Home'))
                return 'erro final'    
            else:
                Usuario.query.filter(Usuario.name == name)
                
                return 'Error ok '
            
        elif action == 'cadastra':
            return redirect(url_for('cadastro.Cadastro'))
            
        
        
    return render_template('login.html')



