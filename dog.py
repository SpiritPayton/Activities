# initialise variables
dogList = []
cost = 22.50
days = 0

# This function runs the main program and coordinates calls to other functions
def main_routine():
    choice = 0

    while choice != 5:
        print("---------------------------------------------")
        print("Welcome to DogsRus!")
        print("What would you like to do? Choose one of the items below")
        print("---------------------------------------------")
        print()
        print("1: Drop off a dog")
        print("2: Pick up a dog")
        print("3: Calculate cost")
        print("4: Print Roll")
        print("5: Exit the system")
        print()
        choice = int(input("Enter your choice (number between 1 and 5):"))
        print()

        if choice == 1:
            dropOff()

        elif choice == 2:
            pickUp()

        elif choice == 3:
            calcCost()

        elif choice == 4:
            printRoll()

        else:
            quit()

def dropOff():
    dogName = input("What is the dog's name?: ").upper()
    dogList.append(dogName)
    return dogList

def pickUp():
    dogFound = bool(False)
    while dogFound == False:
        dogName = input("What is the dog's name): ").upper()
        if dogName in dogList:
            dogFound = True
            dogList.remove(dogName)
            print(f"{dogName} has been checked out")
        else:
            print("Dog not found. Please check the dog's name.")

def calcCost():
    days = int(input("Enter the number of days: "))
    print(f"The total charge is ${len(dogList) * cost * days}")

def printRoll():
    print(dogList)


def quit():
    print("Thank you for using DogsRus! Goodbye!")


main_routine()
