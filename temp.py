def removeValueFromDictionary(dictionary, value):
    for key, valueList in dictionary.items():
        valueList.remove(value)
        dictionary[key] = valueList
    return dictionary


dictionary = {'UofO': ['Alex', 'Sara', 'Jane', 'Layla', 'Ying', 'Amit', 'Alan', 'Ali', 'Megan'], 'UofA': ['Ying', 'Alex', 'Megan', 'Amit', 'Sara', 'Jane', 'Alan', 'Layla', 'Ali'], 'OT': ['Alex', 'Jane', 'Megan', 'Ying', 'Sara', 'Layla', 'Ali', 'Amit', 'Alan'], 'UofT': ['Alan', 'Amit', 'Ying', 'Megan', 'Ali', 'Sara', 'Alex', 'Layla', 'Jane'], 'UBC': ['Layla', 'Alex', 'Megan', 'Jane', 'Sara', 'Ali', 'Alan', 'Ying', 'Amit'], 'QU': ['Jane', 'Sara', 'Amit', 'Ali', 'Alan', 'Ying', 'Layla', 'Megan', 'Alex'], 'YU': ['Sara', 'Jane', 'Alex', 'Ying', 'Ali', 'Layla', 'Alan', 'Megan', 'Amit'], 'CU': ['Ying', 'Alan', 'Layla', 'Ali', 'Megan', 'Sara', 'Amit', 'Jane', 'Alex'], 'MU': ['Alan', 'Layla', 'Megan', 'Sara', 'Alex', 'Jane', 'Ali', 'Amit', 'Ying'], 'UofW': ['Jane', 'Ali', 'Amit', 'Megan', 'Layla', 'Ying', 'Alex', 'Sara', 'Alan']}

currStudent = 'Alex'
