# Program to calculate the average age of kids at Kidz Fun holiday programme

child_list = []

# this function runs the main program and calls to other functions


def main_routine():
    programme = ""
    number_of_active_kidz = 0
    number_of_fun_in_sun = 0
    total_age_active_kidz = 0
    total_age_fun_in_sun = 0

    while programme != "X":
        print("---------------------------------------")
        print("Welcome! Here are our holiday programmes: ")
        print("1: Fun in the Sun")
        print("2: Active Kidz")
        programme = input("Which holiday programme is your child attending? ").upper()
        if programme == "ACTIVE KIDZ":
            number_of_active_kidz += 1
            age = int(input("Please enter your child's age in years: "))
            total_age_active_kidz += age
        elif programme == "FUN IN THE SUN":
            number_of_fun_in_sun += 1
            age = int(input("Please enter your child's age in years: "))
            total_age_fun_in_sun += age
        elif programme == "X":
            print_info(number_of_active_kidz, total_age_active_kidz, number_of_fun_in_sun, total_age_fun_in_sun)


def print_info(number_of_active_kidz, total_age_active_kidz, number_of_fun_in_sun, total_age_fun_in_sun):
    print(f"The total number of children in Active Kidz is {number_of_active_kidz}.")
    print(f"The average age of children in Active Kidz is {total_age_active_kidz / number_of_active_kidz}.")
    print()
    print(f"The total number of children in Fun in the Sun is {number_of_fun_in_sun}.")
    print(f"The average age of children in Fun in the Sun is {total_age_fun_in_sun / number_of_fun_in_sun}.")


main_routine()
