import os, json
files = [f for f in os.listdir('images') if f.endswith('.png')]
with open('imageList.json', 'w') as f:
    json.dump(files, f)
