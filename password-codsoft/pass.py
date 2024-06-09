import sqlite3
import hashlib

class PasswordManager:
    def __init__(self):
        self.conn = sqlite3.connect("passwords.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS passwords
                               (id INTEGER PRIMARY KEY, 
                               website TEXT NOT NULL,
                               username TEXT NOT NULL,
                               password TEXT NOT NULL)''')
        self.conn.commit()

    def hash_password(self, password):
        # Hash the password using SHA-256 algorithm
        return hashlib.sha256(password.encode()).hexdigest()

    def add_password(self, website, username, password):
        # Hash the password before storing
        hashed_password = self.hash_password(password)
        self.cursor.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
                            (website, username, hashed_password))
        self.conn.commit()
        print("Password added successfully!")

    def get_password(self, website, username):
        self.cursor.execute("SELECT password FROM passwords WHERE website=? AND username=?",
                            (website, username))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def close_connection(self):
        self.conn.close()

if __name__ == "__main__":
    password_manager = PasswordManager()

    while True:
        print("\n1. Add Password")
        print("2. Get Password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            password_manager.add_password(website, username, password)
        elif choice == "2":
            website = input("Enter website: ")
            username = input("Enter username: ")
            stored_password = password_manager.get_password(website, username)
            if stored_password:
                print(f"Stored password for {website} and username {username} is: {stored_password}")
            else:
                print("No password found for the provided website and username.")
        elif choice == "3":
            password_manager.close_connection()
            break
        else:
            print("Invalid choice! Please choose again.")
        