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
MIT License

Copyright (c) 2025 Priyanshu Paikra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
