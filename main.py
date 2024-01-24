from ImageExtractor import *
from TextExtractor import *

def createMarkdown(pdf_path: str, dpi = 100):
    target_dir = 'paper'
    markdown_file_path = 'output.md'

    convert_pdf_to_images(pdf_path, target_dir, dpi)

    if os.path.exists(target_dir) and os.path.isdir(target_dir):
        files = sorted(os.listdir(target_dir))
        for filename in files:
            filepath = os.path.join(target_dir, filename)
            if os.path.isfile(filepath):
                append_to_markdown(markdown_file_path, getText(filepath))
                print(f"Processing file: {filename}")


createMarkdown('paper.pdf', 100)