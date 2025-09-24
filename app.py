import os
from manga_ocr import MangaOcr
from PIL import Image
import easyocr
from transformers import pipeline

imgPath = 'Examples/6.png'
img = Image.open(imgPath)

# Load models.
reader = easyocr.Reader(['ja'])
mocr = MangaOcr()
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-ja-en")

# Find textboxes, crop and save them.
results = reader.readtext(imgPath, decoder='beamsearch')

croppedImgIndex = 1
for result in results:
	textBoxCoords,_,_ = result
	botLeftX = int(min(textBoxCoords[0][0],textBoxCoords[1][0],textBoxCoords[2][0],textBoxCoords[3][0]))
	botLeftY = int(min(textBoxCoords[0][1],textBoxCoords[1][1],textBoxCoords[2][1],textBoxCoords[3][1]))
	topRightX = int(max(textBoxCoords[0][0],textBoxCoords[1][0],textBoxCoords[2][0],textBoxCoords[3][0]))
	topRightY = int(max(textBoxCoords[0][1],textBoxCoords[1][1],textBoxCoords[2][1],textBoxCoords[3][1]))
	width = topRightX - botLeftX
	length = topRightY - botLeftY
	croppedImg = img.crop((botLeftX,botLeftY,botLeftX + width,botLeftY + length))
	croppedImg.save('croppedImages/croppedImg' + str(croppedImgIndex) + '.png')
	croppedImgIndex += 1

# Extract text from cropped images.
croppedImgFolderPath = 'croppedImages'
croppedImgList = os.listdir(croppedImgFolderPath)
for croppedImg in croppedImgList:
	text = mocr(croppedImgFolderPath + '/' + croppedImg)
	print(text)
	print(pipe(text)[0]['translation_text'])