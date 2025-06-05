class availability:
    def __init__(self, status, studnetnumber):
        self.status = status
        self.studnetnumber = studnetnumber
    def __str__(self):
        return f"Status: {self.status} Student Number : {self.studnetnumber}"

class Book:
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability
        self.pages = 100
        self.cost = 124

    def __str__(self):
        return f"Book Name : {self.title} - Book Status : {self.availability}"
