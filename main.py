
symbol_to_name = {
    "o2": "oxygen",
    "co2": "carbon dioxide",
    "cl2": "chlorine",
    "znso4": "zinc sulfate",
    "cuso4": "copper sulfate",
    "s04": "sulfate",
    "k2cr2o7": "potassium dichromate",
}

name_to_symbol = {value: key for key, value in symbol_to_name.items()}

def converter():
    prompt = input("Enter a symbol of a chemical compound OR TYPE q TO QUIT: ")
    
    for symbol in symbol_to_name:
        if prompt in symbol_to_name:
            to = "name"
        elif prompt == "q":
            break
        else:
            for name in name_to_symbol:
                if prompt in name_to_symbol:
                    to = "symbol"
                else:
                    print("Not found in our database")
                    return True

    if prompt == "q":
        print("Thank You!")
        return False
    elif to == "name":
        print(symbol_to_name[prompt])
    elif to == "symbol":
        print(name_to_symbol[prompt])

while converter() is not False:
        converter()
        

