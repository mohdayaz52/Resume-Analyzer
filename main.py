from resume_reader import extract_text
from skill_matcher import find_skills
from ats_score import calculate_score
from similarity import calculate_similarity
from suggestions import generate_suggestions
from database import create_database, save_report, view_reports

create_database()

resume_path = input("Enter Resume PDF Path : ")
resume_text = extract_text(resume_path)

resume_skills = find_skills(resume_text)

jd_input = input("Enter JD Skills (comma separated) : ")

jd_skills = [
  skill.strip().lower()
  for skill in jd_input.split(",")
]

score, matched = calculate_score(resume_skills, jd_skills)

similarity_score = calculate_similarity(resume_text, jd_input)


missing = []
for skill in jd_skills:
  if skill not in matched:
    missing.append(skill)

suggestions = generate_suggestions(missing)

print("\nATS Score : ", round(score, 2), "%")

print("\nMatched Skills : ")
for skill in matched:
  print("-", skill)

print("\nMissing Skills : ")
for skill in missing:
  print("-", skill)

print("\nResume Similarity: ", round(similarity_score, 2), "%")

print("\nSuggestions: ")
for s in suggestions:
    print("-", s)

save_report(resume_path, score, similarity_score)

print("\nSaved Reports: ")
for report in view_reports():
    print(report)

