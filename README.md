# finance-manager
Build a Complete Personal Finance Manager with data persistence, reporting, and multiple user features.
# 💰 Personal Finance Manager

A **command-line Personal Finance Manager** built using Python and SQLite.  
It helps users track income, expenses, generate reports, and export data — all through a simple text-based interface.

---

## 👩‍💻 Author
**Name:** Sanjana Dhal  
**Project Duration:** 1 month
**Repository:** https://github.com/sanjanadhal1000/finance-manager

---

## 🚀 Features
✅ Register and login with username & password  
✅ Add income and expenses  
✅ View and manage all transactions  
✅ Generate monthly summaries and balance reports  
✅ Export transactions to CSV or JSON  
✅ Input validation and error handling  
✅ Simple, clean, menu-based interface  

---

## 🗂️ Project Structure

finance-manager/
│
├── finance_manager.py # main program file (CLI)
├── db.py # database connection and table creation
├── models.py # user & expense management classes
├── utils.py # helper functions (e.g. export to CSV/JSON)
├── README.md # documentation
├── requirements.txt # dependencies list (can be empty)
├── .gitignore # ignored files like db and cache
└── tests/ # optional test folder


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/sanjanadhal1000/finance-manager.git
cd finance-manager

### 2️⃣ Create a virtual environment (optional)
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate   # macOS/Linux

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Run the application
python finance_manager.py


