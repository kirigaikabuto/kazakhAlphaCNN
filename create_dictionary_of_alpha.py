import os
import json

path = "cv/1/"
files = os.listdir(path)
alpha_dict = {}
for i in range(len(files)):
    name, ras = files[i].split(".")
    alpha_dict[name] = i

data = json.dumps(alpha_dict, indent=4, ensure_ascii=False, )
file = open("alpha.json", "w", encoding="utf-8")
file.write(data)
file.close()
