from utils.db_utils import DatabaseManager

db = DatabaseManager()

db.insert_user("admin123", "admin123")

print("User Inserted Successfully")

user = db.get_user()

print(user)

db.close_connection()
