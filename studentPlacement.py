schoolPreferences = "school-preferences.txt"
studentPreferences = "student-preferences.txt"


def readPreferences(filename):

    preferences = {}
    with open(filename) as f:
        keys = f.readline().split(",")
        for line in f:
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


# def findBestMatching(studentPreferences, schoolPreferences):
#     """Finds the best matching of students to schools.

#     Parameters:
#         studentPreferences: a dictionary mapping students to lists of schools
#         schoolPreferences: a dictionary mapping schools to lists of students

#     Returns:
#         A dictionary mapping students to schools
#     """
#     matching = {}
#     for student in studentPreferences:
#         for school in getSchoolPreferences(student, studentPreferences, schoolPreferences):
#             if school not in matching:
#                 matching[student] = school
#                 break
#     return matching


# def getSchoolPreferences(student, studentPreferences, schoolPreferences):
#     """Returns a list of schools in order of preference for a student.

#     Parameters:
#         student: the name of the student
#         studentPreferences: a dictionary mapping students to lists of schools
#         schoolPreferences: a dictionary mapping schools to lists of students

#     Returns:
#         A list of schools in order of preference for the student
#     """
#     schools = []
#     for school in studentPreferences[student]:
#         if student in schoolPreferences[school]:
#             schools.append(school)
#     return schools

# Doing the following to remove \n from last key in dictionary because i could not find any other way to do it
schoolPref = readPreferences(schoolPreferences)
schoolPref["UofW"] = schoolPref["UofW\n"]
schoolPref.pop("UofW\n")
studentPref = readPreferences(studentPreferences)
studentPref["Alex"] = studentPref["Alex\n"]
studentPref.pop("Alex\n")
# print(schoolPref)
#print(" ")
#print(" ")
# print(studentPref)


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
