#the code is taken and modded from https://pypi.org/project/pytesseract/
import pytesseract
import os.path

# convert all files ending in .jpg inside a directory
dirname = "C:\\songs\\1273"
i = 0
text = []
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# print(pytesseract.image_to_string(r'C:\copy\djangoproject\Alpha-2021\static\songs\GDFSC_v8_0048.tif'))

# with open('test.txt', 'w') as f:
# 	f.write(pytesseract.image_to_string(r'C:\\songs\\1520\\15201.png'))

# f.close()


for fname in os.listdir(dirname):
	i+=1

	if not fname.endswith(".png"):
		continue
	path = os.path.join(dirname, fname)
	if os.path.isdir(path):
		continue

	with open('test.txt', 'a') as f:
		f.write('PAGE START:============================================================\n')
		f.write(pytesseract.image_to_string(r'C:\\songs\\1273\\1273'+str(i)+'.png'))

f.close()

