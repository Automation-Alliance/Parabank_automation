import mysql.connector


class DatabaseManager:

    def __init__(self):

        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="parabank_automation",
        )

        self.cursor = self.connection.cursor()

    def insert_user(self, username, password):

        query = """
        INSERT INTO users(username, password)
        VALUES (%s, %s)
        """

        values = (username, password)

        self.cursor.execute(query, values)

        self.connection.commit()

    def get_user(self):

        query = """
        SELECT username, password
        FROM users
        ORDER BY id DESC
        LIMIT 1
        """

        self.cursor.execute(query)

        return self.cursor.fetchone()

    def close_connection(self):

        self.cursor.close()
        self.connection.close()