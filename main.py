import csv
import os
import sys

# Hafnium(Hf) and Hydrogen floride(HF) problem
# taking · as . in input 

database = {} # Reading csv file
with open(os.path.abspath(os.path.dirname(sys.argv[0])) + '/database.csv', 'r') as database_file:
    readerx = csv.reader(database_file)
    for row in readerx:
        database[row[0]] = row[1]
database_file.close()

while True:
    prompt = input("Enter a symbol or a name OR ENTER q TO QUIT: ").lower()
    
    if prompt == "q": # Checks if the input is 'q'. If it is, quits the program.
        print("Thank You!")
        break

    try:
        result = database[prompt] # requesting from the data dictionary with key as user input.
        print(result)
    except KeyError:
        print("Not found in our database!")  