'''
we use pip(package manager)
https://pypi.org

colorama -> used to print colorfull texts in terminal
'''
'''
from colorama import init, Fore
init()

print(Fore.CYAN + 'Ronaldo')'''

from reportlab.pdfgen import canvas

def create_pdf(file_path, content):
    # Create a PDF document
    pdf_canvas = canvas.Canvas(file_path)

    # Add content to the PDF
    pdf_canvas.drawString(100, 750, content)

    # Save the PDF
    pdf_canvas.save()

# Example usage
pdf_path = 'example.pdf'
content_to_add = 'Hello, this is a sample PDF content.'
create_pdf(pdf_path, content_to_add)

