from PIL import Image
import pytesseract as pyt
import re

tesseract_exe = tdu.expandPath(ipar.ExtPython.Tesseractexe)

pyt.pytesseract.tesseract_cmd = r"%s" % tesseract_exe

ocr_result = pyt.image_to_string(Image.open('ocr_source.png'))
if re.match(ocr_result, "^\s*$"):
    ocr_result = "ERROR: No readable text found."
else:
    ocr_result = re.sub('\s+', '', ocr_result)

equity = "$" + "{:,}".format(float(ocr_result))
print(equity)
op('text_ocr_result')[0,0] = equity
