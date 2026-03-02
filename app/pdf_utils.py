from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
import os


def create_pdf(filename, transcript, notes, quiz, flashcards):

    os.makedirs("outputs", exist_ok=True)
    pdf_path = f"outputs/{filename}.pdf"

    doc = SimpleDocTemplate(pdf_path)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        name="TitleStyle",
        parent=styles["Heading1"],
        alignment=TA_CENTER,
        spaceAfter=20
    )

    story = []

    story.append(Paragraph("AI Smart Lecture Assistant", title_style))
    story.append(Spacer(1, 20))

    # -------- Transcript --------
    story.append(Paragraph("Transcript", styles["Heading2"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(transcript.replace("\n", "<br/>"), styles["Normal"]))
    story.append(Spacer(1, 20))

    # -------- Notes --------
    story.append(Paragraph("Structured Notes", styles["Heading2"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(notes.replace("\n", "<br/>"), styles["Normal"]))
    story.append(Spacer(1, 20))

    # -------- Quiz --------
    story.append(Paragraph("Quiz", styles["Heading2"]))
    story.append(Spacer(1, 10))

    if isinstance(quiz, list):
        for i, q in enumerate(quiz):
            story.append(Paragraph(f"<b>Q{i+1}:</b> {q['question']}", styles["Normal"]))
            story.append(Spacer(1, 5))
            for idx, option in enumerate(q["options"]):
                story.append(Paragraph(f"{chr(65+idx)}. {option}", styles["Normal"]))
            story.append(Spacer(1, 5))
            story.append(Paragraph(f"<b>Answer:</b> {q['answer']}", styles["Normal"]))
            story.append(Spacer(1, 15))

    story.append(Spacer(1, 20))

    # -------- Flashcards --------
    story.append(Paragraph("Flashcards", styles["Heading2"]))
    story.append(Spacer(1, 10))

    if isinstance(flashcards, str):
        story.append(Paragraph(flashcards.replace("\n", "<br/>"), styles["Normal"]))

    doc.build(story)

    return pdf_path