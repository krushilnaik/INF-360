# INF360 - Programming in Python
# Krushil Naik
# Assignment 3

# (5/5 points) Create a dictionary for each vehicle that contains the fields/keys and values listed above.
# (5/5 points) Write a function that will take a list of these dictionaries and return a new dictionary with the 'name' value as the key, and the dictionary as the value.
# (5/5 points) Write a function that will go through the newly created dictionary and return a list of all the car's names, sorted alphabetically.
# (5/5 points) Write a function that will go through the newly created dictionary return a dictionary of all the cars names and year introduced.
# (5/5 points) Use a print statement to show the results of the function from step 3, each on their own line.
# (5/5 points) Use a print statement to show the results of the function from step 4 to display in the format: year : name. Sort by year introduced.

def printEach(things: list):
    print(*things, sep="\n")


ka = {
    "name": "Ka",
    "yearIntroduced": 1996,
    "currentModel": 2014,
    "generation": "3rd",
    "information": "Developed by Ford Brazil as a super mini car "
}

fiesta = {
    "name": "Fiesta",
    "yearIntroduced": 1976,
    "currentModel": 2017,
    "generation": "7th",
    "information": "Ford's long running subcompact line based on global B-car Platform"
}

focus = {
    "name": "Focus",
    "yearIntroduced": 1998,
    "currentModel": 2018,
    "generation": "3rd",
    "information": "Ford's Compact car based on global C-car platform"
}

mondeo = {
    "name": "Mondeo",
    "yearIntroduced": 1992,
    "currentModel": 2012,
    "generation": "2nd",
    "information": 'Mid sized passenger sedan with "One-Ford" design based on CD4 platform'
}

fusion = {
    "name": "Fusion",
    "yearIntroduced": 2005,
    "currentModel": 2014,
    "generation": "5th",
    "information": "Similar to Mondero"
}

taurus = {
    "name": "Taurus",
    "yearIntroduced": 1986,
    "currentModel": 2009,
    "generation": "6th",
    "information": "Full sized car based on D3 platform"
}

fiesta_st = {
    "name": "Fiesta ST",
    "yearIntroduced": 2013,
    "currentModel": 2013,
    "generation": "1st",
    "information": "Fiesta's high performance factory tune"
}

focus_rs = {
    "name": "Focus RS",
    "yearIntroduced": 2015,
    "currentModel": 2015,
    "generation": "1st",
    "information": "Special high performance Focus developed by SVT"
}

mustang = {
    "name": "Mustang",
    "yearIntroduced": 1964,
    "currentModel": 2014,
    "generation": "6th",
    "information": "Ford's long running pony/muscle car"
}

gt = {
    "name": "GT",
    "yearIntroduced": 2004,
    "currentModel": 2016,
    "generation": "2nd",
    "information": "Ford's limited production super car inspired by the legendary race car GT40"
}


def toDictionary(_list: list):
    return {_dict["name"]: _dict for _dict in _list}


def getNames(_dict: dict):
    return sorted(_dict.keys())


def getNamesAndYears(_dict: dict):
    return {_val["name"]: _val["yearIntroduced"] for _val in _dict.values()}


dictionary = toDictionary([
    ka,
    gt,
    fiesta, fiesta_st,
    focus, focus_rs,
    mondeo,
    fusion,
    taurus,
    mustang,
])

namesAndYears = list(getNamesAndYears(dictionary).items())
namesAndYears.sort(key=lambda x: x[-1])

printEach(getNames(dictionary))
print()
print("=====================================")
print()
printEach([f"{year} : {name}" for name, year in namesAndYears])
