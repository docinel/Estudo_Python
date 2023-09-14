from PyPDF2 import PdfReader
pdf_file = open('sources/pdf/NOTAS.pdf','rb')
reader = PdfReader(pdf_file)
page = reader.pages[1]
text = page.extract_text()
print(text)