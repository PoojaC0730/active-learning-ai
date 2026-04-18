# Text processor module

import fitz
import logging

logger = logging.getLogger(__name__)

def extract_text(file):
    try:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text() + "\n"
        return text
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {e}")
        return ""

def extract_all(files):
    all_text = ""
    for file in files:
        all_text += extract_text(file) + "\n"
    return all_text

def chunk_text(text, chunk_size):
    for i in range(0, len(text), chunk_size):
        yield text[i:i + chunk_size]
