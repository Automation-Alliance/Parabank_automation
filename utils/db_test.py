from utils.db_utils import DatabaseManager

db = DatabaseManager()

db.insert_user("admin1234", "admin1234")

print("User Inserted Successfully")

user = db.get_user()

print(user)

db.close_connection()
