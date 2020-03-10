import csv
with open('old_path.txt', 'r') as t1, open('new_path.txt', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('differences.txt', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)
