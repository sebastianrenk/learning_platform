import sqlite3
from datetime import date, timedelta
from contextlib import closing


def initialize_database():

    with closing(sqlite3.connect("database/learning.db")) as connection:
        with connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS activities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    subject TEXT NOT NULL CHECK (length(trim(subject)) > 0),
                    topic TEXT NOT NULL CHECK (length(trim(topic)) > 0),
                    duration INTEGER NOT NULL CHECK (duration > 0),
                    date TEXT NOT NULL
                )    
            """)


def insert_activity(subject, topic, duration, date):

    with closing(sqlite3.connect("database/learning.db")) as connection:
        with connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO activities (subject, topic, duration, date) VALUES (?, ?, ?, ?)",
                (subject, topic, duration, date)
            )

            new_id = cursor.lastrowid

    return new_id


def get_activities():

    with closing(sqlite3.connect("database/learning.db")) as connection:
        with connection:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM activities " 
                "ORDER BY date DESC;"
            )

            results = cursor.fetchall()

    return results


def get_activities_by_subject(subject):

    with closing(sqlite3.connect("database/learning.db")) as connection:
        with connection:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM activities "
                "WHERE subject = ? " 
                "ORDER BY date DESC;",
                (subject,)
            )

            results = cursor.fetchall()

    return results


def update_activity(id, subject, topic, duration, date):

    with closing(sqlite3.connect("database/learning.db")) as connection:
        with connection:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE activities "
                "SET subject = ?, "
                "topic = ?, "
                "duration = ?, "
                "date = ? "
                "WHERE id = ?;",
                (subject, topic, duration, date, id)
            )

            affected = cursor.rowcount

    return affected > 0


def delete_activity(id):

    with closing(sqlite3.connect("database/learning.db")) as connection:
        with connection:
            cursor = connection.cursor()
            cursor.execute(
                "DELETE FROM activities "
                "WHERE id = ?;",
                (id,)
            )

            affected = cursor.rowcount

    return affected > 0


def get_total_learning_time():

    with closing(sqlite3.connect("database/learning.db")) as connection:
        with connection:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT COALESCE(SUM(duration), 0) "
                "FROM activities;"
            )

            result = cursor.fetchone()

    return result[0]


def get_learning_time_by_subject(subject):

    with closing(sqlite3.connect("database/learning.db")) as connection:
        with connection:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT COALESCE(SUM(duration), 0) "
                "FROM activities "
                "WHERE subject = ?;",
                (subject,)
            )

            result = cursor.fetchone()

    return result[0]


def get_subjects():

    with closing(sqlite3.connect("database/learning.db")) as connection:
        with connection:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT DISTINCT subject "
                "FROM activities;"
            )

            results = cursor.fetchall()

    return [row[0] for row in results]


def get_weekly_statistics():

    today = date.today()
    monday = today - timedelta(days=today.weekday())
    next_monday = monday + timedelta(days=7)

    start_date = monday.isoformat()
    end_date = next_monday.isoformat()

    with closing(sqlite3.connect("database/learning.db")) as connection:
        with connection:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT COALESCE(SUM(duration), 0), COUNT(*) "
                "FROM activities "
                "WHERE date >= ? AND date < ?;",
                (start_date, end_date)
            )

            result = cursor.fetchone()

    return result