import pprint

def createDictionary(filename):
    preferences = {}
    with open(filename) as f:
        keys = f.readline().split(",")
        keys = keys[:-1]  # Remove \n from end of line
        for line in f: #TEST
            line = line[:-1]  # Remove \n from end of line
            values = line.split(",")
            for i in range(len(keys)):
                key = keys[i]
                value = values[i]
                if key in preferences:
                    preferences[key].append(value)
                else:
                    preferences[key] = [value]
    return preferences

def printDictionary(dictionary):
    for key, value in dictionary.items() :
        print(key, value)

schoolPreferencesFile = "school-preferences.txt"
studentPreferencesFile = "student-preferences.txt"

# Passes filenames to function which returns the generated dictionary
schoolPref = createDictionary(schoolPreferencesFile)
studentPref = createDictionary(studentPreferencesFile)

printDictionary(schoolPref)
print()
printDictionary(studentPref)

# Stores the final descisions
matches = {
    'Tom':  '',
    'Sara': '',
    'Ali': '',
    'Ying': '',
    'Amit': '',
    'Megan': '',
    'Alan': '',
    'Layla': '',
    'Jane': ''
    }


