
import csv

database = {}
with open('./chem-symbol-to-name/database.csv', 'r') as database_file:
    readerx = csv.reader(database_file)
    for row in readerx:
        database[row[0]] = row[1]

exeptions = []
with open('./chem-symbol-to-name/exeptions.csv', 'r') as exeptions_file:
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
    