from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


def create_pdf(filename, transcript, notes, quiz, flashcards):
    pdf_path = f"outputs/{filename}.pdf"

    os.makedirs("outputs", exist_ok=True)

    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    y = height - 40

    def write_block(title, text):
        nonlocal y
        c.setFont("Helvetica-Bold", 14)
        c.drawString(40, y, title)
        y -= 20

        c.setFont("Helvetica", 10)

        for line in text.split("\n"):
            if y < 40:
                c.showPage()
                y = height - 40
            c.drawString(40, y, line[:100])
            y -= 14

        y -= 10

    write_block("Transcript", transcript)
    write_block("Notes", notes)
    write_block("Quiz", quiz)
    write_block("Flashcards", flashcards)

    c.save()

    return pdf_path