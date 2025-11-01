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
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     """Homepage Route"""
#     return render_template('index.html')

# if __name__=="__main__":
#     app.run(debug=True)

# Adding Transaction Routes & Dashboard in Flask Finance Manager Project.
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "Secret Key"

db_path = os.path.join("data","finance.db")

# Database Setup
def init_db():
    connection = sqlite3.connect(db_path)
    with connection as conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            type TEXT NOT NULL,
                            category TEXT NOT NULL,
                            amount REAL NOT NULL,
                            note TEXT,
                            date TEXT NOT NULL
                     )
                     ''')
        
        conn.commit()

init_db()

# Routes
@app.route('/')
def dashboard():
    connection = sqlite3.connect(db_path)
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT sum(amount) FROM transactions WHERE type = 'income'
                     ''')
        total_income = cursor.fetchone()[0] or 0

        cursor.execute("SELECT sum(amount) FROM transactions WHERE type='expense'")
        total_expense = cursor.fetchone()[0] or 0

        balance = total_income - total_expense
        cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
        records = cursor.fetchall()

    return render_template('dashboard.html',
                           income = total_income,
                           expense = total_expense,
                           balance = balance,
                           records = records)

@app.route('/add', methods=['GET','POST'])
def add_transaction():
    if request.method=='POST':
        t_type = request.form['type']
        category = request.form['category']
        amount = float(request.form['amount'])
        note = request.form['note']
        date = request.form['date']

        with sqlite3.connect(db_path) as conn:
            conn.execute("INSERT INTO transactions (type, category, amount, note, date) VALUES (?, ?, ?, ?, ?)",
                         (t_type, category, amount, note, date))
            conn.commit()
        flash("Transaction added successfully!")
        return redirect(url_for('dashboard'))

    return render_template('add_transaction.html')

@app.route('/delete/<int:id>')
def delete_transaction(id):
    with sqlite3.connect(db_path) as conn:
        conn.execute("DELETE FROM transactions WHERE id=?", (id,))
        conn.commit()
    flash("Transaction deleted successfully!")
    return redirect(url_for('dashboard'))

# Main
if __name__=="__main__":
    app.run(debug=True)

