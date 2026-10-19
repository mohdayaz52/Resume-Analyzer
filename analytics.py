import sqlite3
import matplotlib.pyplot as plt

def get_analytics():
    conn = sqlite3.connect("resume_analyzer.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ats_score
        FROM reports
    """)
    scores = [
        row[0]
        for row in cursor.fetchall()
    ]
    conn.close()
    return scores

def show_graph():
    conn = sqlite3.connect("resume_analyzer.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ats_score
        FROM reports
    """)
    scores = [
        row[0]
        for row in cursor.fetchall()
    ]
    conn.close()

    if not scores:
        return
    
    plt.figure(figsize=(8, 5))
    plt.plot(scores, marker="o")
    plt.title("ATS Score History")
    plt.xlabel("Analysis Number")
    plt.ylabel("ATS Score")
    plt.grid(True)
    plt.show()