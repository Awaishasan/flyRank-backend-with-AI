from app.database.db import get_connection


class PostgresRepository:

    def get_all_tasks(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks")

        rows = cursor.fetchall()

        conn.close()

        return rows