import sqlite3
from datetime import datetime

def create_database():
    conn = sqlite3.connect("resume_analyzer.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            resume_name TEXT,
            ats_score REAL,
            similarity_score REAL,
            analysis_date TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_report(
        resume_name,
        ats_score,
        similarity_score):
    conn = sqlite3.connect("resume_analyzer.db")
    cursor = conn.cursor()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO reports
        (
            resume_name,
            ats_score,
            similarity_score,
            analysis_date
        )
        VALUES (?, ?, ?, ?)
    """, (resume_name, ats_score, similarity_score, current_date))
    conn.commit()
    conn.close()


def get_reports():
    conn = sqlite3.connect("resume_analyzer.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reports ORDER BY id DESC")
    reports = cursor.fetchall()
    conn.close()
    return reports

def search_report(resume_name):
    conn = sqlite3.connect("resume_analyzer.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM reports WHERE resume_name LIKE ?""", ('%' + resume_name + '%',))
    reports = cursor.fetchall()
    conn.close()
    return reports

def delete_report(report_id):
    conn = sqlite3.connect("resume_analyzer.db")
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM reports WHERE id = ?""", (report_id,))
    conn.commit()
    conn.close()