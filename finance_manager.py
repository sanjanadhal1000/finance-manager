# # 1. User Registration and Login

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

# # 2. Add Income and Expense

# import sqlite3
# from datetime import datetime

# def connect_db():
#     connection = sqlite3.connect("data/finance.db")
#     cursor = connection.cursor()

#     # Create Users Table
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users(
#                    id INTEGER PRIMARY KEY AUTOINCREMENT,
#                    username TEXT UNIQUE,
#                    password TEXT
#                    )
#                    """)
    
#     # Create Transactions Table
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS transactions(
#                    id INTEGER PRIMARY KEY AUTOINCREMENT,
#                    user_id INTEGER,
#                    type TEXT,
#                    amount REAL,
#                    category TEXT,
#                    date TEXT,
#                    note TEXT,
#                    FOREIGN KEY (user_id) REFERENCES users(id)
#                    )
#                    """)
    
#     connection.commit()
#     connection.close()

# # User Registration
# def register_user():
#     username = input("Enter a username: ")
#     password = input("Enter the password: ")

#     connection = sqlite3.connect("data/finance.db")
#     cursor = connection.cursor()

#     try:
#         cursor.execute("INSERT INTO users (username,password) VALUES (?,?)",(username,password))
#         connection.commit()
#         print("User Registered Successfully!\n")
#     except sqlite3.IntegrityError:
#         print("Username already exists! Please Try Again!")
#     finally:
#         connection.close()

# # User Login
# def login_user():
#     username = input("Enter the username: ")
#     password = input("Enter the password: ")

#     connection = sqlite3.connect("data/finance.db")
#     cursor = connection.cursor()

#     cursor.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
#     user = cursor.fetchone()
#     connection.commit()

#     if user:
#         print(f"Welcome Back, {username}!\n")
#         return user[0]                        # Returning user_id
#     else:
#         print("Invalid Credentials! Please Try Again!\n")
#         return None
    
# # Add Income
# def add_income(user_id):
#     amount = float(input("Enter Amount: "))
#     category = input("Enter Category: ")
#     note = input("Add a short note (optional): ")
#     date = datetime.now().strftime("%Y-%m-%d")

#     connection = sqlite3.connect("data/finance.db")
#     cursor = connection.cursor()

#     cursor.execute("""INSERT INTO transactions (user_id,type,amount,category,note,date) 
#                    VALUES (?,'income',?,?,?,?)""",
#                    (user_id,amount,category,note,date))
    
#     connection.commit()
#     connection.close()

#     print("Income Added Successfully!\n")

# # Add Expense
# def add_expense(user_id):
#     amount = float(input("Enter expense amount: "))
#     category = input("Enter expense category (e.g., Food, Travel, Shopping): ")
#     note = input("Add a short note (optional): ")
#     date = datetime.now().strftime("%Y-%m-%d")

#     connection = sqlite3.connect("data/finance.db")
#     cursor = connection.cursor()

#     cursor.execute("""INSERT INTO transactions (user_id, type, amount, category, date, note)
#                       VALUES (?, 'expense', ?, ?, ?, ?)""",
#                    (user_id, amount, category, date, note))

#     connection.commit()
#     connection.close()
#     print("Expense added successfully!\n")

# # View Transactions
# def view_transactions(user_id):
#     connection = sqlite3.connect("data/finance.db")
#     cursor = connection.cursor()

#     cursor.execute("SELECT type, amount, category, date, note FROM transactions WHERE user_id=?", (user_id,))
#     rows = cursor.fetchall()
#     connection.close()

#     if not rows:
#         print("No transactions found.\n")
#         return

#     print("\nTransaction History:")
#     for t in rows:
#         print(f"{t[3]} | {t[0].capitalize()} | Rs.{t[1]} | {t[2]} | Note: {t[4]}")
#     print()

# # Main Menu
# def main():
#     connect_db()
#     print("--- Welcome to Personal Finance Manager---\n")

#     while True:
#         print("1. Register")
#         print("2. Login")
#         print("3. Exit")

#         choice = input("Enter a choice (1-3): ")

#         if choice=="1":
#             register_user()
#         elif choice=="2":
#             user_id = login_user()
#             if user_id:
#                 while True:
#                     print("\n---Menu---")
#                     print("1. Add Income")
#                     print("2. Add Expense")
#                     print("3. View Transactions")
#                     print("4. Logout")

#                     ch = input("Enter your choice (1-4): ")

#                     if ch=="1":
#                         add_income(user_id)
#                     elif ch=="2":
#                         add_expense(user_id)
#                     elif ch=="3":
#                         view_transactions(user_id)
#                     elif ch=="4":
#                         print("User logged out!\n")
#                         break
#                     else:
#                         print("Invalid Choice! Try Again!\n")

#         elif choice=="3":
#             print("Thank you for using the Personal Finance Manager! Hope to See You Again!")
#             break
#         else:
#             print("Invalid Choice! Please Try Again!")

# if __name__=="__main__":
#     main()

# # 3. Reporting System
# import sqlite3
# from datetime import datetime

# class FinanceManager:
#     def __init__(self, db_name="data/finance.db"):
#         self.db_name = db_name
#         self.connection = sqlite3.connect(self.db_name)
#         self.cursor = self.connection.cursor()
#         self.create_tables()

#     def create_tables(self):
#         """Creates tables if they don't exist."""
#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                                 username TEXT UNIQUE NOT NULL,
#                                 password TEXT NOT NULL
#                             )''')

#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
#                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                                 user_id INTEGER,
#                                 type TEXT,
#                                 amount REAL,
#                                 category TEXT,
#                                 note TEXT,
#                                 date TEXT,
#                                 FOREIGN KEY (user_id) REFERENCES users(id)
#                             )''')

#         self.connection.commit()

#     # =====================================================
#     # User registration and login
#     # =====================================================
#     def register_user(self):
#         """Register a new user."""
#         username = input("Enter username: ")
#         password = input("Enter password: ")
#         try:
#             self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
#             self.connection.commit()
#             print("Registration successful!\n")
#         except sqlite3.IntegrityError:
#             print("Username already exists. Try a different one.\n")

#     def login_user(self):
#         """Login existing user."""
#         username = input("Enter username: ")
#         password = input("Enter password: ")
#         self.cursor.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
#         result = self.cursor.fetchone()
#         if result:
#             print(f"Welcome, {username}!\n")
#             return result[0]  # user_id
#         else:
#             print("Invalid username or password.\n")
#             return None

#     # =====================================================
#     # Add income and expense
#     # =====================================================
#     def add_income(self, user_id):
#         """Adds an income record."""
#         amount = float(input("Enter income amount: "))
#         category = input("Enter income category (e.g., Salary, Gift): ")
#         note = input("Add note (optional): ")
#         date = datetime.now().strftime("%Y-%m-%d")

#         self.cursor.execute("""INSERT INTO transactions 
#                             (user_id, type, amount, category, note, date)
#                             VALUES (?, 'income', ?, ?, ?, ?)""",
#                             (user_id, amount, category, note, date))
#         self.connection.commit()
#         print("Income added successfully!\n")

#     def add_expense(self, user_id):
#         """Adds an expense record."""
#         amount = float(input("Enter expense amount: "))
#         category = input("Enter expense category (e.g., Food, Travel): ")
#         note = input("Add note (optional): ")
#         date = datetime.now().strftime("%Y-%m-%d")

#         self.cursor.execute("""INSERT INTO transactions 
#                             (user_id, type, amount, category, note, date)
#                             VALUES (?, 'expense', ?, ?, ?, ?)""",
#                             (user_id, amount, category, note, date))
#         self.connection.commit()
#         print("Expense added successfully!\n")

#     # =====================================================
#     # Reporting functionalities
#     # =====================================================
#     def show_total_balance(self, user_id):
#         """Displays the total balance (income - expenses)."""
#         self.cursor.execute("""SELECT SUM(amount) FROM transactions 
#                                WHERE user_id=? AND type='income'""", (user_id,))
#         total_income = self.cursor.fetchone()[0] or 0

#         self.cursor.execute("""SELECT SUM(amount) FROM transactions 
#                                WHERE user_id=? AND type='expense'""", (user_id,))
#         total_expense = self.cursor.fetchone()[0] or 0

#         balance = total_income - total_expense
#         print("\n----- Total Balance -----")
#         print(f"Total Income : ₹{total_income:.2f}")
#         print(f"Total Expense: ₹{total_expense:.2f}")
#         print(f"Net Balance  : ₹{balance:.2f}\n")

#     def monthly_summary(self, user_id):
#         """Shows monthly summary of income and expenses."""
#         self.cursor.execute("""
#             SELECT 
#                 strftime('%Y-%m', date) AS month,
#                 SUM(CASE WHEN type='income' THEN amount ELSE 0 END) AS total_income,
#                 SUM(CASE WHEN type='expense' THEN amount ELSE 0 END) AS total_expense
#             FROM transactions
#             WHERE user_id=?
#             GROUP BY month
#             ORDER BY month DESC
#         """, (user_id,))
#         rows = self.cursor.fetchall()

#         if not rows:
#             print("No transactions found.\n")
#             return

#         print("\n----- Monthly Summary -----")
#         for month, income, expense in rows:
#             print(f"{month}: Income ₹{income:.2f} | Expense ₹{expense:.2f} | Balance ₹{income-expense:.2f}")
#         print()

#     def close(self):
#         self.connection.close()


# # =====================================================
# # MAIN FUNCTION
# # =====================================================
# def main():
#     app = FinanceManager()

#     while True:
#         print("========== PERSONAL FINANCE MANAGER ==========")
#         print("1. Register")
#         print("2. Login")
#         print("3. Exit")
#         choice = input("Choose an option: ")

#         if choice == '1':
#             app.register_user()
#         elif choice == '2':
#             user_id = app.login_user()
#             if user_id:
#                 while True:
#                     print("\n----- MENU -----")
#                     print("1. Add Income")
#                     print("2. Add Expense")
#                     print("3. Show Total Balance")
#                     print("4. Show Monthly Summary")
#                     print("5. Logout")

#                     sub_choice = input("Choose an option: ")

#                     if sub_choice == '1':
#                         app.add_income(user_id)
#                     elif sub_choice == '2':
#                         app.add_expense(user_id)
#                     elif sub_choice == '3':
#                         app.show_total_balance(user_id)
#                     elif sub_choice == '4':
#                         app.monthly_summary(user_id)
#                     elif sub_choice == '5':
#                         print("Logged out successfully.\n")
#                         break
#                     else:
#                         print("Invalid choice, try again.\n")

#         elif choice == '3':
#             app.close()
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.\n")


# if __name__ == "__main__":
#     main()

# 4. Export into csv and json files.
# Error handling, input validation & duplicate username prevention

import json, os, csv

class FinanceManager:
    """Manage users and their financial transactions using a JSON database."""

    def __init__(self, filename="data.json"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        """Load data from a JSON file or create a new structure."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("⚠️ Data file corrupted. Starting fresh.")
        return {"users": {}}

    def save_data(self):
        """Save current data to JSON file."""
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

    # ------------------ USER MANAGEMENT ------------------
    def register_user(self, username, password):
        """Register a new user."""
        if not username.strip() or not password.strip():
            print("❌ Username/password cannot be empty.")
            return False
        if username in self.data["users"]:
            print("❌ Username already exists.")
            return False
        self.data["users"][username] = {"password": password, "transactions": []}
        self.save_data()
        print(f"✅ User {username} registered.")
        return True

    def login_user(self, username, password):
        """Login an existing user."""
        user = self.data["users"].get(username)
        if user and user["password"] == password:
            print(f"✅ Welcome, {username}!")
            return True
        print("❌ Invalid credentials.")
        return False

    # ---------------- TRANSACTION MANAGEMENT ----------------
    def add_transaction(self, username, t_type, category, amount, note, date):
        """Add a validated transaction for a user."""
        if username not in self.data["users"]:
            print("❌ User not found.")
            return False
        try:
            amount = float(amount)
            if amount <= 0:
                print("❌ Amount must be positive.")
                return False
        except ValueError:
            print("❌ Invalid amount.")
            return False
        if t_type not in ["income", "expense"]:
            print("❌ Type must be 'income' or 'expense'.")
            return False

        tx = {"type": t_type, "category": category, "amount": amount, "note": note, "date": date}
        self.data["users"][username]["transactions"].append(tx)
        self.save_data()
        print("✅ Transaction added.")
        return True

    def view_transactions(self, username):
        """Display all user transactions."""
        if username not in self.data["users"]:
            print("❌ User not found.")
            return
        txs = self.data["users"][username]["transactions"]
        if not txs:
            print("📭 No transactions yet.")
            return
        print(f"\n📋 Transactions for {username}:")
        for t in txs:
            print(f"{t['date']} | {t['type']} | {t['category']} | ₹{t['amount']} | {t['note']}")

    def export_to_csv(self, username):
        """Export all transactions for a user to a CSV file."""
        if username not in self.data["users"]:
            print("❌ User not found.")
            return False
        filename = f"{username}_transactions.csv"
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["type", "category", "amount", "note", "date"])
            writer.writeheader()
            writer.writerows(self.data["users"][username]["transactions"])
        print(f"✅ Exported to {filename}")
        return True

    def summary_report(self, username):
        """Generate income/expense summary."""
        if username not in self.data["users"]:
            print("❌ User not found.")
            return False
        txs = self.data["users"][username]["transactions"]
        income = sum(t["amount"] for t in txs if t["type"] == "income")
        expense = sum(t["amount"] for t in txs if t["type"] == "expense")
        print("\n📊 Summary:")
        print(f"Total Income: ₹{income}")
        print(f"Total Expense: ₹{expense}")
        print(f"Net Balance: ₹{income - expense}")
        return True


'''
Main Interface for Personal Finance Manager
-------------------------------------------
This script provides a console-based interface to interact with FinanceManager.
Users can register, login, add/view transactions, export data, and view reports.

Author: Sanjana Dhal
'''

def main():
    '''Main interactive loop for the finance manager program.'''
    fm = FinanceManager()
    current_user = None

    while True:
        print("\n=== 💰 Personal Finance Manager ===")
        '''Menu for Logged-out Users.'''
        if not current_user:
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                fm.register_user(username, password)

            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                if fm.login_user(username, password):
                    current_user = username

            elif choice == "3":
                print("👋 Exiting... Goodbye!")
                break

            else:
                print("❌ Invalid choice. Please try again.")

        else:
            # Menu for Logged-in Users
            print(f"\n👤 Logged in as: {current_user}")
            print("1. Add Transaction")
            print("2. View Transactions")
            print("3. Export to CSV")
            print("4. Summary Report")
            print("5. Delete Account")
            print("6. Logout")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                t_type = input("Enter type (income/expense): ")
                category = input("Enter category: ")
                amount = input("Enter amount: ")
                note = input("Enter note: ")
                date = input("Enter date (YYYY-MM-DD): ")
                fm.add_transaction(current_user, t_type, category, amount, note, date)

            elif choice == "2":
                fm.view_transactions(current_user)

            elif choice == "3":
                fm.export_to_csv(current_user)

            elif choice == "4":
                fm.summary_report(current_user)

            elif choice == "5":
                fm.delete_user(current_user)
                current_user = None

            elif choice == "6":
                print(f"👋 Logged out from {current_user}.")
                current_user = None

            else:
                print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

#     def __init__(self, db_name="data/finance.db"):
#         """Initialize and connect to SQLite database"""
#         self.db_name = db_name
#         self.connection = sqlite3.connect(self.db_name)
#         self.cursor = self.connection.cursor()
#         self.create_tables()

#     def create_tables(self):
#         """Create necessary database tables if they don't exist."""
#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                                 username TEXT UNIQUE NOT NULL,
#                                 password TEXT NOT NULL
#                             )''')

#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
#                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                                 user_id INTEGER,
#                                 type TEXT,
#                                 amount REAL,
#                                 category TEXT,
#                                 note TEXT,
#                                 date TEXT,
#                                 FOREIGN KEY (user_id) REFERENCES users(id)
#                             )''')

#         self.connection.commit()

#     # ============================
#     # Add Income
#     # ============================
#     def add_income(self, user_id):
#         """Adds an income record."""
#         amount = float(input("Enter income amount: "))
#         category = input("Enter income category (e.g., Salary, Gift): ")
#         note = input("Add note (optional): ")
#         date = datetime.now().strftime("%Y-%m-%d")

#         self.cursor.execute("""INSERT INTO transactions 
#                             (user_id, type, amount, category, note, date)
#                             VALUES (?, 'income', ?, ?, ?, ?)""",
#                             (user_id, amount, category, note, date))
#         self.connection.commit()
#         print("✅ Income added successfully!\n")

#     # ============================
#     # Add Expense
#     # ============================
#     def add_expense(self, user_id):
#         """Adds an expense record."""
#         amount = float(input("Enter expense amount: "))
#         category = input("Enter expense category (e.g., Food, Travel): ")
#         note = input("Add note (optional): ")
#         date = datetime.now().strftime("%Y-%m-%d")

#         self.cursor.execute("""INSERT INTO transactions 
#                             (user_id, type, amount, category, note, date)
#                             VALUES (?, 'expense', ?, ?, ?, ?)""",
#                             (user_id, amount, category, note, date))
#         self.connection.commit()
#         print("✅ Expense added successfully!\n")

#     # ============================
#     # Show Total Balance
#     # ============================
#     def show_total_balance(self, user_id):
#         """Displays the total balance (income - expenses)."""
#         self.cursor.execute("""SELECT SUM(amount) FROM transactions 
#                                WHERE user_id=? AND type='income'""", (user_id,))
#         total_income = self.cursor.fetchone()[0] or 0

#         self.cursor.execute("""SELECT SUM(amount) FROM transactions 
#                                WHERE user_id=? AND type='expense'""", (user_id,))
#         total_expense = self.cursor.fetchone()[0] or 0

#         balance = total_income - total_expense

#         print("\n----- 💰 Total Balance -----")
#         print(f"Total Income : ₹{total_income:.2f}")
#         print(f"Total Expense: ₹{total_expense:.2f}")
#         print(f"Net Balance  : ₹{balance:.2f}\n")

#     # ============================
#     # Monthly Summary
#     # ============================
#     def monthly_summary(self, user_id):
#         """Shows monthly summary of income and expenses."""
#         self.cursor.execute("""
#             SELECT 
#                 strftime('%Y-%m', date) AS month,
#                 SUM(CASE WHEN type='income' THEN amount ELSE 0 END) AS total_income,
#                 SUM(CASE WHEN type='expense' THEN amount ELSE 0 END) AS total_expense
#             FROM transactions
#             WHERE user_id=?
#             GROUP BY month
#             ORDER BY month DESC
#         """, (user_id,))
#         rows = self.cursor.fetchall()

#         if not rows:
#             print("No transactions found.\n")
#             return

#         print("\n----- 📅 Monthly Summary -----")
#         for month, income, expense in rows:
#             print(f"{month}: Income ₹{income:.2f} | Expense ₹{expense:.2f} | Balance ₹{income - expense:.2f}")
#         print()

#     # ============================
#     # Export Transactions 
#     # ============================
#     def export_transactions(self, user_id):
#         """Exports all user transactions to CSV and JSON files."""
#         self.cursor.execute("SELECT * FROM transactions WHERE user_id=?", (user_id,))
#         rows = self.cursor.fetchall()

#         if not rows:
#             print("No transactions to export.\n")
#             return

#         # Export to CSV
#         with open("transactions.csv", "w", newline="", encoding="utf-8") as f:
#             writer = csv.writer(f)
#             writer.writerow(["ID", "User_ID", "Type", "Amount", "Category", "Note", "Date"])
#             writer.writerows(rows)
#         print("✅ Transactions exported to 'transactions.csv'")

#         # Export to JSON
#         json_data = [
#             {
#                 "id": row[0],
#                 "user_id": row[1],
#                 "type": row[2],
#                 "amount": row[3],
#                 "category": row[4],
#                 "note": row[5],
#                 "date": row[6],
#             }
#             for row in rows
#         ]

#         with open("transactions.json", "w", encoding="utf-8") as f:
#             json.dump(json_data, f, indent=4)
#         print("✅ Transactions exported to 'transactions.json'\n")

#     # ============================
#     # Close Connection
#     # ============================
#     def close(self):
#         """Close the database connection."""
#         self.connection.close()


# # ============================
# # Main Program Loop
# # ============================
# def main():
#     fm = FinanceManager()
#     print("\nWelcome to Personal Finance Manager!")
#     user_id = int(input("Enter your user ID to continue: "))

#     while True:
#         print("""
#         1️⃣ Add Income
#         2️⃣ Add Expense
#         3️⃣ View Total Balance
#         4️⃣ View Monthly Summary
#         5️⃣ Export Transactions (CSV/JSON)
#         6️⃣ Exit
#         """)

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             fm.add_income(user_id)
#         elif choice == '2':
#             fm.add_expense(user_id)
#         elif choice == '3':
#             fm.show_total_balance(user_id)
#         elif choice == '4':
#             fm.monthly_summary(user_id)
#         elif choice == '5':
#             fm.export_transactions(user_id)
#         elif choice == '6':
#             fm.close()
#             print("👋 Goodbye!")
#             break
#         else:
#             print("❌ Invalid choice. Please try again.\n")


# if __name__ == "__main__":
#     main()


# # 5. Make the Finance Manager Programmatic (integrated into a GUI, Flask app, or automated tests).
# import sqlite3
# from datetime import datetime

# class FinanceManager:
#     def __init__(self, db_name="data/finance.db"):
#         self.db_name = db_name
#         self.connection = sqlite3.connect(self.db_name)
#         self.cursor = self.connection.cursor()
#         self.create_tables()

#     # =====================================================
#     # TABLE CREATION
#     # =====================================================
#     def create_tables(self):
#         """Create tables if they don't exist."""
#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                                 username TEXT UNIQUE NOT NULL,
#                                 password TEXT NOT NULL
#                             )''')

#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
#                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                                 user_id INTEGER,
#                                 type TEXT,
#                                 amount REAL,
#                                 category TEXT,
#                                 note TEXT,
#                                 date TEXT,
#                                 FOREIGN KEY (user_id) REFERENCES users(id)
#                             )''')
#         self.connection.commit()

#     # =====================================================
#     # USER MANAGEMENT
#     # =====================================================
#     def register_user(self, username, password):
#         """Register a new user."""
#         try:
#             self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
#             self.connection.commit()
#             return {"success": True, "message": "User registered successfully!"}
#         except sqlite3.IntegrityError:
#             return {"success": False, "message": "Username already exists."}

#     def login_user(self, username, password):
#         """Login existing user and return user_id if successful."""
#         self.cursor.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
#         result = self.cursor.fetchone()
#         if result:
#             return {"success": True, "user_id": result[0], "message": "Login successful!"}
#         else:
#             return {"success": False, "message": "Invalid username or password."}

#     # =====================================================
#     # TRANSACTIONS
#     # =====================================================
#     def add_income(self, user_id, amount, category, note="", date=None):
#         """Add an income record."""
#         date = date or datetime.now().strftime("%Y-%m-%d")
#         self.cursor.execute("""INSERT INTO transactions 
#                             (user_id, type, amount, category, note, date)
#                             VALUES (?, 'income', ?, ?, ?, ?)""",
#                             (user_id, amount, category, note, date))
#         self.connection.commit()
#         return {"success": True, "message": "Income added successfully."}

#     def add_expense(self, user_id, amount, category, note="", date=None):
#         """Add an expense record."""
#         date = date or datetime.now().strftime("%Y-%m-%d")
#         self.cursor.execute("""INSERT INTO transactions 
#                             (user_id, type, amount, category, note, date)
#                             VALUES (?, 'expense', ?, ?, ?, ?)""",
#                             (user_id, amount, category, note, date))
#         self.connection.commit()
#         return {"success": True, "message": "Expense added successfully."}

#     # =====================================================
#     # REPORTING
#     # =====================================================
#     def get_total_balance(self, user_id):
#         """Return income, expense, and balance values."""
#         self.cursor.execute("""SELECT SUM(amount) FROM transactions 
#                                WHERE user_id=? AND type='income'""", (user_id,))
#         total_income = self.cursor.fetchone()[0] or 0

#         self.cursor.execute("""SELECT SUM(amount) FROM transactions 
#                                WHERE user_id=? AND type='expense'""", (user_id,))
#         total_expense = self.cursor.fetchone()[0] or 0

#         balance = total_income - total_expense
#         return {
#             "income": total_income,
#             "expense": total_expense,
#             "balance": balance
#         }

#     def get_monthly_summary(self, user_id):
#         """Return monthly summary as a list of dictionaries."""
#         self.cursor.execute("""
#             SELECT 
#                 strftime('%Y-%m', date) AS month,
#                 SUM(CASE WHEN type='income' THEN amount ELSE 0 END) AS total_income,
#                 SUM(CASE WHEN type='expense' THEN amount ELSE 0 END) AS total_expense
#             FROM transactions
#             WHERE user_id=?
#             GROUP BY month
#             ORDER BY month DESC
#         """, (user_id,))
#         rows = self.cursor.fetchall()

#         return [
#             {"month": month, "income": income, "expense": expense, "balance": income - expense}
#             for month, income, expense in rows
#         ]

#     # =====================================================
#     # CLEANUP
#     # =====================================================
#     def close(self):
#         self.connection.close()


# # =====================================================
# # OPTIONAL: DEMO USAGE (no input)
# # =====================================================
# def main():
#     fm = FinanceManager()

#     # Register and login
#     fm.register_user("alice", "1234")
#     login_result = fm.login_user("alice", "1234")
#     user_id = login_result["user_id"]

#     # Add some data
#     fm.add_income(user_id, 5000, "Salary", "Monthly salary")
#     fm.add_expense(user_id, 1500, "Groceries")
#     fm.add_expense(user_id, 700, "Travel")

#     # Get summary
#     print("\n=== TOTAL BALANCE ===")
#     print(fm.get_total_balance(user_id))

#     print("\n=== MONTHLY SUMMARY ===")
#     for summary in fm.get_monthly_summary(user_id):
#         print(summary)

#     fm.close()


# if __name__ == "__main__":
#     main()




