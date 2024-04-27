import glob

mifiles = glob.glob("files/*.txt")

for filepath in mifiles:
    with open(filepath, 'r') as file:
        print(file.read())