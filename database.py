
import sqlite3

DATABASE = "students.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            course TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)

    connection.commit()
    connection.close()


def get_all_students():
    connection = get_connection()

    students = connection.execute(
        "SELECT * FROM students ORDER BY id"
    ).fetchall()

    connection.close()

    return [dict(student) for student in students]


def get_student(student_id):
    connection = get_connection()

    student = connection.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    connection.close()

    return dict(student) if student else None


def add_student(name, course, email):
    connection = get_connection()

    cursor = connection.execute(
        "INSERT INTO students (name, course, email) VALUES (?, ?, ?)",
        (name, course, email)
    )

    connection.commit()
    student_id = cursor.lastrowid
    connection.close()

    return get_student(student_id)


def update_student(student_id, name, course, email):
    connection = get_connection()

    cursor = connection.execute(
        """
        UPDATE students
        SET name = ?, course = ?, email = ?
        WHERE id = ?
        """,
        (name, course, email, student_id)
    )

    connection.commit()
    updated = cursor.rowcount > 0
    connection.close()

    return get_student(student_id) if updated else None


def delete_student(student_id):
    connection = get_connection()

    cursor = connection.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    connection.commit()
    deleted = cursor.rowcount > 0
    connection.close()

    return deleted
