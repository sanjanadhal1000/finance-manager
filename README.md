# 💰 Personal Finance Manager

A **command-line Personal Finance Manager** built using Python.  
It helps users **track income, expenses, generate reports, and export data** — all through a simple and interactive text-based interface.

---

## 👩‍💻 Author
**Name:** Sanjana Dhal  
**Project Duration:** 1 month  
**Repository:** [github.com/sanjanadhal1000/finance-manager](https://github.com/sanjanadhal1000/finance-manager)

---

## 🚀 Features

✅ Register and login with username & password  
✅ Add income and expense transactions  
✅ View and manage all transactions  
✅ Generate monthly summaries and balance reports  
✅ Export data to CSV or JSON  
✅ Input validation and error handling  
✅ Clean, simple, menu-based CLI interface  

---

## 🗂️ Project Structure

finance-manager/
│
├── finance_manager.py # Main program file (CLI interface)
├── db.py # Database connection and setup (if used)
├── models.py # Classes for users and transactions
├── utils.py # Helper functions (CSV/JSON export, validation)
├── tests/ # Unit tests for functions
├── README.md # Documentation
├── requirements.txt # Dependencies list
└── .gitignore # Files to ignore (DB, cache, etc.)


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/sanjanadhal1000/finance-manager
cd finance-manager

2️⃣ (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate   # macOS/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
python finance_manager.py

🖥️ Preview

Main Menu (before login):

=== 💰 Personal Finance Manager ===
1. Register
2. Login
3. Exit


After login:

👤 Logged in as: sanjanadhal1000
1. Add Transaction
2. View Transactions
3. Export to CSV
4. Summary Report
5. Delete Account
6. Logout


Example Run:

Enter type (income/expense): income
Enter category: Salary
Enter amount: 2000
Enter note: September Salary
Enter date (YYYY-MM-DD): 2025-09-30
✅ Transaction added successfully!

🧪 Testing

To run all unit tests:

python -m unittest discover tests

📘 What I Learned

Managing data persistence using JSON and file handling

Writing clean, modular, and documented Python code

Implementing input validation and user error handling

Designing a structured CLI workflow

Writing unit tests for critical functions

🪪 License

This project is open-source and available under the MIT License.

🌟 Acknowledgements

Special thanks to open-source Python documentation and resources that helped in building this project.

Final Commit:
Day 30 — Final Submission: Added README, documentation, and project summary

