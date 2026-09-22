import fitz
import os

from app.config import PDF_TEMPLATE, PDF_OUTPUT_DIR


def generate_application_pdf(applicant):

    os.makedirs(PDF_OUTPUT_DIR, exist_ok=True)

    student_id = applicant["id"]

    # PDF path
    pdf_path = PDF_OUTPUT_DIR / f"student_{student_id}_application.pdf"

    # Open existing PDF template
    pdf = fitz.open(PDF_TEMPLATE)

    # Get the first page
    page = pdf[0]

    # ==================================================
    # STUDENT INFORMATION
    # ==================================================

    page.insert_text(
        (120, 135),
        str(applicant["id"]),
        fontsize=9
    )

    page.insert_text(
        (120, 170),
        str(applicant["first_name"] or ""),
        fontsize=9
    )

    page.insert_text(
        (120, 195),
        str(applicant["last_name"] or ""),
        fontsize=9
    )

    page.insert_text(
        (120, 225),
        str(applicant["date_of_birth"] or ""),
        fontsize=9
    )

    page.insert_text(
        (120, 250),
        str(applicant["gender"] or ""),
        fontsize=9
    )

    # ==================================================
    # GUARDIAN INFORMATION
    # ==================================================

    guardians = applicant.get("guardians", [])

    # --------------------------------------------------
    # Guardian 1
    # --------------------------------------------------

    if len(guardians) > 0:

        guardian1 = guardians[0]

        page.insert_text(
            (120, 370),
            str(guardian1["first_name"] or ""),
            fontsize=9
        )

        page.insert_text(
            (380, 370),
            str(guardian1["last_name"] or ""),
            fontsize=9
        )

        page.insert_text(
            (120, 400),
            str(guardian1["relationship"] or ""),
            fontsize=9
        )

        page.insert_text(
            (380, 400),
            str(guardian1["phone"] or ""),
            fontsize=9
        )

        page.insert_text(
            (120, 430),
            str(guardian1["email"] or ""),
            fontsize=9
        )

        page.insert_text(
            (120, 460),
            str(guardian1["address"] or ""),
            fontsize=8
        )

    # --------------------------------------------------
    # Guardian 2
    # --------------------------------------------------

    if len(guardians) > 1:

        guardian2 = guardians[1]

        page.insert_text(
            (120, 530),
            str(guardian2["first_name"] or ""),
            fontsize=9
        )

        page.insert_text(
            (380, 530),
            str(guardian2["last_name"] or ""),
            fontsize=9
        )

        page.insert_text(
            (120, 555),
            str(guardian2["relationship"] or ""),
            fontsize=9
        )

        page.insert_text(
            (380, 555),
            str(guardian2["phone"] or ""),
            fontsize=9
        )

        page.insert_text(
            (120, 585),
            str(guardian2["email"] or ""),
            fontsize=9
        )

        page.insert_text(
            (120, 615),
            str(guardian2["address"] or ""),
            fontsize=8
        )

    # ==================================================
    # SAVE AS A NEW PDF
    # ==================================================

    pdf.save(pdf_path)

    pdf.close()

    return pdf_path