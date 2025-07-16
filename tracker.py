import sqlite3
import csv
from datetime import datetime
DB_NAME = 'finance.db'

def add_transaction(user_id, trans_type, category, amount, date):
    if not check_budget_warning(user_id, trans_type, amount, category, date):
        return False

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''INSERT INTO transactions (user_id, type, amount, category, date)
                 VALUES (?, ?, ?, ?, ?)''',
              (user_id, trans_type, amount, category, date))
    conn.commit()
    conn.close()
    return True

def view_transactions(user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id, type, amount, category, date FROM transactions WHERE user_id = ?", (user_id,))
    rows = c.fetchall()
    conn.close()
    return rows

def delete_transaction(user_id, transaction_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM transactions WHERE id = ? AND user_id = ?", (transaction_id, user_id))
    conn.commit()
    conn.close()
    return True

def set_budget(user_id, category, month, amount):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''INSERT OR REPLACE INTO budgets (user_id, category, month, amount)
                 VALUES (?, ?, ?, ?)''', (user_id, category, month, amount))
    conn.commit()
    conn.close()
    return True

def export_transactions_to_csv(user_id, filename):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''SELECT date, type, category, amount
                 FROM transactions
                 WHERE user_id = ?
                 ORDER BY date ASC''', (user_id,))
    rows = c.fetchall()
    conn.close()

    if not rows:
        return False

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Type", "Category", "Amount"])
        writer.writerows(rows)

    return True

def generate_report(user_id, report_type, year, month=None):
    if report_type == "monthly" and month:
        start_date = f"{year}-{month}-01"
        end_date = f"{year}-{month}-31"
    elif report_type == "yearly":
        start_date = f"{year}-01-01"
        end_date = f"{year}-12-31"
    else:
        return {"error": "Invalid report parameters."}

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        SELECT type, SUM(amount)
        FROM transactions
        WHERE user_id = ? AND date BETWEEN ? AND ?
        GROUP BY type
    ''', (user_id, start_date, end_date))

    rows = c.fetchall()
    conn.close()

    income = 0
    expense = 0

    for row in rows:
        if row[0] == 'income':
            income = row[1]
        elif row[0] == 'expense':
            expense = row[1]

    return {
        "income": round(income, 2),
        "expense": round(expense, 2),
        "savings": round(income - expense, 2),
        "period": f"{start_date} to {end_date}"
    }

def check_budget_warning(user_id, trans_type, amount, category, date):
    if trans_type != 'expense':
        return True  

    month = date[:7]  
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''SELECT amount FROM budgets
                 WHERE user_id = ? AND category = ? AND month = ?''',
              (user_id, category, month))
    budget_row = c.fetchone()

    if not budget_row:
        return True

    budget_limit = budget_row[0]

    c.execute('''SELECT SUM(amount) FROM transactions
                 WHERE user_id = ? AND category = ? AND date LIKE ? AND type = 'expense' ''',
              (user_id, category, f'{month}-%'))
    total_spent = c.fetchone()[0] or 0

    conn.close()

    if total_spent + amount > budget_limit:
        print(f"❌ Transaction denied: This expense (₹{amount}) will exceed your ₹{budget_limit} budget for '{category}' in {month}.")
        return False
    elif total_spent + amount == budget_limit:
        print(f"⚠️ You're about to hit your exact budget for '{category}' in {month}.")
    elif total_spent + amount > (0.8 * budget_limit):
        print(f"⚠️ You’re approaching your budget limit for '{category}' ({round(total_spent + amount, 2)}/₹{budget_limit}).")

    return True



