def generate_suggestions(missing_skills):
  suggestions = []
  for skill in missing_skills:
    suggestions.append(f"Consider adding experience in {skill}")

  return suggestions