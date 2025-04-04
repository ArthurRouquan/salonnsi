from pprint import pprint
from PyPDF2 import PdfReader, PdfWriter
from tqdm import tqdm

SUBJECTS_FOLDER = './data/sujets'
EXERCICES_FOLDER = './data/exercices'
SUBJECTS_INFO = """
24-NSI0A 2,3,4,5 6,7,8,9 10,11,12,13,14
24-NSI0B 2,3,4 5,6,7,8 9,10,11,12,13,14
24-NSIG11BIS 2,3,4 5,6,7,8 9,10,11,12,13
24-NSIJ1AN1 2,3,4,5 6,7,8 9,10,11,12,13
24-NSIJ1G11 2,3 4,5,6 7,8,9,10,11
24-NSIJ1JA1 2,3,4,5 6,7,8,9,10,11 12,13,14
24-NSIJ1ME1 2,3,4,5 6,7,8 9,10,11,12,13,14,15
24-NSIJ1ME3 2,3,4,5 6,7,8,9,10 11,12,13,14,15,16
24-NSIJ1PO1 2,3,4,5 6,7 8,9,10,11
24-NSIJ2AN1 2,3,4 5,6,7 8,9,10,11,12
24-NSIJ2G11 2,3,4,5 6,7,8 9,10,11,12,13,14
24-NSIJ2JA1 2,3,4 5,6,7 8,9,10,11,12
24-NSIJ2ME1 2,3,4 5,6,7,8 9,10,11,12,13,14,15
24-NSIJ2ME3 2,3 4,5,6 7,8,9,10,11,12
24-NSIJ2PO1 2,3,4,5,16 6,7,8,9 10,11,12,13,14,15
"""


def extract_pages(input_pdf, output_pdf, pages_to_extract):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page_num in pages_to_extract:
        writer.add_page(reader.pages[page_num - 1])  # PyPDF2 uses 0-based indexing

    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)


def pdf_to_string(pdf_path):
    return ''.join(page.extract_text() for page in PdfReader(pdf_path).pages)


def parse(subjects_info):
    lines = subjects_info.strip().split('\n')
    subjects = {}
    for line in lines:
        code, *pages = line.split()
        subjects[code] = [list(map(int, p.split(','))) for p in pages]
    return subjects


subjects = parse(SUBJECTS_INFO)

for code, exercices in subjects.items():
    print(code)
    subject_pdf = f'{SUBJECTS_FOLDER}/{code}.pdf'
    for i, pages in enumerate(exercices):
        exercise_pdf = f'{EXERCICES_FOLDER}/{code}-{i + 1}.pdf'
        extract_pages(subject_pdf, exercise_pdf, pages)
