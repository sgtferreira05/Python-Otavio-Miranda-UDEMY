# PyPDF2 > to manipulate PDF files
# PyPDF2 is a library for reading and writing PDF files in Python. It's free and open-source, and it allows you to extract text, merge, split, and manipulate PDF files in various ways.
# The documentation for PyPDF2 can be found at: https://pypdf2.readthedocs.io/en/3.x/

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger


root_file = Path(__file__).parent

original_file = root_file / 'pdfs_originais'
new_file = root_file / 'new.pdf'

bacen_relatory = original_file / 'R20250411.pdf'


new_file.mkdir( exist_ok=True)
reader = PdfReader(bacen_relatory)


# print(len(reader.pages)) # Number of pages in the PDF file
# for page in reader.pages:
#     print(page) 
#     print('---' * 20) # Separator between pages 


page1 = reader.pages[0] # First page of the PDF file
page2 = reader.pages[1] # Second page of the PDF file

image2 = page2.images[1] # First image of the first page


# print(page1.extract_text()) # Extract text from the first page
# print(page2.extract_text()) # Extract text from the second page

# print(page1.images[0]) # List of images in the first page

# with open(new_file / image1.name, 'wb') as fp:
#     fp.write(image1.data) # Save the image to a file

# writer = PdfWriter()
# writer.add_page(page1) # Add the first page to the new PDF file
# with open(new_file / 'page1.pdf', 'wb') as fp:
#     writer.write(fp) # Save the new PDF file with the first page only




# # COLOCAR OS PDF's EM UMA PASTA NOVA
# writer = PdfWriter()

# with open(new_file / 'all_pages.pdf', 'wb') as fp:
#     for page in reader.pages:
#         writer.add_page(page)
#     writer.write(fp) # Save the new PDF file with all pages



# # SEPARAR OS PDF's
# for i, page in enumerate(reader.pages):
#     writer = PdfWriter()
#     with open(new_file / f'page{i}.pdf', 'wb') as fp:
#         writer.add_page(page)
#         writer.write(fp)


## MERGE PDF's
# merger = PdfMerger()

# files = [
#     new_file / 'page1.pdf',
#     new_file / 'page0.pdf',
# ]
# for file in files:
#     merger.append(file)

# with open(new_file / 'merged.pdf', 'wb') as fp:
#     merger.write(fp) # Save the new PDF file with all pages merged