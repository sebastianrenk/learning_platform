import sqlite3


def initialize_database():

    connection = sqlite3.connect("learning.db")
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

    connection = sqlite3.connect("learning.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO activities (subject, topic, duration, date) VALUES (?, ?, ?, ?)",
        (subject, topic, duration, date)
    )

    connection.commit()
    connection.close()


def get_activities():

    connection = sqlite3.connect("learning.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM activities " 
        "ORDER BY date DESC;"
    )

    results = cursor.fetchall()
    connection.close()
    return results


def get_activities_by_subject(subject):

    connection = sqlite3.connect("learning.db")
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

    connection = sqlite3.connect("learning.db")
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

    connection.commit()
    connection.close()


def delete_activity(id):

    connection = sqlite3.connect("learning.db")
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM activities "
        "WHERE id = ?;",
        (id,)
    )

    connection.commit()
    connection.close()