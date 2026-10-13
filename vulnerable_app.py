import sqlite3


def setup_database():
    """Create an in-memory database with sample users."""
    connection = sqlite3.connect(":memory:")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE users (
            username TEXT,
            password TEXT
        )
    """)

    cursor.execute(
        "INSERT INTO users VALUES (?, ?)",
        ("kavi", "demo123")
    )

    cursor.execute(
        "INSERT INTO users VALUES (?, ?)",
        ("admin", "admin123")
    )

    connection.commit()

    return connection


def login(connection):
    """Demonstrate an intentionally vulnerable login."""
    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor = connection.cursor()

    # INTENTIONALLY VULNERABLE:
    # User input is directly concatenated into the SQL query.
    query = (
        "SELECT * FROM users WHERE username = '"
        + username
        + "' AND password = '"
        + password
        + "'"
    )

    print("\nExecuting SQL query:")
    print(query)

    try:
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            print("\nLogin successful!")
            print("Welcome,", result[0])
        else:
            print("\nLogin failed. Invalid username or password.")

    except sqlite3.Error as error:
        print("\nSQL error:", error)


def main():
    connection = setup_database()

    print("=== Vulnerable Login Application ===")
    print("For educational testing only.")
    print("Sample accounts:")
    print("Username: kavi | Password: demo123")
    print("Username: admin | Password: admin123")
    print()

    try:
        login(connection)
    finally:
        connection.close()


if __name__ == "__main__":
    main()