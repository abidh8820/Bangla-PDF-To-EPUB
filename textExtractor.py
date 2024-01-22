from autoocr import AutoOCR

oa = AutoOCR(lang='Bengali')
oa.set_datapath('/usr/local/Cellar/tesseract/4.0.0_1/share/tessdata')
oa.set_datapath('/path/to/tessdata')

def getText(image_path):
    text = oa.get_text(image_path)
    return text
