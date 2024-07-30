from flask import Flask 
from flask_migrate import Migrate
from views.login import login
from views.cadastro import cadastro
from database.models.models import db


def create_app():

    app = Flask(__name__, template_folder='templates')
    
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./Testdb.db'
     
    # app.register_blueprint(home)
    app.register_blueprint(cadastro, prefix='/cadastro')
    app.register_blueprint(login, prefix='/login')
    
    
    db.init_app(app)
    

    
    
    migrate = Migrate(app, db)
    
    return app 




    



