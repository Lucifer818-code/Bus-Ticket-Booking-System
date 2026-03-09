from database_helper import db_connect

class Admin:
    def __init__(self):
        self.db = db_connect()

    def adminRegistration(self):
        print("\n--- Admin Registration ---")
        user = input("Enter a UserName: ")
        pwd = input("Enter a Password: ")
        try:
            query = "INSERT INTO admins (username, password) VALUES (%s, %s)"
            self.db.execute_query(query, (user, pwd))
            print("Registration Successful!")
        except:
            print("Username already exists!")

    def adminlogin(self):
        print("\n--- Admin Login ---")
        user = input("Enter a UserName: ")
        pwd = input("Enter a Password: ")
        query = "SELECT * FROM admins WHERE username = %s AND password = %s"
        result = self.db.execute_query(query, (user, pwd))
        if result:
            print("Login Successfully!!")
            return True
        print("Invalid credentials!")
        return False