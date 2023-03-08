import pdfplumber
import re

def parsePDFFileToNotes(file):
    with pdfplumber.open(file) as pdf:
        dirty_notes = []
        pattern = r"[0-7]+\.\d{2}"
        for page in pdf.pages:
            page_text = page.extract_text()
            matches = re.findall(pattern, page_text)
            dirty_notes.extend(matches)
        clean_notes = []
        for dirty_note in dirty_notes:
            clean_note = float(re.sub("[^0-9.]", "", dirty_note))
            clean_notes.append(clean_note)
        notes_without_ppa = clean_notes[1:]
    return notes_without_ppa