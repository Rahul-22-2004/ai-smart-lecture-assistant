from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

def create_pdf(filename, transcript, notes, quiz, flashcards):

    os.makedirs("outputs", exist_ok=True)
    pdf_path = f"outputs/{filename}.pdf"

    doc = SimpleDocTemplate(pdf_path)
    styles = getSampleStyleSheet()

    story = []

    def add_section(title, text):
        story.append(Paragraph(f"<b>{title}</b>", styles["Heading1"]))
        for line in text.split("\n"):
            if line.strip():
                story.append(Paragraph(line, styles["Normal"]))
        story.append(Spacer(1, 12))

    add_section("Transcript", transcript)
    add_section("Notes", notes)
    add_section("Quiz", quiz)
    add_section("Flashcards", flashcards)

    doc.build(story)

    return pdf_path