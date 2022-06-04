#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description:


# This function converts a list of strings into a list of integers
def str_int(strings):
    ints = []
    for word in strings:
        new_num = int(word)
        ints.append(new_num)

    return ints

def find_sum_pairs(ints, num_sum):
    counter1 = 0
    n_pairs = []
    for a_num in ints:
        counter1 += 1
        counter2 = 0
        match_num = num_sum - a_num

        for number in ints:
            counter2 += 1
            if counter2 == counter1:
                continue

            if number == match_num:
                pair = "({} + {})".format(a_num, number)
                n_pairs.append(pair)

                for a_pair in n_pairs:
                    check_pair = "({} + {})".format(number, a_num)
                    if a_pair == check_pair:
                        n_pairs.pop()


    return n_pairs



# This function calculates the remainders of the numbers in the list divided by
# the entered divisor
def calc_remainders(ints, divisor):
    l_remainder = []
    for a_num in ints:
        div_num = a_num % divisor
        l_remainder.append(div_num)

    return l_remainder



def index_finder():
    print("This is index")



def sum_matcher():
    failure_loop2 = True
    l_str2 = []
    l_ints2 = []

    while failure_loop2:
        u_ints2 = input("Enter a list of integers (Each number must be separated"
        + " by \',\' followed by a space): ")

        l_str2 = u_ints2.split(", ")

        try:
            l_ints2 = str_int(l_str2)

            sum_failure = True

            while sum_failure:
                try:
                    u_sum = int(
                        input(
                            "Enter the integer that you would like the sum to be: "))
                    failure_loop2 = False
                    sum_failure = False
                    pairs = find_sum_pairs(l_ints2, u_sum)

                    if len(pairs) == 0:
                        print("There were no pairs adding up to {}".format(u_sum))
                    else:
                        print("The pairs of numbers that add up to {} are:".format(
                            u_sum))

                        for pair in pairs:
                            print(pair, end = "")


                except ValueError:
                    print("You didn't enter an integer! Try again.")
        except ValueError:
            print("There was something wrong with the list of integers")





def remainder():
    failure_loop = True
    l_str = []
    l_ints = []
    while failure_loop:
        u_ints = input("Enter a list of integers (Each number must be separated"
        + " by \',\' followed by a space): ")

        l_str = u_ints.split(", ")
        try:
            l_ints = str_int(l_str)

            div_failure = True
            while div_failure:
                try:
                    u_divisor = int(
                        input("Enter the integer you'd like to divide by: "))

                    div_failure = False
                    failure_loop = False
                    remainders = calc_remainders(l_ints, u_divisor)

                    for counter in range(len(remainders)):
                        print("The remainder of position {} is {}".format(
                            counter, remainders[counter]))

                except ValueError:
                    print("That was not a valid integer")
        except ValueError:
            print("There was something wrong with the list of numbers you "
            + "entered")


def main():
    restart_loop = True
    # Loop allows for the user to choose a new program once the calculations
    # are finished
    while restart_loop:
        retry_loop = True

        choice = input(
            "Choose a program to run: \n\n"
            + "1 - Remainder finder program \n2 - Sum matcher program "
            + "\n3 - Index finder program\n\n"
            + "Selection: "
        )
        # Calls whichever fnction was chosen
        if choice == "1":
            remainder()
        elif choice == "2":
            sum_matcher()
        elif choice == "3":
            index_finder()
        else:
            print("I don't understand, please try again!")

        while retry_loop:
            choice2 = input("\nWould you like to do something else? (y/n): ")
            # this is what decides whether or not to run the program again
            if choice2 == "y":
                retry_loop = False
            elif choice2 == "n":
                retry_loop = False
                restart_loop = False
            else:
                print("I don't understand, try again!")


if __name__ == "__main__":
    main()