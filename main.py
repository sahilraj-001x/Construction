from flask import Flask, render_template, flash
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcd1234903632751753'
photos_folder = path.join('static', 'images')
app.config["UPLOAD_FOLDER"] = photos_folder

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ideathon.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    aadhar = db.Column(db.Integer, nullable=False)
    phno = db.Column(db.Integer, unique=True, nullable=False)


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=2, max=30)])
    aadhar = StringField('aadhar', validators=[DataRequired(),
                                               Length(min=2, max=30)])
    phno = StringField('Phone number', validators=[DataRequired(),
                                                   Length(min=2, max=30)])
    submit = SubmitField('Signup')

    def validate_phno(self, phno):
        user = User.query.filter_by(phno=phno.data).first()
        if user:
            raise ValueError('Phone number already taken, please choose another')

    def validate_aadhar(self, aadhar):
        user = User.query.filter_by(aadhar=aadhar.data).first()
        if user:
            raise ValueError('Wrong aadhar')


@app.route("/", methods=['POST', 'GET'])
# @app.route("/home", methods=['POST', 'GET'])
def homepage():
    logo = path.join(app.config["UPLOAD_FOLDER"], "logo.png")
    search_icon = path.join(app.config["UPLOAD_FOLDER"], "search-icon.png")
    left_icon = path.join(app.config["UPLOAD_FOLDER"], "left-icon.png")
    right_icon = path.join(app.config["UPLOAD_FOLDER"], "right-icon.png")
    about_img = path.join(app.config["UPLOAD_FOLDER"], "about-img.png")
    icon_1 = path.join(app.config["UPLOAD_FOLDER"], "icon-1.png")
    img_3 = path.join(app.config["UPLOAD_FOLDER"], "img-3.png")
    img_4 = path.join(app.config["UPLOAD_FOLDER"], "img-4.png")
    img_5 = path.join(app.config["UPLOAD_FOLDER"], "img-5.png")
    img_6 = path.join(app.config["UPLOAD_FOLDER"], "img-6.png")
    img_7 = path.join(app.config["UPLOAD_FOLDER"], "img-7.png")
    agro = path.join(app.config["UPLOAD_FOLDER"], "agro.png")
    return render_template("index.html", logo=logo, search_icon=search_icon, left_icon=left_icon, right_icon=right_icon,
                           about_img=about_img, agro=agro, icon_1=icon_1, img_3=img_3, img_4=img_4, img_6=img_6,
                           img_5=img_5, img_7=img_7)


@app.route("/projects", methods=['POST', 'GET'])
def projects():
    logo = path.join(app.config["UPLOAD_FOLDER"], "logo.png")
    img_3 = path.join(app.config["UPLOAD_FOLDER"], "img-3.png")
    img_4 = path.join(app.config["UPLOAD_FOLDER"], "img-4.png")
    img_5 = path.join(app.config["UPLOAD_FOLDER"], "img-5.png")
    img_6 = path.join(app.config["UPLOAD_FOLDER"], "img-6.png")
    map_icon = path.join(app.config["UPLOAD_FOLDER"], "map-icon.png")
    call_icon = path.join(app.config["UPLOAD_FOLDER"], "call-icon.png")
    mail_icon = path.join(app.config["UPLOAD_FOLDER"], "mail-icon.png")
    return render_template("projects.html", logo=logo, img_3=img_3, img_4=img_4, img_6=img_6, img_5=img_5,
                           mail_icon=mail_icon, call_icon=call_icon, map_icon=map_icon)


@app.route("/services", methods=['POST', 'GET'])
def services():
    logo = path.join(app.config["UPLOAD_FOLDER"], "logo.png")
    img_3 = path.join(app.config["UPLOAD_FOLDER"], "img-3.png")
    img_4 = path.join(app.config["UPLOAD_FOLDER"], "img-4.png")
    img_5 = path.join(app.config["UPLOAD_FOLDER"], "img-5.png")
    img_6 = path.join(app.config["UPLOAD_FOLDER"], "img-6.png")
    map_icon = path.join(app.config["UPLOAD_FOLDER"], "map-icon.png")
    call_icon = path.join(app.config["UPLOAD_FOLDER"], "call-icon.png")
    mail_icon = path.join(app.config["UPLOAD_FOLDER"], "mail-icon.png")
    return render_template("services.html", logo=logo, img_3=img_3, img_4=img_4, img_6=img_6, img_5=img_5,
                           mail_icon=mail_icon, call_icon=call_icon, map_icon=map_icon)


@app.route("/about", methods=['POST', 'GET'])
def about():
    logo = path.join(app.config["UPLOAD_FOLDER"], "logo.png")
    img_3 = path.join(app.config["UPLOAD_FOLDER"], "img-3.png")
    img_4 = path.join(app.config["UPLOAD_FOLDER"], "img-4.png")
    img_5 = path.join(app.config["UPLOAD_FOLDER"], "img-5.png")
    img_6 = path.join(app.config["UPLOAD_FOLDER"], "img-6.png")
    map_icon = path.join(app.config["UPLOAD_FOLDER"], "map-icon.png")
    call_icon = path.join(app.config["UPLOAD_FOLDER"], "call-icon.png")
    mail_icon = path.join(app.config["UPLOAD_FOLDER"], "mail-icon.png")
    return render_template("about.html", logo=logo, img_3=img_3, img_4=img_4, img_6=img_6, img_5=img_5,
                           mail_icon=mail_icon, call_icon=call_icon, map_icon=map_icon)


@app.route("/login", methods=['POST', 'GET'])
def contact():
    form = RegistrationForm()
    logo = path.join(app.config["UPLOAD_FOLDER"], "logo.png")
    img_3 = path.join(app.config["UPLOAD_FOLDER"], "img-3.png")
    img_4 = path.join(app.config["UPLOAD_FOLDER"], "img-4.png")
    img_5 = path.join(app.config["UPLOAD_FOLDER"], "img-5.png")
    img_6 = path.join(app.config["UPLOAD_FOLDER"], "img-6.png")
    map_icon = path.join(app.config["UPLOAD_FOLDER"], "map-icon.png")
    call_icon = path.join(app.config["UPLOAD_FOLDER"], "call-icon.png")
    mail_icon = path.join(app.config["UPLOAD_FOLDER"], "mail-icon.png")
    if form.validate_on_submit():
        user = User(username=form.username.data, aadhar=form.aadhar.data, phno=form.phno.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account is successfully created', 'success')
    return render_template("contact.html", logo=logo, img_3=img_3, img_4=img_4, img_6=img_6, img_5=img_5,
                           mail_icon=mail_icon, call_icon=call_icon, map_icon=map_icon, form=form)


if __name__ == "__main__":
    app.secret_key = 'thisismysupersecretkey'
    app.run(debug=True)
