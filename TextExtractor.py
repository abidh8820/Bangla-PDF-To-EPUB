from autoocr import AutoOCR

oa = AutoOCR(lang='bangla') 
oa.set_datapath('/usr/share/tesseract-ocr/5/tessdata')

def getText(image_path):
    text = oa.get_text(image_path)
    return text

def append_to_markdown(file_path, text):
    try:
        with open(file_path, 'a', encoding='utf-8') as markdown_file:
            markdown_file.write(text + '\n\n')
    except Exception as e:
        print(f'Error appending text to {file_path}: {e}')


markdown_file_path = 'output.md'
text_to_append = (getText('sample.png'))

append_to_markdown(markdown_file_path, text_to_append)
