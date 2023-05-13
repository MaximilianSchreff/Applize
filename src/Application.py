class Application():
    def __init__(self, company, jobTitle, jobType, jobDescription, status, date, feedback, coverLetterPdf, coverLetterText, coverletterPdfFile, coverLetterTextFile, cvFile):
        self.company = company
        self.jobTitle = jobTitle
        self.jobType = jobType
        self.jobDescription = jobDescription
        self.status = status
        self.date = date
        self.feedback = feedback
        #Boolean ob Anschreiben existiert (in PDF oder Textform)
        self.coverLetterPdf = coverLetterPdf
        self.coverLetterText = coverLetterText
        #Pfade zu den Dateien
        self.coverletterPdfFile = coverletterPdfFile
        self.coverLetterTextFile = coverLetterTextFile
        self.cvFile = cvFile

    def toCsv(self):
        return self.company + "," + self.jobTitle + "," + self.jobType + "," + self.jobDescription + "," + self.status + "," + self.date + "," + self.feedback + "," + self.coverLetterPdf + "," + self.coverLetterText + "," + self.coverletterPdfFile + "," + self.coverLetterTextFile + "," + self.cvFile + "\n"


