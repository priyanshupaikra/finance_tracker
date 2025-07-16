# 💸 Personal Finance Tracker

A full-featured, responsive web application built with **Flask**, **SQLite**, and **Tailwind CSS** to help users manage their income, expenses, budgets, and financial reports — all in one place.

![Dashboard](static/dashboard_illustration.png)

---

## 🚀 Features

- ✅ User Registration & Login
- ➕ Add Income and Expenses
- 📋 View All Transactions
- 🗑️ Delete Transactions
- 📊 Generate Monthly and Yearly Financial Reports
- 💰 Set Monthly Budgets by Category
- 📤 Export Transactions to CSV
- 🌈 Fully Responsive UI using **Tailwind CSS**

---

## 🛠️ Tech Stack

| Frontend        | Backend     | Database   | Extras       |
|-----------------|-------------|------------|--------------|
| HTML + Tailwind | Python Flask| SQLite     | Git + GitHub |

---

## 📁 Project Structure

```
finance_tracker/
│
├── app.py                     # Flask application
├── auth.py                    # User auth functions
├── db.py                      # Table creation logic
├── tracker.py                 # Finance tracking logic
│
├── templates/                 # HTML templates
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_transaction.html
│   ├── view_transactions.html
│   ├── delete_transaction.html
│   ├── set_budget.html
│   └── report.html
│
├── static/                    # CSS/images/static assets
│   └── dashboard_illustration.png
│
└── finance.db                 # SQLite database (auto-created)
```

---

## ⚙️ How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/finance_tracker.git
   cd finance_tracker
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install flask
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. Visit [http://localhost:5000](http://localhost:5000) in your browser 🚀

---

## 🧠 Future Improvements

- Dark Mode toggle
- Pie charts for category spending
- Email CSV reports
- Cloud database support (PostgreSQL/Firebase)

---

## 🙌 Credits

- Tailwind CSS for design
- SQLite for simple embedded storage
- Icons via Emoji & Unicode ❤️

---

## 📜 License

MIT License. Use it freely, improve it endlessly. ✨
