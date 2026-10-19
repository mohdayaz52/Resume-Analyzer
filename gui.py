import tkinter as tk
from tkinter import filedialog
from resume_reader import extract_text
from skill_matcher import find_skills
from ats_score import calculate_score
from similarity import calculate_similarity
from suggestions import generate_suggestions
from database import create_database, save_report, get_reports, search_report, delete_report
from jd_reader import extract_jd_text
from report_generator import generate_pdf
from datetime import datetime
from rating import get_resume_rating
from analytics import get_analytics, show_graph

create_database()

last_score = 0
last_similarity = 0
last_missing = []
last_suggestions = []

def browse_resume():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    resume_entry.delete(0, tk.END)
    resume_entry.insert(0, file_path)

def browse_jd():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    jd_entry.delete(0, tk.END)
    jd_entry.insert(0, file_path)

def show_reports():
    reports = get_reports()
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Previous Reports:\n\n") 
    for report in reports:
        result_text.insert(tk.END, f"ID:{report[0]}\n")
        result_text.insert(tk.END, f"Resume:{report[1]}\n")
        result_text.insert(tk.END, f"ATS Score:{report[2]:.2f}%\n")
        result_text.insert(tk.END, f"Similarity:{report[3]:.2f}%\n")
        result_text.insert(tk.END, f"Analysis Date:{report[4]}\n")
        result_text.insert(tk.END, f"{'-'*40}\n\n")


def analyze_resume():
    global last_score
    global last_similarity
    global last_missing
    global last_suggestions
    resume_path = resume_entry.get()
    resume_text = extract_text(resume_path)
    resume_skills = find_skills(resume_text)
    jd_path = jd_entry.get()
    jd_text = extract_jd_text(jd_path)
    jd_skills = find_skills(jd_text)
    score, matched = calculate_score(resume_skills, jd_skills)
    rating = get_resume_rating(score)
    similarity_score = calculate_similarity(resume_text, jd_text)
    analysis_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # missing = []
    # for skill in jd_skills:
    #     if skill not in matched:
    #         missing.append(skill)
    missing = list(set(jd_skills) - set(matched))

    suggestions = generate_suggestions(missing)

    last_score = score
    last_similarity = similarity_score
    last_missing = missing
    last_suggestions = suggestions

    save_report(resume_path,score,similarity_score)

    result = (
        f"Analysis Date: {analysis_time}\n"
        f"ATS Score: {score:.2f}%\n\n"
        f"Similarity: {similarity_score:.2f}%\n\n"
        f"Rating: {rating}\n\n"
        f"Missing Skills:\n"
        + "\n".join(missing)
        + "\n\nSuggestions:\n"
        + "\n".join(suggestions)
    )
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)


def export_pdf():
    generate_pdf(last_score, last_similarity, last_missing, last_suggestions)
    result_text.insert(tk.END, "\n\nPDF Report Exported Successfully!")


def show_analytics():
    scores = get_analytics()
    if not scores:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "No Reports Found")
        return 
    average_score = (sum(scores) / len(scores))
    highest_score = max(scores)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"Total Reports: {len(scores)}\n\n")
    result_text.insert(tk.END, f"Highest ATS Score: {highest_score:.2f}%\n\n")
    result_text.insert(tk.END, f"Average ATS Score: {average_score:.2f}%\n\n")
    show_graph()

def search_history():
    resume_name = search_entry.get()
    reports = search_report(resume_name)
    result_text.delete("1.0",tk.END)
    if not reports:
        result_text.insert(tk.END,"No reports found.")
        return
    for report in reports:
        result_text.insert(tk.END,f"ID: {report[0]}\n")
        result_text.insert(tk.END,f"Resume: {report[1]}\n")
        result_text.insert(tk.END,f"ATS Score: {report[2]:.2f}%\n")
        result_text.insert(tk.END,f"Similarity: {report[3]:.2f}%\n")
        result_text.insert(tk.END,f"Date: {report[4]}\n")
        result_text.insert(tk.END,"-" * 40 + "\n\n")


def delete_history():
    report_id = delete_entry.get()
    if not report_id:
        return
    delete_report(report_id)
    result_text.delete("1.0",tk.END)
    result_text.insert(tk.END,f"Report ID {report_id} deleted successfully.")

root = tk.Tk()

root.config(bg="#f0f8ff")

title_label = tk.Label(root, text="Resume Analyzer", font=("Arial", 20, "bold"), bg="#f0f8ff")
title_label.pack(pady=10)

root.title("Resume Analyzer")
root.geometry("900x700")

resume_label = tk.Label(root, text="Enter Resume PDF Path:")
resume_label.pack()

resume_entry = tk.Entry(root, width=50)
resume_entry.pack()

browse_button = tk.Button(root, text="Browse", command=browse_resume)
browse_button.pack()

# jd_label = tk.Label(root, text="Enter JD Skills (comma separated):")
jd_label = tk.Label(root, text="Job Description PDF :")
jd_label.pack()

jd_entry = tk.Entry(root, width=60)
jd_entry.pack()

jd_button = tk.Button(root, text="Browse JD", command=browse_jd)
jd_button.pack(pady=5)

analyze_button = tk.Button(root, text="Analyze Resume", command=analyze_resume)
analyze_button.pack(pady=10)

report_button = tk.Button(root, text="View Previous Reports", command=show_reports)

export_button = tk.Button(root, text="Export PDF Report", command=export_pdf)
export_button.pack(pady=5)

analytics_button = tk.Button(root, text="Analytics Dashboard", command=show_analytics)
analytics_button.pack(pady=5)

search_label = tk.Label(root, text="Search Resume:")
search_label.pack()

search_entry = tk.Entry(root, width=40)
search_entry.pack()

search_button = tk.Button(root, text="Search Report", command=search_history)
search_button.pack(pady=5)

delete_label = tk.Label(root,text="Delete Report ID:")
delete_label.pack()

delete_entry = tk.Entry(root,width=15)
delete_entry.pack()

delete_button = tk.Button(root,text="Delete Report",command=delete_history)
delete_button.pack(pady=5)

# result_text = tk.Text(root, height=15, width=80)
# result_text.pack()    # adding scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text = tk.Text(root, height=10, width=80, yscrollcommand=scrollbar.set)
result_text.pack(pady=5)
scrollbar.config(command=result_text.yview)

# # result_label = tk.Label(root, height=20, width=80)    # OLD ONE 
result_label = tk.Label(root, text="Results will appear here", justify="left")
result_label.pack()


history_button = tk.Button(root, text="View Previous Reports", command=show_reports)
history_button.pack(pady=5)

root.mainloop()

