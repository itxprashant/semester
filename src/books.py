import os
import subprocess

default_pdf_reader = "okular"

library_address = []

class Book:
    def __init__(self, title, author, edition, address):
        self.title = title
        self.author = author
        self.edition = edition
        self.address = address
    
    def openBook(self):
        print(f"Opening book: {self.title}")
        subprocess.run(f"{default_pdf_reader} {self.title}.pdf")
        
def loadLibrary():
    print("Loading library....")

def refreshLibrary():
    print("Refreshing library....")


        
