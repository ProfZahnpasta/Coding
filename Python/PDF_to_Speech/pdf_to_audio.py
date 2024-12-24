import pyttsx3
import PyPDF2
name_of_file = input("Whats the name of the file you want to convert to speech? (without .pdf) ")
pdf_file = open(f"{name_of_file}.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(pdf_file)
pages_of_pdf = len(pdf_reader.pages)
print("The PDF file has " , pages_of_pdf , " Pages") 
speaker = pyttsx3.init()
speaker.say("Test hallo Papa")
speaker.runAndWait()
