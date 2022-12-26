from flask import Blueprint,render_template
api  = Blueprint('api',__name__)

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,EqualTo,Email
import email_validator
from flask_mail import Mail,Message
from flask import current_app as app


class Apply(FlaskForm):
    email =  StringField("電子郵件",validators=[DataRequired(),Email(message="email錯誤")])
    password = PasswordField("密碼",validators=[DataRequired(),EqualTo('password_again',message='Passwords must match')])
    password_again = PasswordField("密碼驗證",validators=[DataRequired()])

@api.route("/",methods=['POST','GET'])
def index():
    apply_form  = Apply()    
    if apply_form.is_submitted():
        app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
        app.config['MAIL_PORT'] = 587
        app.config['MAIL_USE_TLS'] = True
        app.config['MAIL_USERNAME'] = 'roberthsu2004@gmail.com'
        app.config['MAIL_PASSWORD'] = 'ftjlhogpdhixgsem'
        mail = Mail(app)
        msg = Message('test email',sender="service@test.com",recipients=[apply_form.email.data])
        msg.body = 'this is the plain text body'
        msg.html = 'This is the <b>HTML</b> body'
        mail.send(msg)
        return '已經傳送資料過去'
    context = {
        'form':apply_form
    }
    return render_template('api/index.html',**context)