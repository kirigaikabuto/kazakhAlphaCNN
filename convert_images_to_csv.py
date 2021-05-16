from PIL import Image
from numpy import asarray
import os
import pandas as pd
import json

alphaFile = "alpha.json"
file = open(alphaFile, encoding="utf-8")
dataJson = file.read()
dataDict = json.loads(dataJson)
datasetDir = "final_data/"
files = os.listdir(datasetDir)
targets = []
all = []

for file in files:
    name, res = file.split(".")
    temp = []
    path = datasetDir + "/" + file
    img = Image.open(path)
    arraydata = asarray(img)
    for i in arraydata:
        for j in i:
            if j == 255:
                temp.append(0)
            else:
                temp.append(1)
    for key in dataDict:
        if key in name:
            print(name, key)
            targets.append([dataDict[key]])
            break
    all.append(temp)

df = pd.DataFrame(all)
df.to_csv("data.csv")

df = pd.DataFrame(targets)
df.to_csv("targets.csv")
