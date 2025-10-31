# # User Registration and Login

# import sqlite3
# connection = sqlite3.connect("data/finance.db")

# import sqlite3
# import os

# DB_PATH = "data/finance.db"

# # ✅ Create database and users table if not exists
# def setup_database():
#     os.makedirs("data", exist_ok=True)
#     connection = sqlite3.connect(DB_PATH)
#     cursor = connection.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT UNIQUE,
#             email TEXT,
#             password TEXT
#         )
#     """)

#     connection.commit()
#     connection.close()


# # ✅ Register new user
# def register_user():
#     username = input("Enter username: ")
#     email = input("Enter email: ")
#     password = input("Enter password: ")

#     connection = sqlite3.connect(DB_PATH)
#     cursor = connection.cursor()

#     try:
#         cursor.execute(
#             "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
#             (username, email, password)
#         )
#         connection.commit()
#         print("\n✅ Registration successful!\n")
#     except sqlite3.IntegrityError:
#         print("\n⚠️ Username already exists! Try a different one.\n")
#     finally:
#         connection.close()


# # ✅ Login existing user
# def login_user():
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     connection = sqlite3.connect(DB_PATH)
#     cursor = connection.cursor()
#     cursor.execute(
#         "SELECT * FROM users WHERE username = ? AND password = ?",
#         (username, password)
#     )

#     user = cursor.fetchone()
#     connection.close()

#     if user:
#         print(f"\n✅ Welcome back, {username}!\n")
#         return True
#     else:
#         print("\n❌ Invalid credentials. Please try again.\n")
#         return False


# # ✅ Main Menu
# def main():
#     setup_database()

#     while True:
#         print("==== Finance Manager ====")
#         print("1. Register")
#         print("2. Login")
#         print("3. Exit")
#         choice = input("Enter choice (1-3): ")

#         if choice == "1":
#             register_user()
#         elif choice == "2":
#             if login_user():
#                 print("You can now access your finance features.\n")
#         elif choice == "3":
#             print("Exiting... Goodbye!")
#             break
#         else:
#             print("Invalid choice, try again.\n")


# if __name__ == "__main__":
#     main()

# Add Income and Expense

import sqlite3
from datetime import datetime

def connect_db():
    connection = sqlite3.connect("data/finance.db")
    cursor = connection.cursor()

    # Create Users Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT UNIQUE,
                   password TEXT
                   )
                   """)
    
    # Create Transactions Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id INTEGER,
                   type TEXT,
                   amount REAL,
                   category TEXT,
                   date TEXT,
                   note TEXT,
                   FOREIGN KEY (user_id) REFERENCES users(id)
                   )
                   """)
    
    connection.commit()
    connection.close()

# User Registration
def register_user():
    username = input("Enter a username: ")
    password = input("Enter the password: ")

    connection = sqlite3.connect("data/finance.db")
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO users (username,password) VALUES (?,?)",(username,password))
        connection.commit()
        print("User Registered Successfully!\n")
    except sqlite3.IntegrityError:
        print("Username already exists! Please Try Again!")
    finally:
        connection.close()

# User Login
def login_user():
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    connection = sqlite3.connect("data/finance.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
    user = cursor.fetchone()
    connection.commit()

    if user:
        print(f"Welcome Back, {username}!\n")
        return user[0]                        # Returning user_id
    else:
        print("Invalid Credentials! Please Try Again!\n")
        return None
    
# Add Income
def add_income(user_id):
    amount = float(input("Enter Amount: "))
    category = input("Enter Category: ")
    note = input("Add a short note (optional): ")
    date = datetime.now().strftime("%Y-%m-%d")

    connection = sqlite3.connect("data/finance.db")
    cursor = connection.cursor()

    cursor.execute("""INSERT INTO transactions (user_id,type,amount,category,note,date) 
                   VALUES (?,'income',?,?,?,?)""",
                   (user_id,amount,category,note,date))
    
    connection.commit()
    connection.close()

    print("Income Added Successfully!\n")

# Add Expense
def add_expense(user_id):
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category (e.g., Food, Travel, Shopping): ")
    note = input("Add a short note (optional): ")
    date = datetime.now().strftime("%Y-%m-%d")

    connection = sqlite3.connect("data/finance.db")
    cursor = connection.cursor()

    cursor.execute("""INSERT INTO transactions (user_id, type, amount, category, date, note)
                      VALUES (?, 'expense', ?, ?, ?, ?)""",
                   (user_id, amount, category, date, note))

    connection.commit()
    connection.close()
    print("Expense added successfully!\n")

# View Transactions
def view_transactions(user_id):
    connection = sqlite3.connect("data/finance.db")
    cursor = connection.cursor()

    cursor.execute("SELECT type, amount, category, date, note FROM transactions WHERE user_id=?", (user_id,))
    rows = cursor.fetchall()
    connection.close()

    if not rows:
        print("No transactions found.\n")
        return

    print("\nTransaction History:")
    for t in rows:
        print(f"{t[3]} | {t[0].capitalize()} | Rs.{t[1]} | {t[2]} | Note: {t[4]}")
    print()

# Main Menu
def main():
    connect_db()
    print("--- Welcome to Personal Finance Manager---\n")

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter a choice (1-3): ")

        if choice=="1":
            register_user()
        elif choice=="2":
            user_id = login_user()
            if user_id:
                while True:
                    print("\n---Menu---")
                    print("1. Add Income")
                    print("2. Add Expense")
                    print("3. View Transactions")
                    print("4. Logout")

                    ch = input("Enter your choice (1-4): ")

                    if ch=="1":
                        add_income(user_id)
                    elif ch=="2":
                        add_expense(user_id)
                    elif ch=="3":
                        view_transactions(user_id)
                    elif ch=="4":
                        print("User logged out!\n")
                        break
                    else:
                        print("Invalid Choice! Try Again!\n")

        elif choice=="3":
            print("Thank you for using the Personal Finance Manager! Hope to See You Again!")
            break
        else:
            print("Invalid Choice! Please Try Again!")

if __name__=="__main__":
    main()




