
import csv
import os
import sys

database = {}
with open(os.path.abspath(os.path.dirname(sys.argv[0])) + '/database.csv', 'r') as database_file:
    readerx = csv.reader(database_file)
    for row in readerx:
        database[row[0]] = row[1]

exeptions = []
with open(os.path.abspath(os.path.dirname(sys.argv[0])) + '/exeptions.csv', 'r') as exeptions_file:
    readery = csv.reader(exeptions_file)
    l = list(readery)
    for sublist in l:
        for item in sublist:
            exeptions.append(item)

def converter():
    prompt = input("Enter a symbol or a name of a chemical compound OR ENTER q TO QUIT: ")

    for expetion in exeptions:
        if prompt in exeptions:
            prompt = prompt.capitalize()

    for symbol in database:
        if prompt in database or prompt == "q":
            break
        else:
            print("Not found in our database")
            return True

    if prompt == "q":
        print("Thank You!")
        return False

    print(database[prompt])


while converter() is not False:
        converter()
    