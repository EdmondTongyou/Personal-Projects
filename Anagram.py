def isAnagram(stringA, stringB):
    listA = []
    listB = []
    _stringA = stringA.lower()
    _stringB = stringB.lower()
    if len(_stringA) != len(_stringB):
        return False

    for i in range(0, len(_stringA)):
        listA.append(_stringA[i])
    for i in range(0, len(_stringB)):
        listB.append(_stringB[i])

    listA.sort()
    listB.sort()
    if listA != listB:
        return False

    return True

choice = "y"
while(choice != "n"):

    print("Enter a string:")
    stringA = input(stringA)
    print("Enter another string:")
    stringB = input(stringB)
    print("Are", stringA, "and", stringB, "Anagrams?")
    print(isAnagram(stringA, stringB))
    print("CONTINUE? (y/n)")
    choice = ""
    choice = input(choice)
    stringA = ""
    stringB = ""