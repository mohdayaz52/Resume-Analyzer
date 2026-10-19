from skills import skills

def find_skills(text):
  found = []
  for skill in skills:
    if skill in text:
      found.append(skill)

  return found