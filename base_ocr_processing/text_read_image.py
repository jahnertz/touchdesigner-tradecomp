from PIL import Image
import pytesseract as pyt

pyt.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

print(pyt.image_to_string(Image.open('ocr_source.png')))
