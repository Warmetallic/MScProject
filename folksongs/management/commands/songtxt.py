#the code is taken and modded from https://pypi.org/project/pytesseract/
import pytesseract
import os.path

# convert all files ending in .jpg inside a directory
dirname = "C:\copy\djangoproject\Alpha-2021\static\songs"
i = 46
text = []
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# print(pytesseract.image_to_string(r'C:\copy\djangoproject\Alpha-2021\static\songs\GDFSC_v8_0048.tif'))

with open('test.txt', 'w') as f:
	f.write(pytesseract.image_to_string(r'C:\copy\djangoproject\Alpha-2021\static\songs\GDFSC_v8_0048.tif'))

f.close()


for fname in os.listdir(dirname):
	i+=1

	if not fname.endswith(".tif"):
		continue
	path = os.path.join(dirname, fname)
	if os.path.isdir(path):
		continue

	with open('test.txt', 'a') as f:
		f.write('PAGE START:============================================================\n')
		f.write(pytesseract.image_to_string(r'C:\copy\djangoproject\Alpha-2021\static\songs\GDFSC_v8_00'+str(i)+'.tif'))

f.close()

