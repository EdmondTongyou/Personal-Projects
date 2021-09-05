# Bubble Sort Program
# Edmond Tongyou 09/03/2021
# Sorts list either from least to greatest and vice versa.
# Done without the use of sort function.

import random

notSorted = True
notValid = True
list = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 4, 5, 6]
random.shuffle(list)


while notValid:
    print("Would you like to sort from least to greatest or vice versa?")
    print("1 - Least to Greatest")
    print("2 - Greatest to Least")
    choice = input()

    if choice == "1" or choice == "2":
        notValid = False
    else:
        print("Invalid choice, please input a valid choice.")


if choice == "1":
    while notSorted:
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]

        if list == list2:
            notSorted = False


if choice == "2":
    list2.reverse()
    while notSorted:
        for i in range(len(list)-1):
            if list[i] < list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]

        if list == list2:
            notSorted = False


print(list)