from flask import Blueprint, render_template, redirect, url_for, request
from database.models.models import Usuario, db 

cadastro = Blueprint('cadastro', __name__)

@cadastro.route('/cadastro', methods=['GET','POST'])
def Cadastro():
    message = {'Status':None}
    if request.method == 'POST':
        btn_action = request.form .get('btn-action')
        
        if btn_action == 'cadastro':
            
            
            if (request.form.get('Email') == request.form.get('EmaiL')) and (
            request.form.get('password') == request.form.get('Password')):
                
                name = request.form.get('name')
                Email = request.form.get('Email')
                password = request.form.get('password')
                
                
                if not Usuario.query.filter_by(email=Email).first():
                    
                    
                        
                    usuario = Usuario(name=name, email=Email)
                    usuario.set_password(password) 
                    
                    message = {'Status':True}
                    
                    try:
                        db.session.add(usuario)
                        db.session.commit()
                        
                        
                        
                        return redirect(url_for('login.Login'))
                    except:
                       message = {'Status':False}
                                      
            
            
        elif btn_action == 'login':
            return redirect(url_for('login.Login'))
        
    return render_template('cadastro.html', message)
