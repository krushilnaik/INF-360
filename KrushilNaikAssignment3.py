# INF360 - Programming in Python
# Krushil Naik
# Assignment 3

# (5/5 points) Create a dictionary for each vehicle that contains the fields/keys and values listed above.
# (5/5 points) Write a function that will take a list of these dictionaries and return a new dictionary with the 'name' value as the key, and the dictionary as the value.
# (5/5 points) Write a function that will go through the newly created dictionary and return a list of all the car's names, sorted alphabetically.
# (5/5 points) Write a function that will go through the newly created dictionary return a dictionary of all the cars names and year introduced.
# (5/5 points) Use a print statement to show the results of the function from step 3, each on their own line.
# (5/5 points) Use a print statement to show the results of the function from step 4 to display in the format: year : name. Sort by year introduced.

# just a helper function
def printEach(things: list):
    print(*things, sep="\n")


car1 = {
    "Name": "Ka",
    "Year Introduced": 1996,
    "Production of the Current Model": 2014,
    "Generation": "3rd",
    "Vehicle Information": "Developed by Ford Brazil as a super mini car"
}

car2 = {
    "Name": "Fiesta",
    "Year Introduced": 1976,
    "Production of the Current Model": 2017,
    "Generation": "7th",
    "Vehicle Information": "Ford's long running subcompact line based on global B-car Platform"
}

car3 = {
    "Name": "Focus",
    "Year Introduced": 1998,
    "Production of the Current Model": 2018,
    "Generation": "3rd",
    "Vehicle Information": "Ford's Compact car based on global C-car platform"
}

car4 = {
    "Name": "Mondeo",
    "Year Introduced": 1992,
    "Production of the Current Model": 2012,
    "Generation": "2nd",
    "Vehicle Information": 'Mid sized passenger sedan with "One-Ford" design based on CD4 platform'
}

car5 = {
    "Name": "Fusion",
    "Year Introduced": 2005,
    "Production of the Current Model": 2014,
    "Generation": "5th",
    "Vehicle Information": "Similar to Mondero"
}

car6 = {
    "Name": "Taurus",
    "Year Introduced": 1986,
    "Production of the Current Model": 2009,
    "Generation": "6th",
    "Vehicle Information": "Full sized car based on D3 platform"
}

car7 = {
    "Name": "Fiesta ST",
    "Year Introduced": 2013,
    "Production of the Current Model": 2013,
    "Generation": "1st",
    "Vehicle Information": "Fiesta's high performance factory tune"
}

car8 = {
    "Name": "Focus RS",
    "Year Introduced": 2015,
    "Production of the Current Model": 2015,
    "Generation": "1st",
    "Vehicle Information": "Special high performance Focus developed by SVT"
}

car9 = {
    "Name": "Mustang",
    "Year Introduced": 1964,
    "Production of the Current Model": 2014,
    "Generation": "6th",
    "Vehicle Information": "Ford's long running pony/muscle car"
}

car10 = {
    "Name": "GT",
    "Year Introduced": 2004,
    "Production of the Current Model": 2016,
    "Generation": "2nd",
    "Vehicle Information": "Ford's limited production super car inspired by the legendary race car GT40"
}


def toDictionary(_list: list):
    return {_dict["Name"]: _dict for _dict in _list}


def getNames(_dict: dict):
    return sorted(_dict.keys())


def getNamesAndYears(_dict: dict):
    return {_val["Name"]: _val["Year Introduced"] for _val in _dict.values()}


dictionary = toDictionary([
    car1, car2, car3, car4, car5,
    car6, car7, car8, car9, car10,
])

namesAndYears = list(getNamesAndYears(dictionary).items())
namesAndYears.sort(key=lambda x: x[-1])

printEach(getNames(dictionary))
print()
print("=====================================")
print()
printEach([f"{year} : {name}" for name, year in namesAndYears])
