# 📄 AI Resume Analyzer

An AI-powered Resume Analyzer built using Python, Streamlit, SQLite, and NLP techniques to evaluate resumes against job descriptions.

---

## 🚀 Features

### Resume Analysis
- PDF Resume Upload
- PDF Job Description Upload
- Automatic Text Extraction
- Skill Detection

### ATS Analysis
- ATS Score Calculation
- Resume Strength Rating
- Matched Skills Identification
- Missing Skills Detection

### NLP Features
- TF-IDF Vectorization
- Cosine Similarity Calculation
- Resume-Job Description Matching

### Recommendations
- Personalized Improvement Suggestions
- Skill Gap Analysis

### Report Management
- SQLite Database Integration
- Save Analysis History
- View Previous Reports
- Search Reports
- Delete Reports

### Analytics
- ATS Score Trends
- Average ATS Score
- Highest ATS Score
- Matplotlib Visualizations

### Export Features
- PDF Report Generation
- Downloadable Analysis Reports

### User Interfaces
- Tkinter Desktop Application
- Streamlit Web Application

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Libraries

### PDF Processing

- PyPDF2

Purpose:
- Extract text from Resume PDFs
- Extract text from Job Description PDFs

---

### Machine Learning & NLP

- Scikit-Learn

Used For:
- TF-IDF Vectorization
- Cosine Similarity

---

### Database

- SQLite

Used For:
- Report Storage
- Report History
- Search Functionality

---

### Visualization

- Matplotlib

Used For:
- ATS Analytics Dashboard
- Performance Trends

---

### PDF Generation

- ReportLab

Used For:
- Export Analysis Reports as PDF

---

### GUI

- Tkinter

Used For:
- Desktop Application

---

### Web Application

- Streamlit

Used For:
- Browser-based Resume Analyzer

---

# 🏗️ Project Structure

```text
AI_RESUME_ANALYZER
│
├── streamlit_app.py
├── gui.py
├── analytics.py
├── ats_score.py
├── database.py
├── jd_reader.py
├── rating.py
├── report_generator.py
├── resume_reader.py
├── similarity.py
├── skill_matcher.py
├── skills.py
├── suggestions.py
│
├── sample_resume.pdf
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ How It Works

```text
Resume PDF
      ↓
Text Extraction
      ↓
Skill Detection
      ↓
ATS Calculation
      ↓
TF-IDF Analysis
      ↓
Cosine Similarity
      ↓
Missing Skill Detection
      ↓
Suggestions Generation
      ↓
Store in Database
      ↓
Display Results
      ↓
Export PDF Report
```

---

# 📚 Modules

## resume_reader.py

Responsible For:

- Reading Resume PDFs
- Extracting Text

---

## jd_reader.py

Responsible For:

- Reading Job Description PDFs
- Extracting Text

---

## skill_matcher.py

Responsible For:

- Finding technical skills from extracted text

---

## ats_score.py

Responsible For:

- Calculating ATS Score

Formula:

```text
ATS Score =
Matched Skills
---------------- × 100
Total JD Skills
```

---

## similarity.py

Responsible For:

- TF-IDF Vectorization
- Cosine Similarity Calculation

Purpose:

```text
Measure similarity between Resume and Job Description.
```

---

## suggestions.py

Responsible For:

- Generating Resume Improvement Suggestions

---

## rating.py

Responsible For:

Resume Ratings:

```text
90-100 → ★★★★★ Excellent

75-89 → ★★★★ Good

50-74 → ★★★ Average

25-49 → ★★ Needs Improvement

0-24 → ★ Poor
```

---

## database.py

Responsible For:

- Creating Database
- Saving Reports
- Viewing Reports
- Searching Reports
- Deleting Reports

---

## analytics.py

Responsible For:

- ATS Analytics
- Performance Visualization

---

## report_generator.py

Responsible For:

- Exporting Analysis Reports to PDF

---

# 📊 Example Output

```text
Analysis Time:
2026-10-17 20:15:10

ATS Score:
54.55%

Resume Rating:
★★★ Average

Similarity Score:
20.16%

Matched Skills:
python
sql
html
css
git
c++

Missing Skills:
mongodb
mysql
javascript
java
aws

Suggestions:
Consider adding experience in mongodb
Consider adding experience in mysql
Consider adding experience in javascript
Consider adding experience in java
Consider adding experience in aws
```

---

# 📈 Analytics Dashboard

Displays:

- Total Reports
- Highest ATS Score
- Average ATS Score
- ATS Trend Graph

---

# 🗄️ Database Schema

### reports

| Column | Type |
|----------|----------|
| id | INTEGER |
| resume_name | TEXT |
| ats_score | REAL |
| similarity_score | REAL |
| analysis_date | TEXT |

---

# 📦 Installation

Clone Repository:

```bash
git clone https://github.com/yourusername/AI-Resume-Analyzer.git
```

Move Into Project:

```bash
cd AI-Resume-Analyzer
```

Install Dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Desktop Application

```bash
python gui.py
```

---

# 🌐 Run Streamlit Application

```bash
streamlit run streamlit_app.py
```

---

# 🎯 Concepts Implemented

- Python Programming
- Modular Programming
- File Handling
- PDF Processing
- SQLite Database
- SQL Queries
- CRUD Operations
- Natural Language Processing
- TF-IDF
- Cosine Similarity
- Data Visualization
- GUI Development
- Streamlit Web Apps
- Report Generation

---

# 🔮 Future Improvements

- Resume Ranking System
- AI-Powered Resume Suggestions
- Job Recommendation Engine
- User Authentication
- Cloud Deployment
- Multi-Resume Comparison
- Advanced NLP Models

---

# 👨‍💻 Author

**Mohd Ayaz**

B.Tech Computer Science Engineering  
Jamia Millia Islamia

---

# ⭐ Project Status

```text
Version: 5.0

Status: Completed ✅
```