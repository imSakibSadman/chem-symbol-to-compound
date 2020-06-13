
"""
data = {
       "Carbon": "c",
       "Oxygen": "o"
}

exeptions = ["carbon", "oxygen"]
   
   
prompt = input("Enter a symbol or a name of a chemical compound OR ENTER q TO QUIT: ")

for expetion in exeptions:
    if prompt in exeptions:
        prompt = prompt.capitalize()

print(data[prompt])
"""
import csv

data = {
       "Carbon": "c",
       "Oxygen": "o"
}


#exeptions = ['']

with open('./chem-symbol-to-name/exeptions.csv', 'r') as exeptions_file:
    readery = csv.reader(exeptions_file)
    l = list(readery)
    exeptions = []
    for sublist in l:
        for item in sublist:
            exeptions.append(item)


#lists = (line.strip() for line in exeptions_file)