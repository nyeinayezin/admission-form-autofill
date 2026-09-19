'''def read_applicant_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    applicant = {}

    for line in lines:
        key, value = line.strip().split(":", 1)
        applicant[key.strip()] = value.strip()

    return applicant


def main():
    applicant = read_applicant_file("data/applicant.txt")

    print("Applicant information:")
    print(applicant)


if __name__ == "__main__":
    main()   '''
from app.database.database import create_database, save_applicant
from app.config import APPLICANT_FILE
def read_applicant_file(file_path):
    applicant = {}
    with open (file_path,"r", encoding = "utf-8") as file:
        for line in file:
            key, value = line.strip().split(":",1)
            applicant[key.strip()] = value.strip()
    return applicant
def main():
    create_database()
    applicant = read_applicant_file(APPLICANT_FILE)
    print(applicant)
    save_applicant(applicant)
if __name__=="__main__":
    main()
