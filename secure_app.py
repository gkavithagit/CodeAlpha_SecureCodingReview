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
    """Authenticate users using a parameterized SQL query."""
    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor = connection.cursor()

    # SECURE: Parameterized query prevents SQL injection.
    query = "SELECT * FROM users WHERE username = ? AND password = ?"

    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        print("\nLogin successful!")
        print("Welcome,", result[0])
    else:
        print("\nLogin failed. Invalid username or password.")


def main():
    connection = setup_database()

    print("=== Secure Login Application ===")
    print("For educational testing only.")
    print()

    try:
        login(connection)
    finally:
        connection.close()


if __name__ == "__main__":
    main()