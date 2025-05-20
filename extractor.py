import pdfplumber
import os

from markdownify import markdownify as md


class Extractor:

    def __init__(self, path):
        self.folder_path = path

    def extract_all_pdfs(self):
        all_markdowns = []
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(self.folder_path, filename)
                markdown = self.convert_pdf_to_markdown(pdf_path)
                all_markdowns.append(markdown)
                print(f"Обработан файл: {filename}")
        return all_markdowns

    @staticmethod
    def convert_pdf_to_markdown(pdf_path):
        markdown_text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    markdown_text += md(text) + "\n\n"
        return markdown_text
