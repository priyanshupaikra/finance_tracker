# 💰 Personal Finance Tracker (Command-Line Application)

A Python-based command-line application to help users manage their personal finances by tracking income, expenses, setting budgets, and generating financial reports.

---

## 📦 Features

### 🔐 User Authentication
- User registration and login with password hashing
- Data stored securely using SQLite

### 💵 Income & Expense Tracking
- Add, view, and delete transactions
- Categorize each transaction (e.g., Food, Rent, Salary)
- Auto-records transaction dates

### 📊 Financial Reporting
- Monthly and yearly reports
- Calculates total income, expenses, and net savings

### 💰 Budgeting
- Set monthly budgets for each category
- Real-time warnings if budget limits are exceeded
- Optional: Strict budget enforcement (blocks over-budget expenses)

### 📁 CSV Export
- Export all transactions to a CSV file
- Useful for backup or analysis

---

## 🛠 Tech Stack

- **Python 3**
- **SQLite3**
- `hashlib` for password hashing
- `datetime`, `csv` modules for reports

---

## 🧪 How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/finance-tracker-cli.git
   cd finance-tracker-cli

📂 File Structure
finance-tracker-cli/
├── auth.py                # Registration & login logic
├── db.py                  # Database table creation
├── tracker.py             # Transaction logic & reports
├── main.py                # Main menu / CLI dashboard
└── finance.db             # Auto-created SQLite database

🔐 Security Note
All passwords are hashed before storing in the database.
Use getpass for secure password entry in future improvements.

🚀 Future Improvements
Add a graphical interface (Tkinter/Streamlit)
Graphs and pie charts (matplotlib, seaborn)
Cloud backup with Firebase or Google Sheets
Login session tokens

🧑‍💻 Author
Your Name
Python Developer Intern
LinkedIn | GitHub