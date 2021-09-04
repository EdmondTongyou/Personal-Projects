# Tower of Hanoi Program
# Edmond Tongyou, 09/03/2021


inputValid = False

while inputValid == False:
    print("Please type the Largest Disk Size")
    largest_disk_size = input()

    if largest_disk_size.isdigit():
        inputValid = True
        
    else:
        print("Invalid Input")
