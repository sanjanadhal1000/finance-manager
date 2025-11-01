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

# # Flask Web Setup
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     """Homepage Route"""
#     return render_template('index.html')

# if __name__=="__main__":
#     app.run(debug=True)

# # Adding Transaction Routes & Dashboard in Flask Finance Manager Project.
# from flask import Flask, render_template, request, redirect, url_for, flash
# import sqlite3
# import os

# app = Flask(__name__)
# app.secret_key = "Secret Key"

# db_path = os.path.join("data","finance.db")

# # Database Setup
# def init_db():
#     connection = sqlite3.connect(db_path)
#     with connection as conn:
#         conn.execute('''
#         CREATE TABLE IF NOT EXISTS transactions (
#                             id INTEGER PRIMARY KEY AUTOINCREMENT,
#                             type TEXT NOT NULL,
#                             category TEXT NOT NULL,
#                             amount REAL NOT NULL,
#                             note TEXT,
#                             date TEXT NOT NULL
#                      )
#                      ''')
        
#         conn.commit()

# init_db()

# # Routes
# @app.route('/')
# def dashboard():
#     connection = sqlite3.connect(db_path)
#     with connection as conn:
#         cursor = conn.cursor()
#         cursor.execute('''
#         SELECT sum(amount) FROM transactions WHERE type = 'income'
#                      ''')
#         total_income = cursor.fetchone()[0] or 0

#         cursor.execute("SELECT sum(amount) FROM transactions WHERE type='expense'")
#         total_expense = cursor.fetchone()[0] or 0

#         balance = total_income - total_expense
#         cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
#         records = cursor.fetchall()

#     return render_template('dashboard.html',
#                            income = total_income,
#                            expense = total_expense,
#                            balance = balance,
#                            records = records)

# @app.route('/add', methods=['GET','POST'])
# def add_transaction():
#     if request.method=='POST':
#         t_type = request.form['type']
#         category = request.form['category']
#         amount = float(request.form['amount'])
#         note = request.form['note']
#         date = request.form['date']

#         with sqlite3.connect(db_path) as conn:
#             conn.execute("INSERT INTO transactions (type, category, amount, note, date) VALUES (?, ?, ?, ?, ?)",
#                          (t_type, category, amount, note, date))
#             conn.commit()
#         flash("Transaction added successfully!")
#         return redirect(url_for('dashboard'))

#     return render_template('add_transaction.html')

# @app.route('/delete/<int:id>')
# def delete_transaction(id):
#     with sqlite3.connect(db_path) as conn:
#         conn.execute("DELETE FROM transactions WHERE id=?", (id,))
#         conn.commit()
#     flash("Transaction deleted successfully!")
#     return redirect(url_for('dashboard'))

# # Main
# if __name__=="__main__":
#     app.run(debug=True)

# # ===============================
# # DAY 29 - Data Visualization Dashboard
# # ===============================
# from flask import jsonify

# @app.route('/chart-data')
# def chart_data():
#     """Returns income and expense data per month for Chart.js visualization."""
#     user_id = session.get('user_id')
#     if not user_id:
#         return jsonify({'error': 'Not logged in'}), 403

#     conn = sqlite3.connect('data/finance.db')
#     cursor = conn.cursor()

#     cursor.execute("""
#         SELECT 
#             strftime('%Y-%m', date) AS month,
#             SUM(CASE WHEN type='income' THEN amount ELSE 0 END) AS total_income,
#             SUM(CASE WHEN type='expense' THEN amount ELSE 0 END) AS total_expense
#         FROM transactions
#         WHERE user_id=?
#         GROUP BY month
#         ORDER BY month
#     """, (user_id,))

#     data = cursor.fetchall()
#     conn.close()

#     # Convert data into lists for Chart.js
#     months = [row[0] for row in data]
#     income = [row[1] for row in data]
#     expense = [row[2] for row in data]

#     return jsonify({'months': months, 'income': income, 'expense': expense})

# ===============================
# Flask Finance Manager with Visualization
# ===============================

from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import sqlite3
import os

# -------------------------------
# Flask App Setup
# -------------------------------
app = Flask(__name__)
app.secret_key = "SuperSecretKey"

# Database Path
db_path = os.path.join("data", "finance.db")

# -------------------------------
# Database Initialization
# -------------------------------
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

# -------------------------------
# Routes
# -------------------------------

@app.route('/')
def dashboard():
    """Main Dashboard Route"""
    connection = sqlite3.connect(db_path)
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
        total_income = cursor.fetchone()[0] or 0

        cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
        total_expense = cursor.fetchone()[0] or 0

        balance = total_income - total_expense
        cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
        records = cursor.fetchall()

    return render_template('dashboard.html',
                           income=total_income,
                           expense=total_expense,
                           balance=balance,
                           records=records)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    """Add New Transaction"""
    if request.method == 'POST':
        t_type = request.form['type']
        category = request.form['category']
        amount = float(request.form['amount'])
        note = request.form['note']
        date = request.form['date']

        with sqlite3.connect(db_path) as conn:
            conn.execute(
                "INSERT INTO transactions (type, category, amount, note, date) VALUES (?, ?, ?, ?, ?)",
                (t_type, category, amount, note, date)
            )
            conn.commit()

        flash("Transaction added successfully!")
        return redirect(url_for('dashboard'))

    return render_template('add_transaction.html')

@app.route('/delete/<int:id>')
def delete_transaction(id):
    """Delete a Transaction"""
    with sqlite3.connect(db_path) as conn:
        conn.execute("DELETE FROM transactions WHERE id=?", (id,))
        conn.commit()
    flash("Transaction deleted successfully!")
    return redirect(url_for('dashboard'))

# -------------------------------
# Chart Visualization Route
# -------------------------------
@app.route('/chart-data')
def chart_data():
    """Returns income and expense data per month for Chart.js visualization."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            strftime('%Y-%m', date) AS month,
            SUM(CASE WHEN type='income' THEN amount ELSE 0 END) AS total_income,
            SUM(CASE WHEN type='expense' THEN amount ELSE 0 END) AS total_expense
        FROM transactions
        GROUP BY month
        ORDER BY month
    """)

    data = cursor.fetchall()
    conn.close()

    # Convert data into lists for Chart.js
    months = [row[0] for row in data]
    income = [row[1] for row in data]
    expense = [row[2] for row in data]

    return jsonify({'months': months, 'income': income, 'expense': expense})

# -------------------------------
# Main
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)

