"""
    Simple program to demonstrate three different type of debugging
    1. print statements
    2. copy-paste into the Python Tutor
    3. using pdb

    The code shown below has at least 4 problems:
    * ONE Runtime error that crashes the program, and
    * THREE bugs that let the program run but produce the wrong result
"""

def do_a_sum(n):
    """ This is a multi-line Docstring: gives a brief explanation

        It optionally provides more detail of what this function does
        with the use of a few additional lines, followed by a description
        of the input parameters and returned values.

        NOTE: THIS FUNCTION HAS 3 BUGS!!! (on purpose)

        Params:
            n: an integer input to set the loop

        Returns:
            the addition of 1 up to the number n
    """
    print ("IN do_a_sum()") # Debug print
    if n <= 0 or n > 10:
        print ("Try again but with a number in [1, 10]")
        return -1

    # an accummulator variable (for the sum)
    my_sum = 0

    # The loop that accummulates the addition
    for x in range(1, n + 1): #
        my_sum = x + my_sum #

    return my_sum


def main():
    """ A one-line Docstring: simple explanation of what this function does """

    # NOTE: THIS FUNCTION CAUSES 1 RUNTIME ERROR!!! (on purpose)

    #First line... a comment
    print ("First line of executable code... IN main()") # Debug print
    user_input = input("Give me one integer: ")
    if user_input.isdigit():
        print ("IN main()... if is digit") # Debug print
        result = do_a_sum(int(user_input))
        if result != -1:
            print( f"Sum from 1 to {user_input}: {result}")
        else:
            print("Picked a number outside [1,10]")
    else:
        print ("I said 'an integer'! ")
    print("Done") # Debug print

if "__main__" == __name__:
    main()
