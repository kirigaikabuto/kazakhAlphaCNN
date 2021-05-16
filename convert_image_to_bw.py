import os
from PIL import Image
import cv2


def resizeImage(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    resized_image = original_image.resize(size)
    resized_image.save(output_image_path)


alphaPath = "alpha.json"
foldersPath = "cv/"
folders = os.listdir(foldersPath)
filesAbsoluteDir = []
filesNames = []
bWFolder = "dataset/"
for folder in folders:
    path = foldersPath + folder
    temp = [path + "/" + i for i in os.listdir(path)]
    filesAbsoluteDir += temp
    tempNames = [i for i in os.listdir(path)]
    filesNames += tempNames

for i in range(len(filesNames)):
    print(filesAbsoluteDir[i])
    originalImage = cv2.imread(filesAbsoluteDir[i])
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(bWFolder + filesNames[i], blackAndWhiteImage)
    resizeImage(bWFolder + filesNames[i], bWFolder + filesNames[i], (28, 28))
