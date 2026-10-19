from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text, jd_text):
  documents = [resume_text, jd_text]
  vectorizer = TfidfVectorizer()

  matrix = vectorizer.fit_transform(documents)

  similarity = cosine_similarity(matrix[0], matrix[1])

  return similarity[0][0] * 100