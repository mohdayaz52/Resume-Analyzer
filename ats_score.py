def calculate_score(resume_skill, jd_skills):
  matched = []
  for skill in jd_skills:
    if skill in resume_skill:
      matched.append(skill)

  score = (len(matched) / len(jd_skills)) * 100

  return score, matched