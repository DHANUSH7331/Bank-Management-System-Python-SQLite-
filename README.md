Bank Management System (Python + SQLite)

A Command Line Interface (CLI) based Bank Management System developed using Python and SQLite.
This project simulates core banking operations such as account creation, deposit, withdrawal, balance inquiry, and fund transfer.

📌 Project Overview

This application is designed to demonstrate:

Database connectivity using SQLite

CRUD operations

Transaction handling

Input validation

Modular Python programming

CLI-based interaction

It is suitable for beginners learning backend logic and database integration.

🚀 Features

🆕 Create New Bank Account

💰 Deposit Money

💸 Withdraw Money

🔄 Transfer Funds Between Accounts

📊 Check Account Balance

🗑 Delete Account

🔐 Secure Login (if implemented)

🗄 Persistent Data Storage using SQLite

🛠 Technologies Used

Python 3

SQLite3

Command Line Interface (CLI)

SQL Queries

📂 Project Structure
Bank-Management-System/
│
├── main.py
├── database.db
├── requirements.txt (if any)
└── README.md
🧠 How It Works

The program connects to a local SQLite database.

If the database or table does not exist, it creates one.

Users interact through a CLI menu.

SQL queries perform operations like:

INSERT (Create Account)

SELECT (Check Balance)

UPDATE (Deposit/Withdraw)

DELETE (Remove Account)

All changes are committed to the database.

▶️ How to Run the Project
Step 1: Clone the Repository
git clone https://github.com/your-username/Bank-Management-System.git
cd Bank-Management-System
Step 2: Run the Program
python main.py
📸 Sample Menu
1. Create Account
2. Deposit
3. Withdraw
4. Transfer
5. Check Balance
6. Delete Account
7. Exit
📊 Database Schema
Field Name	Type
Acc_num	TEXT
Name	TEXT
Age	INTEGER
Balance	REAL
🎯 Learning Outcomes

Practical understanding of SQL operations

Handling real-world logic like balance validation

Implementing transaction management

Working with relational databases

Writing clean modular Python code

🔮 Future Enhancements

GUI using Tkinter or Web Interface

User Authentication with Password Encryption

Admin Dashboard

Transaction History

REST API Integration

🤝 Contributing

Feel free to fork this repository and enhance the features.

📧 Contact

If you found this project helpful, feel free to connect with me:

GitHub: https://github.com/your-username

LinkedIn: https://linkedin.com/in/your-profile
