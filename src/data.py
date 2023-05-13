import os.path
import pandas as pd
from Application import Application
import numpy as np


def create_file_system():
    if not os.path.exists(cover_path):
        os.makedirs(cover_path)
    if not os.path.exists(resume_path):
        os.makedirs(resume_path)
    if not os.path.exists(csv_path):
        csv = open(csv_path, 'a')
        csv.write(column_line)
        csv.close()


def to_csv(app):
    return str(len(applications) - 1) + ";" + app.status + ";" + app.jobTitle + ";" + app.employmentType + ";" + \
           app.company + ";" + app.jobPosting + ";" + app.link + ";" + app.date + ";" + str(app.coverAdded) + \
           ";" + app.coverText + ";" + app.coverPdf + ";" + app.resumePdf + ";" + app.mistakes + ";" + \
           app.feedback + "\n"


def add_application_to_data(application):
    applications.append(application)

    def append_csv():
        csv_path = os.path.dirname(__file__) + "\\..\\data\\applications.csv"
        print(csv_path)
        csv_file = open(csv_path, "a")
        print(to_csv(application))
        csv_file.write(to_csv(application))
        csv_file.close()

    append_csv()
    to_csv(application)


def load_applications_from_csv():
    applications_file = open(csv_path, "r")

    applications_file.close()

    # reading the CSV file
    app_df = pd.read_csv(csv_path, sep=";")

    for i in range(app_df.shape[0]):
        new_app = Application("" if pd.isna(app_df.loc[i, "status"]) else app_df.loc[i, "status"],
                              "" if pd.isna(app_df.loc[i, "title"]) else app_df.loc[i, "title"],
                              "" if pd.isna(app_df.loc[i, "employmentType"]) else app_df.loc[i, "employmentType"],
                              "" if pd.isna(app_df.loc[i, "company"]) else app_df.loc[i, "company"],
                              "" if pd.isna(app_df.loc[i, "jobPosting"]) else app_df.loc[i, "jobPosting"],
                              "" if pd.isna(app_df.loc[i, "link"]) else app_df.loc[i, "link"],
                              "" if pd.isna(app_df.loc[i, "date"]) else app_df.loc[i, "date"],
                              "" if pd.isna(app_df.loc[i, "coverAdded"]) else app_df.loc[i, "coverAdded"],
                              "" if pd.isna(app_df.loc[i, "coverText"]) else app_df.loc[i, "coverText"],
                              "" if pd.isna(app_df.loc[i, "coverPdf"]) else app_df.loc[i, "coverPdf"],
                              "" if pd.isna(app_df.loc[i, "resumePdf"]) else app_df.loc[i, "resumePdf"],
                              "" if pd.isna(app_df.loc[i, "mistakes"]) else app_df.loc[i, "mistakes"],
                              "" if pd.isna(app_df.loc[i, "feedback"]) else app_df.loc[i, "feedback"])
        applications.append(new_app)


csv_path = os.path.dirname(__file__) + "\\..\\data\\applications.csv"
resume_path = os.path.dirname(__file__) + "\\..\\data\\resumes"
cover_path = os.path.dirname(__file__) + "\\..\\data\\cover_letters"

column_line = ";status;title;employmentType;company;jobPosting;link;" + \
                 "date;coverAdded;coverText;coverPdf;resumePdf;mistakes;feedback\n"

applications = []

if __name__ == "__main__":
    load_applications_from_csv()
    print(len(applications))
