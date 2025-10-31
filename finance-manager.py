import sqlite3
connection = sqlite3.connect("data/finance.db")

import sqlite3
import os

DB_PATH = "data/finance.db"

# ✅ Create database and users table if not exists
def setup_database():
    os.makedirs("data", exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            email TEXT,
            password TEXT
        )
    """)

    connection.commit()
    connection.close()


# ✅ Register new user
def register_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, password)
        )
        connection.commit()
        print("\n✅ Registration successful!\n")
    except sqlite3.IntegrityError:
        print("\n⚠️ Username already exists! Try a different one.\n")
    finally:
        connection.close()


# ✅ Login existing user
def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )

    user = cursor.fetchone()
    connection.close()

    if user:
        print(f"\n✅ Welcome back, {username}!\n")
        return True
    else:
        print("\n❌ Invalid credentials. Please try again.\n")
        return False


# ✅ Main Menu
def main():
    setup_database()

    while True:
        print("==== Finance Manager ====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice (1-3): ")

        if choice == "1":
            register_user()
        elif choice == "2":
            if login_user():
                print("You can now access your finance features.\n")
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()


