def createDictionary(filename):
    dictionary = {}
    with open(filename) as f:
        keys = f.readline().split(",")
        keys[-1] = keys[-1].replace("\n", "")   # Remove \n from end of line
        for line in f:
            line = line[:-1]  # Removes \n from end of line
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
        print(key, "is matched with",value)

def removeValueFromDictionary(dictionary, value):
    for key, valueList in dictionary.items():
        valueList.remove(value)
        dictionary[key] = valueList
    return dictionary

def decisionMakingAlgorithm():
    # Define global variables and regular variables
    global universityPref
    global studentPref
    global availableStudents
    global availableUniversities
    global decisions
    currStudentIndex = 0

    while(len(availableStudents) > 0):  # Runs the program as long as there are still matches to be made
        resetLoop = False
        
        for university in universityPref.keys():    # Loops through all universities in the university preference dictionary
            
            if(currStudentIndex < len(availableStudents)):  # Checks if the current index is out of bonunds                
                currStudent = universityPref[university][currStudentIndex]  # Sets the current tsudent to be matched
                
                if((currStudent in availableStudents) and (university in availableUniversities)):   # If the student and university are both available for matches
                    
                    if(studentPref[currStudent][0] == university):
                        decisions[currStudent] = university # Remove all instances of the student and university from both dictionaries
                        
                        # Remove all instances of the student and university from both dictionaries
                        availableStudents.remove(currStudent)
                        availableUniversities.remove(university)
                        studentPref = removeValueFromDictionary(studentPref, university)
                        universityPref = removeValueFromDictionary(universityPref, currStudent)
                        
                        resetLoop = True    # Reset the loop and indices
        
        if (resetLoop):
            currStudentIndex = 0
        else:
            currStudentIndex += 1


# Passes filenames to function which returns the generated dictionary
universityPref = createDictionary("school-preferences.txt")
studentPref = createDictionary("student-preferences.txt")

# Creates lists using the keys from a dictionary
availableStudents = list(studentPref.keys())
availableUniversities = list(universityPref.keys())

# Creates an empty dictionary with an associated list
decisions = dict(zip(availableStudents, [None]*len(availableStudents)))

decisionMakingAlgorithm()

printDictionary(decisions)


    



