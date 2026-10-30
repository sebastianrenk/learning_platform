import sqlite3
from datetime import date, timedelta


def initialize_database():

    connection = sqlite3.connect("database/learning.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            topic TEXT NOT NULL,
            duration INTEGER NOT NULL,
            date TEXT NOT NULL
        )    
    """)

    connection.commit()
    connection.close()


def insert_activity(subject, topic, duration, date):

    connection = sqlite3.connect("database/learning.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO activities (subject, topic, duration, date) VALUES (?, ?, ?, ?)",
        (subject, topic, duration, date)
    )

    connection.commit()
    connection.close()


def get_activities():

    connection = sqlite3.connect("database/learning.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM activities " 
        "ORDER BY date DESC;"
    )

    results = cursor.fetchall()
    connection.close()
    
    return results


def get_activities_by_subject(subject):

    connection = sqlite3.connect("database/learning.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM activities "
        "WHERE subject = ? " 
        "ORDER BY date DESC;",
        (subject,)
    )

    results = cursor.fetchall()
    connection.close()

    return results


def update_activity(id, subject, topic, duration, date):

    connection = sqlite3.connect("database/learning.db")
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
    connection.commit()
    connection.close()

    return affected


def delete_activity(id):

    connection = sqlite3.connect("database/learning.db")
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM activities "
        "WHERE id = ?;",
        (id,)
    )

    affected = cursor.rowcount
    connection.commit()
    connection.close()

    return affected


def get_total_learning_time():

    connection = sqlite3.connect("database/learning.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT SUM(duration) "
        "FROM activities;"
    )

    result = cursor.fetchone()
    connection.close()

    return result[0] if result[0] is not None else 0


def get_learning_time_by_subject(subject):

    connection = sqlite3.connect("database/learning.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT SUM(duration) "
        "FROM activities "
        "WHERE subject = ?;",
        (subject,)
    )

    result = cursor.fetchone()
    connection.close()

    return result[0] if result[0] is not None else 0


def get_subjects():

    connection = sqlite3.connect("database/learning.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT DISTINCT subject "
        "FROM activities;"
    )

    results = cursor.fetchall()
    connection.close()

    return [row[0] for row in results]


def get_weekly_statistics():

    today = date.today()
    monday = today - timedelta(days=today.weekday())
    next_monday = monday + timedelta(days=7)

    start_date = monday.isoformat()
    end_date = next_monday.isoformat()

    connection = sqlite3.connect("database/learning.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT SUM(duration), COUNT(*) "
        "FROM activities "
        "WHERE date >= ? AND date < ?;",
        (start_date, end_date)
    )

    result = cursor.fetchone()
    connection.close()

    return result