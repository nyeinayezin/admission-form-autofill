from pathlib import Path
# Project root folder
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
# Data folder
DATA_DIR = BASE_DIR / "data"
# Database file
DATABASE_NAME = DATA_DIR / "school.db"
# Applicant input file
APPLICANT_FILE = DATA_DIR / "applicant.txt"

# Database_sql folder
SQL_DIR = BASE_DIR / "database_sql"
# Templates Folder
TEMPLATE_DIR = BASE_DIR/"templates"
# Pdf #
PDF_TEMPLATE = TEMPLATE_DIR/"school_application_form_template.pdf"
PDF_OUTPUT_DIR = BASE_DIR/"generated_pdfs"





