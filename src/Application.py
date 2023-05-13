
class Application:
    def __init__(self, jobTitle, employmentType, company, jobPosting, link, date,
                 coverAdded, coverText, coverPdf, resumePdf, status, mistakes, feedback):
        # job info
        self.jobTitle = jobTitle
        self.employmentType = employmentType
        self.company = company
        self.jobPosting = jobPosting
        self.link = link

        # application info
        self.date = date
        self.coverAdded = coverAdded
        self.coverText = coverText
        # file paths
        self.coverPdf = coverPdf
        self.resumePdf = resumePdf

        # application overhead
        self.status = status
        self.mistakes = mistakes
        self.feedback = feedback

    def toCsv(self):
        return self.company + "," + self.jobTitle + "," + self.employmentType + "," + self.jobPosting + "," + \
               self.status + "," + self.date + "," + self.feedback + "," + self.coverPdf + "," + \
               self.coverText + "," + self.resumePdf + "\n"


