schoolPreferences = "school-preferences.txt"
studentPreferences = "student-preferences.txt"


def readPreferences(filename):

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

# Passes filenames to function which returns the generated dictionary
schoolPref = readPreferences(schoolPreferences)
studentPref = readPreferences(studentPreferences)

print(studentPref)
print()
print(schoolPref)


# Check if students first choice is available, if not check if some shcool has that student as first choice, else iterate


def findBestMatching(studentPref, schoolPref):
    studentsList = list(studentPref.keys())
    schoolList = list(schoolPref.keys())
    # print(schoolList)
    matchingList = {}
    i = 0
    for student, studentchoice in studentPref.items():
        print(studentchoice)
        # if studentchoice[i] in schoolList:
        if (studentchoice[i] in schoolList):
            matchingList[student] = studentchoice[i]
            schoolList.remove(studentchoice[i])
        elif (studentchoice[i] not in schoolList):
            for school, schoolchoice in schoolPref.items():
                if (student == schoolchoice[i] and studentchoice[i] in schoolList):
                    matchingList[student] = school
                    schoolList.remove(school)

    return matchingList


print("Matching: ", findBestMatching(studentPref, schoolPref))
