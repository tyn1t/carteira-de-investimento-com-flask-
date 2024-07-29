from flask import Flask , render_template, url_for
from views.home import home
from views.login import login 
from views.cadastro import cadastro

app = Flask(__name__)


app.register_blueprint(home)
app.register_blueprint(cadastro, prefix='/cadastro')
app.register_blueprint(login, prefix='/login')


if __name__=="__main__":
   app.run(debug=True)