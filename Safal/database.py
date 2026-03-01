import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("students.db")
        self.cursor = self.conn.cursor()
        self.create_table()
        self.create_users_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            contact TEXT,
            stream TEXT,
            percentage REAL,
            grade TEXT,
            interests TEXT,
            skills TEXT
        )''')
        self.conn.commit()
        self._migrate_students_table()

    def _migrate_students_table(self):
        self.cursor.execute("PRAGMA table_info(students)")
        columns = [col[1] for col in self.cursor.fetchall()]
        if "achievements" not in columns:
            return

        self.cursor.execute('''CREATE TABLE students_new (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            contact TEXT,
            stream TEXT,
            percentage REAL,
            grade TEXT,
            interests TEXT,
            skills TEXT
        )''')
        self.cursor.execute('''INSERT INTO students_new (
            id, name, age, gender, contact, stream, percentage, grade, interests, skills
        )
        SELECT id, name, age, gender, contact, stream, percentage, grade, interests, skills
        FROM students''')
        self.cursor.execute("DROP TABLE students")
        self.cursor.execute("ALTER TABLE students_new RENAME TO students")
        self.conn.commit()

    def insert_student(self, name, age, gender, contact, stream, percentage, grade, interests, skills):
        self.cursor.execute('''INSERT INTO students (name, age, gender, contact, stream, percentage, grade, interests, skills)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (name, age, gender, contact, stream, percentage, grade, interests, skills))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_all_students(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def delete_student(self, student_id):
        self.cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        self.conn.commit()
        return self.cursor.rowcount

    def create_users_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password_hash TEXT,
            is_admin INTEGER DEFAULT 0
        )''')
        self.conn.commit()

    def add_user(self, username, password_hash, is_admin=0):
        try:
            self.cursor.execute('''INSERT INTO users (username, password_hash, is_admin) VALUES (?, ?, ?)''',
                                (username, password_hash, is_admin))
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception:
            return None

    def get_user(self, username):
        self.cursor.execute("SELECT id, username, password_hash, is_admin FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def user_exists(self, username):
        return self.get_user(username) is not None
