
from flask import Flask, redirect, render_template, request, flash, url_for
from wtforms import TextAreaField, SelectField
from wtforms import Form, BooleanField, StringField, PasswordField, validators

from flask_sqlalchemy import SQLAlchemy


base_dir = '.'


try:
    import webview
    if hasattr(sys, '_MEIPASS'):
        base_dir = os.path.join(sys._MEIPASS)
        app = Flask(__name__, static_folder=os.path.join(base_dir, 'static'), template_folder=os.path.join(base_dir, 'templates'))
except:
    app = Flask(__name__)



app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bookmarks.sqlite"
app.config["SQLALCHEMY_ECHO"] = True
app.config['debug'] = True
#app.config['SECRET_KEY'] = 
db = SQLAlchemy(app)


class PassForm(Form):
    password = PasswordField('Optional Password:')
    boo = BooleanField('include password?')



class Bmark(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   url = db.Column(db.String(100))
   description = db.Column(db.String(50))
   password = db.Column(db.String(200))
   picker = db.Column(db.String(100))

class BookMarkForm(Form):
    url = StringField('website url:', [validators.DataRequired(message='data required')])
    description = TextAreaField('description:')
    picker = SelectField('categories:', choices=('technology', 'funny'))


@app.route('/', methods=['GET', 'POST'])
def home():
    form = BookMarkForm(request.form)
    pform = PassForm(request.form)
    if request.method == 'POST' and 'http' in str(request.form['url']):
        value = Bmark(url=request.form['url'], description=request.form['description'], password=request.form['password'], picker=request.form['picker'])
        db.session.add(value)
        db.session.commit()
        flash('must include http')
        return redirect(url_for('site_list'))




    return render_template('create.html', form=form, pform=pform)

@app.route('/sitelist', methods=['GET', 'POST'])
def site_list():
    if request.method == 'POST':
        return redirect('/')
    value = Bmark.query.all()
    print(value)
    return render_template('listview.html', values=value)

@app.route('/category', methods=['GET', 'POST'])
def kat():
    if request.method == 'POST':
        return redirect('/')
    value = Bmark.query.all()
    print(value)
    return render_template('category.html', values=value)
if __name__ == '__main__':

    try:
        db.create_all()
        webview.create_window('Flask example', app)
        webview.start(gui='cef')
    except:
        db.create_all()
        app.run()



