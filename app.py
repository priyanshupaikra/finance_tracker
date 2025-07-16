from flask import Flask, render_template, request, redirect, session, url_for, flash, send_file
from auth import create_users_table, register_user, login_user
from db import create_transactions_table, create_budget_table
from tracker import (
    add_transaction, view_transactions, delete_transaction,
    generate_report, set_budget, export_transactions_to_csv
)
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

create_users_table()
create_transactions_table()
create_budget_table()

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = login_user(request.form['username'], request.form['password'])
        if user:
            session['user'] = user[0]
            session['username'] = user[1]
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials", "danger")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if register_user(request.form['username'], request.form['password']):
            flash("Registered successfully!", "success")
            return redirect(url_for('login'))
        else:
            flash("Username already exists", "danger")
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        add_transaction(session['user'],
                        request.form['type'],
                        request.form['category'],
                        float(request.form['amount']),
                        request.form['date'])
        flash("Transaction added!", "success")
        return redirect(url_for('transactions'))
    return render_template('add_transaction.html')

@app.route('/transactions')
def transactions():
    data = view_transactions(session['user'])
    return render_template('view_transactions.html', transactions=data)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    data = view_transactions(session['user'])
    if request.method == 'POST':
        transaction_id = int(request.form['transaction_id'])
        delete_transaction(session['user'], transaction_id)
        flash("Transaction deleted!", "success")
        return redirect(url_for('transactions'))
    return render_template('delete_transaction.html', transactions=data)

@app.route('/report', methods=['GET', 'POST'])
def report():
    report_data = None
    if request.method == 'POST':
        year = request.form['year']
        month = request.form.get('month')
        if month:
            report_data = generate_report(session['user'], report_type="monthly", year=year, month=month)
        else:
            report_data = generate_report(session['user'], report_type="yearly", year=year)
    return render_template('report.html', report=report_data)

@app.route('/budget', methods=['GET', 'POST'])
def budget():
    if request.method == 'POST':
        category = request.form['category']
        month = request.form['month']
        amount = float(request.form['amount'])
        set_budget(session['user'], category, month, amount)
        flash("Budget saved successfully!", "success")
        return redirect(url_for('dashboard'))
    return render_template('set_budget.html')

@app.route('/export')
def export():
    filename = f"transactions_{session['username']}.csv"
    export_transactions_to_csv(session['user'], filename)
    file_path = os.path.abspath(filename)
    return send_file(file_path, as_attachment=True)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
