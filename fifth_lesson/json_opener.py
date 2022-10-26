import json
f = open('dz_5_1.json')
data = json.load(f)
for i in data["menu"]:
    print(i)

# Closing file
f.close()