import os
from pdf2image import convert_from_path
from LayoutAnalysis import *

def convert_pdf_to_images(input_file, output_directory, dpi=300):
    # Check if the output directory exists, and create it if not
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Convert PDF to images
    pages = convert_from_path(input_file, dpi)
    # TODO: Optimize this to use numpy arrays directly instead of PIL's image libraries

    # Save images in the specified directory as PNG
    for count, page in enumerate(pages):
        page = np.array(page)
        page = extractParagraphsFromImage(page)
        page = Image.fromarray(page)
        image_path = os.path.join(output_directory, f'page{count}.png')
        page.save(image_path, 'PNG')

    print(f"Conversion completed. Images saved in '{output_directory}'")

# Example usage:
convert_pdf_to_images('paper.pdf', 'paper', 100)
