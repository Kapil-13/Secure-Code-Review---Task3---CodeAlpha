import bcrypt
import warnings

warnings.filterwarnings("ignore")

username_db = "admin"
password_db = "admin123"  

stored_hash = bcrypt.hashpw(password_db.encode(), bcrypt.gensalt())

print("User created successfully!\n")


#LOGIN SYSTEM

MAX_ATTEMPTS = 3
attempts = 0

while attempts < MAX_ATTEMPTS:
    username = input("Enter username: ").strip()
    password = input("Enter password: ")

    if username == username_db and bcrypt.checkpw(password.encode(), stored_hash):
        print("✅ Login successful")
        break
    else:
        print("❌ Invalid credentials")

    attempts += 1
    print(f"Attempts left: {MAX_ATTEMPTS - attempts}\n")

if attempts == MAX_ATTEMPTS:
    print("🚫 Account locked")
