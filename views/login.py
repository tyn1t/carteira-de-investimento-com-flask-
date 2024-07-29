from flask import Blueprint, render_template, url_for, redirect, request 


login = Blueprint('login', __name__)

@login.route('/login', methods=['POST', 'GET'])
def Login():
    """LOgin do usuaro ja cadastro """
    if request.method == 'POST':
        action =  request.form.get('btn-action')
        if action == 'login':
            name = request.form.get('name')
            email = request.form.get('Email')
            password = request.form.get('password')
            return redirect(url_for('home.Home'))
        
        elif action == 'cadastra':
            return redirect(url_for('cadastro.Cadastro'))
            
        
        return render_template('index.html')
    return render_template('login.html')



