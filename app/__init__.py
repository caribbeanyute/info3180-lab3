from flask import Flask
from flask_mail import Mail




app = Flask(__name__)

SECRET_KEY = 'Sup3r$3cretkey'
app.config['SECRET_KEY'] = SECRET_KEY



app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'f38e46d0dcc254'
app.config['MAIL_PASSWORD'] = '5f6b8858994448'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)
from app import views