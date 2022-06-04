#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description:


# This function converts a list of strings into a list of integers. Each program
# needs to do this, so I just made a function once so I wouldn't need to write
# the code multiple times
def str_int(strings):
    ints = []
    for word in strings:
        new_num = int(word)
        ints.append(new_num)

    return ints


# this function finds the pairs of numbers in the list that add up to the
# desired sum. It purposefuly excludes repeats or the case where the numbers are
# just switched around. ie. it will only have (7 + 3) = 10 in a list with
# 7, 5, 3, 3, 8, 9.
# This function took a lot of thinking and was a fun little challenge
def find_sum_pairs(ints, num_sum):
    counter1 = 0

    n_pairs = []
    # first loop is to find what each element needs as a complement to
    # achieve the desired sum
    for a_num in ints:
        counter1 += 1
        counter2 = 0
        match_num = num_sum - a_num
        # second loop is to check if the complement is found
        for number in ints:
            counter2 += 1
            counter3 = 0
            # This basically checks to make sure both loops aren't referencing
            # the same index in the list. If they are it will skip whatever is
            # below and will continue the loop
            if counter2 == counter1:
                continue
            # If the complement is found, it formats it into a string and adds
            # it to the list
            if number == match_num:
                pair = "({} + {})".format(a_num, number)
                n_pairs.append(pair)
                # This loop checks to make sure that it only counts a pair one
                # time. Ie. instead of having (7 + 3) and (3 + 7) it will only
                # have (7 + 3) because this is all that the user needs
                for a_pair in n_pairs:
                    # this makes the inverse of the last pair
                    check_pair = "({} + {})".format(number, a_num)
                    # if the inverse of the pair is in the list, it will
                    # pop/remove that pair from the list. This portion excludes
                    # the case of two numbers being the same, because it would
                    # remove it even though it wasn't already in the list. Ie.
                    # (5 + 5) is the inverse of (5 + 5) so they would both be
                    # removed.
                    if (a_pair == check_pair) and (a_num != number):
                        n_pairs.pop()

                    counter4 = 0
                    counter3 += 1
                    # this loop takes care of the case where two numbers are the
                    # same. Ie. (5 + 5)
                    for d_pair in n_pairs:
                        counter4 += 1
                        # again this ensures the loops aren't referencing the
                        # same index in the list
                        if counter4 == counter3:
                            continue
                        # This will pop/remove the element if it there is one
                        # just like it somewhere else in the list.
                        if a_pair == d_pair:
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


# This function finds the index of the desired element in the list
def find_index(ints, number):
    found = -1
    for counter in range(len(ints)):
        if ints[counter] == number:
            return counter

    return found


# This is the function that gets all the necessary input to find the index of
# the desired element in the list
def index_finder():
    failure_loop3 = True
    l_str3 = []
    l_ints3 = []
    # Loop allows for the list to be re-entered incase of invalid input
    while failure_loop3:
        u_ints3 = input(
            "Enter a list of integers (Each number must be separated"
            + " by ',' followed by a space): "
        )
        # Splitting at the commas
        l_str3 = u_ints3.split(", ")

        try:
            # calls a func to converst strings to ints inside list
            l_ints3 = str_int(l_str3)

            index_failure = True
            # Allows for the desired element to be re-entered incase of invalid
            # input
            while index_failure:
                try:
                    find = int(input("Enter the integer you are looking for: "))

                    index_failure = False
                    failure_loop3 = False
                    # Calls the function that will return the index of the
                    # desired element in the list of numbers
                    index = find_index(l_ints3, find)
                    # Displaying results to user
                    if index != -1:
                        print(
                            "The first index of the number {} is {}".format(find, index)
                        )
                    else:
                        print("{} was not in the list!".format(find))

                except ValueError:
                    print("The integer you entered wasn't a real integer")
        except ValueError:
            print("There was something wrong with the list of integers entered")


# THis is the function that gets all the necessary input to find the pairs that
# equal the desired sum
def sum_matcher():
    failure_loop2 = True
    l_str2 = []
    l_ints2 = []
    # Loop allows for the list to be re-entered incase of invalid input
    while failure_loop2:
        u_ints2 = input(
            "Enter a list of integers (Each number must be separated"
            + " by ',' followed by a space): "
        )
        # Splitting at the commas
        l_str2 = u_ints2.split(", ")

        try:
            # calls a func to converst strings to ints inside list
            l_ints2 = str_int(l_str2)

            sum_failure = True
            # allows for the desired sum to be re-entered incase of invalid input
            while sum_failure:
                try:
                    u_sum = int(
                        input("Enter the integer that you would like the sum to be: ")
                    )
                    failure_loop2 = False
                    sum_failure = False
                    # Calls the function that will return a list of the pairs of
                    # elements that add up to the desired sum
                    pairs = find_sum_pairs(l_ints2, u_sum)

                    # Displaying results to user
                    if len(pairs) == 0:
                        print("There were no pairs adding up to {}".format(u_sum))
                    else:
                        print(
                            "The pairs of numbers that add up to {} are:".format(u_sum)
                        )

                        for pair in pairs:
                            print(pair, end="")

                except ValueError:
                    print("You didn't enter an integer! Try again.")
        except ValueError:
            print("There was something wrong with the list of integers")


# this is the function that gets all the necessary input to find the remainders
# of every index in the entered list
def remainder():
    failure_loop = True
    l_str = []
    l_ints = []
    # Loop allows for the list to be re-entered incase of invalid input
    while failure_loop:
        u_ints = input(
            "Enter a list of integers (Each number must be separated"
            + " by ',' followed by a space): "
        )

        # Splitting at the commas
        l_str = u_ints.split(", ")
        try:
            # calls a func to converst strings to ints inside list
            l_ints = str_int(l_str)

            div_failure = True
            # This function allows for the divisor to be re-entered incase of
            # invalid input
            while div_failure:
                try:
                    u_divisor = int(
                        input("Enter the integer you'd like to divide by: ")
                    )

                    div_failure = False
                    failure_loop = False
                    # Calls the function that will calculate the remainders of
                    # each element divided by the divisor
                    remainders = calc_remainders(l_ints, u_divisor)
                    # Displays results to screen
                    for counter in range(len(remainders)):
                        print(
                            "The remainder of position {} is {}".format(
                                counter, remainders[counter]
                            )
                        )

                except ValueError:
                    print("That was not a valid integer")
        except ValueError:
            print("There was something wrong with the list of numbers you " + "entered")


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
