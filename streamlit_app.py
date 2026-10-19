import streamlit as st
from datetime import datetime
from resume_reader import extract_text
from skill_matcher import find_skills
from ats_score import calculate_score
from similarity import calculate_similarity
from suggestions import generate_suggestions
from rating import get_resume_rating
from database import create_database, save_report, get_reports

create_database()

st.set_page_config(page_title="Resume Analyzer", page_icon="📄", layout="wide")

st.title("📄 Resume Analyzer")
st.write("Analyze resumes against job descriptions using ATS scoring, NLP similarity matching, and skill gap analysis.")

resume_file = st.file_uploader("Upload Resume PDF", type=["pdf"])
jd_file = st.file_uploader("Upload Job Description PDF", type=["pdf"])

if st.button("Analyze Resume"):
    if resume_file is None or jd_file is None:
        st.error("Please upload both Resume and Job Description PDFs.")
    else:
        with open("temp_resume.pdf", "wb") as file:
            file.write(resume_file.getbuffer())

        with open("temp_jd.pdf", "wb") as file:
            file.write(jd_file.getbuffer())

        resume_text = extract_text("temp_resume.pdf")
        jd_text = extract_text("temp_jd.pdf")
        resume_skills = find_skills(resume_text)
        jd_skills = find_skills(jd_text)
        score, matched = calculate_score(resume_skills, jd_skills)
        similarity_score = calculate_similarity(resume_text, jd_text)
        missing = list(set(jd_skills) - set(matched))
        suggestions = generate_suggestions(missing)
        rating = get_resume_rating(score)
        analysis_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        save_report(resume_file.name, score, similarity_score)

        st.success("Analysis Complete")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("ATS Score", f"{score:.2f}%")

        with col2:
            st.metric("Similarity Score", f"{similarity_score:.2f}%")

        with col3:
            st.metric("Resume Rating", rating)

        st.write(f"**Analysis Time:** {analysis_time}")
        st.subheader("✅ Matched Skills")
        st.write(matched if matched else "No matched skills found.")
        st.subheader("❌ Missing Skills")
        st.write(missing if missing else "No missing skills detected.")
        st.subheader("💡 Suggestions")

        if suggestions:
            for suggestion in suggestions:
                st.write(f"- {suggestion}")
        else:
            st.write("No suggestions required.")

st.divider()

if st.button("View Previous Reports"):
    reports = get_reports()
    st.subheader("📊 Previous Reports")

    if reports:
        for report in reports:
            st.write(report)
    else:
        st.info("No reports available.")