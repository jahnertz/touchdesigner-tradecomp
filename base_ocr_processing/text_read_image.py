from PIL import Image
import pytesseract as pyt

pyt.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

ocr_result = pyt.image_to_string(Image.open('ocr_source.png'))
print(ocr_result)
op('text_ocr_result')[0,0] = ocr_result
