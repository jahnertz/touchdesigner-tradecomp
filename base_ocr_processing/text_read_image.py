from PIL import Image
import pytesseract as pyt

tesseract_exe = tdu.expandPath(ipar.ExtPython.Tesseractexe)

pyt.pytesseract.tesseract_cmd = r"%s" % tesseract_exe

ocr_result = pyt.image_to_string(Image.open('ocr_source.png'))
print(ocr_result)
op('text_ocr_result')[0,0] = ocr_result
