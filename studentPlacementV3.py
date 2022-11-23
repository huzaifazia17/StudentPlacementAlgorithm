import pprint

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

universityPreferencesFile = "school-preferences.txt"
studentPreferencesFile = "student-preferences.txt"

# Passes filenames to function which returns the generated dictionary
universityPref = createDictionary(universityPreferencesFile)
studentPref = createDictionary(studentPreferencesFile)

students = list(studentPref.keys())
universities = list(universityPref.keys())

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
    'Jane': '',
    'Alex': ''
}

availableStudents = list(students)
availableUniversities = list(universities)

key_list = list(matches.keys())

while len(availableStudents) > 0:
    for student in key_list:
        for university in studentPref[student]:
            if student in list(availableStudents):
                if university not in list(matches.values()):
                    matches[student] = university
                    availableStudents.remove(student)
                    print('{} is linked to {}!'.format(student, university))
                    break
                elif university in list(matches.values()):
                    current_suitor = list(matches.keys())[list(matches.values()).index(university)]
                    u_list = universityPref.get(university)
                    if u_list.index(student) < u_list.index(current_suitor):
                        matches[student] = university
                        availableStudents.remove(student)
                        matches[current_suitor] = ''
                        availableStudents.append(current_suitor)
                        print('{} was previously paired to {} but now is paired with {}! '.format(university, current_suitor, student))
                        break

print()
printDictionary(matches)



