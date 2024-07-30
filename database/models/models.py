from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'Usuario'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(251), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    
    
    def set_password(self, Password):
        self.password = generate_password_hash(Password)

    
    def check_password(self, Password):
        return check_password_hash(self.password, Password)
     