#Импорт
from flask import Flask, render_template,request, redirect
#Подключение библиотеки баз данных
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#Подключение SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gh.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Создание db
db = SQLAlchemy(app )

class User(db.Model):
    username = db.Column(db.String(50), nullable=False)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.String(100), nullable=False)
    #bd = db.Column(db.String(250), nullable=False)
#Запуск страницы с регистрацеей
@app.route('/register',  methods=['GET','POST'])
def form__input():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    else:
        return render_template('registration.html')
    users = User(password=password, username=username, id=id)
    userid = User.query.order_by(User.id).all()
    print(users)
    return "ok"
@app.route('/')
def perenapravit():

    return redirect('/register')

@app.route('/u/<username>')
def user(username):
    print(username)
    return render_template('userprofile.html', username=username)

@app.route('/signin')
def signin():
    
    return render_template('signin.html')

if __name__ == "__main__":
    app.run(debug=True)