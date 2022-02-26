# INF360 - Programming in Python
# Krushil Naik
# Assignment 3


# (5/5 points) Create a dictionary for each vehicle
# that contains the fields/keys and values listed above.
car01 = {
    "Name": "Ka",
    "Year Introduced": 1996,
    "Production of the Current Model": 2014,
    "Generation": "3rd",
    "Vehicle Information": "Developed by Ford Brazil as a super mini car"
}

car02 = {
    "Name": "Fiesta",
    "Year Introduced": 1976,
    "Production of the Current Model": 2017,
    "Generation": "7th",
    "Vehicle Information": "Ford's long running subcompact line based on global B-car Platform"
}

car03 = {
    "Name": "Focus",
    "Year Introduced": 1998,
    "Production of the Current Model": 2018,
    "Generation": "3rd",
    "Vehicle Information": "Ford's Compact car based on global C-car platform"
}

car04 = {
    "Name": "Mondeo",
    "Year Introduced": 1992,
    "Production of the Current Model": 2012,
    "Generation": "2nd",
    "Vehicle Information": 'Mid sized passenger sedan with "One-Ford" design based on CD4 platform'
}

car05 = {
    "Name": "Fusion",
    "Year Introduced": 2005,
    "Production of the Current Model": 2014,
    "Generation": "5th",
    "Vehicle Information": "Similar to Mondero"
}

car06 = {
    "Name": "Taurus",
    "Year Introduced": 1986,
    "Production of the Current Model": 2009,
    "Generation": "6th",
    "Vehicle Information": "Full sized car based on D3 platform"
}

car07 = {
    "Name": "Fiesta ST",
    "Year Introduced": 2013,
    "Production of the Current Model": 2013,
    "Generation": "1st",
    "Vehicle Information": "Fiesta's high performance factory tune"
}

car08 = {
    "Name": "Focus RS",
    "Year Introduced": 2015,
    "Production of the Current Model": 2015,
    "Generation": "1st",
    "Vehicle Information": "Special high performance Focus developed by SVT"
}

car09 = {
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


# (5/5 points) Write a function that will take a list of these dictionaries
# and return a new dictionary with the 'name' value as the key, and the dictionary as the value.
def toDictionary(_list: list):
    return {car["Name"]: car for car in _list}


# (5/5 points) Write a function that will go through the newly created dictionary
# and return a list of all the car's names, sorted alphabetically.
def getNames(_dict: dict):
    return sorted(_dict.keys())


# (5/5 points) Write a function that will go through the newly created dictionary
# return a dictionary of all the cars names and year introduced.
def getNamesAndYears(_dict: dict):
    return {car["Name"]: car["Year Introduced"] for car in _dict.values()}


# just a helper function
def printEach(things: list):
    print(*things, sep="\n")


carDatabase = toDictionary([
    car01, car02, car03, car04, car05,
    car06, car07, car08, car09, car10,
])

# (5/5 points) Use a print statement to show the results of the function from step 3,
# each on their own line.
printEach(getNames(carDatabase))

print()
print("=====================================")
print()

namesAndYears = list(getNamesAndYears(carDatabase).items())
namesAndYears.sort(key=lambda x: x[-1])

# (5/5 points) Use a print statement to show the results of the function from step 4
# to display in the format: year : name. Sort by year introduced.
printEach([f"{year} : {name}" for name, year in namesAndYears])
