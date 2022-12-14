import copy

def createDictionary(filename):
    dictionary = {}
    with open(filename) as f:
        keys = f.readline().split(",")
        keys[-1] = keys[-1].replace("\n", "")   # Remove \n from end of line
        for line in f:
            line = line[:-1]  # Remove \n from end of line
            values = line.split(",")
            for i in range(len(keys)):
                key = keys[i]
                value = values[i]
                if key in dictionary:
                    dictionary[key].append(value)
                else:
                    dictionary[key] = [value]
    return dictionary

def printDictionary(dictionary):
    for key, value in dictionary.items() :
        print(key, "-->",value)

def createEmptyDictionaryFromKeyList(keyList):
    # Initialize dictionary
    dictionary = {}
    
    # Iterating through the elements of list
    for i in keyList:
        dictionary[i] = ''
    return dictionary

def deleteValue(dictionary, lookUp):
    for key, valueList in dictionary.items():
        for i in range (0, len(valueList)):
            if (valueList[i] == lookUp):
                valueList[i] = 'XXX'
                dictionary[key] = valueList
    return dictionary

def removeValueFromDictionary(dictionary, value):
    for key, valueList in dictionary.items():
        valueList.remove(value)
        dictionary[key] = valueList
    return dictionary


# Passes filenames to function which returns the generated dictionary
universityPref = createDictionary("school-preferences.txt")
studentPref = createDictionary("student-preferences.txt")

studentPrefTEMP = copy.deepcopy(studentPref)
universityPrefTEMP = copy.deepcopy(universityPref)

availableStudents = list(studentPref.keys())
availableUniversities = list(universityPref.keys())

decisions = createEmptyDictionaryFromKeyList(availableStudents)

while(len(availableStudents) > 0):
    for i in range (0, len(studentPref.keys())):
        
        print("I-------------------------------", i)
        for university in universityPref.keys():
            print("I: ", i)
            if(i < len(availableStudents)):
                currStudent = universityPref[university][i]
                if((currStudent in availableStudents) and (university in availableUniversities)):
                    if(studentPref[currStudent][0] == university):

                        decisions[currStudent] = university
                        
                        # Remove all instances of the student and university from both dictionaries
                        availableStudents.remove(currStudent)
                        availableUniversities.remove(university)

                        studentPref = removeValueFromDictionary(studentPref, university)
                        universityPref = removeValueFromDictionary(universityPref, currStudent)

                        # studentPrefTEMP = deleteValue(studentPrefTEMP, university)
                        # universityPrefTEMP = deleteValue(universityPrefTEMP, currStudent)
                        # del studentPrefTEMP[currStudent]
                        # del universityPrefTEMP[university]

                        # print()
                        # print()
                        # printDictionary(studentPrefTEMP)
                        # printDictionary(studentPref)
                        # print()
                        # printDictionary(universityPrefTEMP)
                        # printDictionary(universityPref)
                        # print()
                        # print()
                        printDictionary(decisions)
                        print()
                        i = 0
                        # university = availableUniversities[0]
    



