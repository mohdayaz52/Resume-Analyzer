from reportlab.pdfgen import canvas

def generate_pdf(ats_score, similarity_score, missing_skills, suggestions):
    pdf = canvas.Canvas("Analysis_Report.pdf")
    y = 800
    pdf.drawString(100, y, "AI Resume Analysis Report")
    y -= 40
    pdf.drawString(100, y, f"ATS Score: {ats_score:.2f}%")
    y -= 40
    pdf.drawString(100, y, f"Similarity Score: {similarity_score:.2f}%")
    y -= 40
    pdf.drawString(100, y, "Missing Skills:")
    y -= 20
    for skill in missing_skills:
        pdf.drawString(120, y, f"- {skill}")
        y -= 20
    y -= 20
    pdf.drawString(100, y, "Suggestions:")
    y -= 20
    for suggestion in suggestions: 
        pdf.drawString(120, y, f"- {suggestion}")
        y -= 20
    pdf.save()