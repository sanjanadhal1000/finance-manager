# from flask import Flask,render_template,request,redirect,url_for,session
# from finance_manager import FinanceManager
# import sqlite3

# app = Flask(__name__)
# app.secret_key = "SuperSecretKey" # for session management

# db = FinanceManager()

# @app.route('/')
# def home():
#     return render_template("login.html")

# @app.route('/register',methods=['GET','POST'])
# def register():
#     if request.method=="POST":
#         username = request.form['username']
#         password = request.form['password']

#         db.connection = sqlite3.connect(db)
#         db.cursor = db.connection.cursor()

#         db.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

#         db.connection.commit()
#         return redirect(url_for('home'))
#     return render_template('register.html')

# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form['username']
#     password = request.form['password']

#     db.connection = sqlite3.connect(db)
#     db.cursor = db.connection.cursor()

#     db.cursor.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
#     user = db.cursor.fetchone()
#     if user:
#         session['user_id'] = user[0]
#         return redirect(url_for('dashboard'))
#     return "Invalid login! Try again."

# @app.route('/dashboard')
# def dashboard():
#     if 'user_id' not in session:
#         return redirect(url_for('home'))
#     return render_template('dashboard.html')

# @app.route('/logout')
# def logout():
#     session.pop('user_id',None)
#     return redirect(url_for('home'))

# if __name__=="__main__":
#     app.run(debug=True)

# Flask Web Setup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Homepage Route"""
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

