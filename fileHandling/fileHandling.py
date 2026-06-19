import csv
# fileHandling is to read and write the files 

# one-line summary

"""
r - read only (file must exist)
w - write-only (overwrites or creates)
a - append-only (adds to end of file)
r+ - read + write (file must exist)
w+ - write + read (overwites or creates)
a+ - append + read (creates if not exist)
rb - read binary
wb - write binary
ab - append binary
"""

# we must start by open() and close by close()

file = open("fileNAme.txt", "w")
file.write("Welcome to python file handling.\n")
file.write("This is new file.\n")
file.close()


file = open("fileNAme.txt", "r")
content = file.read()
print("file content :\n", content)
file.close()


file = open("fileHandling/fileNAme.txt", "a")
file.write("Adding a new line.\n")
file.close()


# in vscode we have to mention which folder or file the actual file we changing is there

# with is a pythonic way of handling the file 

with open("fileHandling/fileNAme.txt", "r") as file:
    for line in file:
        print(line.strip())


feedBack = input("Enter your feedback : ")

with open("fileHandling/feedback.txt", "a") as log:
        log.write(feedBack + "\n")

print("Thanks for the feedback")


with open("fileHandling/Data.txt") as file:
    pass

#above code is just to open a file without any content using pass


with open("fileHandling/Data.txt", "r") as file:
    print(file.readline().strip())
    print(file.readline().strip())
    print(file.readline().strip())
    print(file.readline().strip())


#in 'for line in file' works exactly like above code cause the word line exactly call readline()

# it works like below example

with open("fileHandling/Data.txt", "r") as file:
    while True:
        line = file.readline()
        if not line :
            break
        if "ERROR" in line :
            print(line.strip())


with open("fileHandling/Data.txt", "r") as file:
    for _ in range(4):
        print(file.readline().strip())

# the above code is to show _ that underscore is called throw variable and if we use any integer like in for loop we sould always use readline() ,y see the above code in line 66 in vs code



with open("fileHandling/example.csv", "r") as inFile, open("fileHandling/exportCSV.csv", "w") as exFile:
    for line in inFile:
        exFile.write(line)

with open("fileHandling/example.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["age"])

#this is using dictionaries
#here dictreader() is a predefined method in csv which will take the first line in a csv file as header's so we just call dictreader() from csv by csv.dictreader()
# and we have to mention the header by []


with open("fileHandling/example.csv", "r") as file:
    lines = file.readlines()
    for line in lines[1:]:
        coloumn = line.strip().split(",")
        print(coloumn[2])

"""
lines[0] = first line
lines[1] = second line
lines[1:] = second line to end (skip first)
lines[:1] = only first line
lines[:-1] = everything except last line
"""











