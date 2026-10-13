CodeAlpha Secure Coding Review

SQL Injection Detection and Prevention Using Python

Project Overview

This project demonstrates SQL Injection (SQLi), a common application security vulnerability, and shows how to prevent it using parameterized SQL queries in Python.

The project contains two applications:

- "vulnerable_app.py" — Demonstrates an intentionally vulnerable login system.
- "secure_app.py" — Implements parameterized SQL queries to prevent the demonstrated SQL injection attack.

The project was developed as part of my CodeAlpha Cybersecurity Internship learning experience.

Objectives

- Understand how SQL Injection works.
- Identify insecure SQL query construction.
- Demonstrate the security impact of manipulated SQL input.
- Implement parameterized SQL queries.
- Compare vulnerable and secure application behavior.
- Document security findings and remediation.

Technologies Used

- Python 3
- SQLite
- SQL
- Git and GitHub

Project Structure

CodeAlpha_SecureCodingReview/
├── vulnerable_app.py
├── secure_app.py
├── security_review.md
├── README.md
├── requirements.txt
└── .gitignore

How It Works

1. Vulnerable Application

The vulnerable application directly concatenates user input into an SQL query.

This allows specially crafted input to change the intended query logic and potentially bypass the login check.

2. Secure Application

The secure application uses parameterized SQL queries.

Example:

query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))

Parameterized queries separate SQL instructions from user-supplied values, preventing the demonstrated SQL injection attack.

Sample Credentials

The applications use a temporary in-memory SQLite database with sample accounts.

Username| Password
kavi| demo123
admin| admin123

These credentials are for local educational testing only.

Installation and Execution

Requirements

- Python 3 installed on your computer.
- A terminal or command prompt.

No third-party Python packages are required for the current implementation because it uses Python's built-in "sqlite3" module.

Run the Vulnerable Application

python vulnerable_app.py

Run the Secure Application

python secure_app.py

Follow the terminal prompts to enter the username and password.

Security Testing

The following tests were performed against the local applications:

Test| Vulnerable Application| Secure Application
Valid credentials| Login successful| Login successful
Invalid credentials| Login failed| Login failed
SQL injection attempt| Login successful| Login failed

The results demonstrate how parameterized SQL queries prevent the tested SQL injection attack.

Security Recommendations

- Use parameterized SQL queries.
- Store passwords using secure password-hashing algorithms.
- Apply least-privilege database permissions.
- Avoid exposing internal database errors.
- Conduct security testing before deployment.

Note: This project is an educational demonstration, not a production-ready authentication system. It uses sample credentials and an in-memory database.

Documentation

See ""security_review.md"" (security_review.md) for the vulnerability analysis, testing results, impact assessment, remediation, and additional security recommendations.

Learning Outcomes

Through this project, I gained practical experience in:

- Understanding SQL Injection.
- Identifying insecure SQL queries.
- Implementing parameterized queries.
- Comparing vulnerable and secure application behavior.
- Documenting security findings.
- Applying secure coding principles.

Author

Kavi
B.Sc. Computer Science with Cybersecurity

Disclaimer

This project was created for educational purposes. All demonstrations were performed against a locally controlled application.