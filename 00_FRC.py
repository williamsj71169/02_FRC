# ?


def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# main stuff
get_int = num_check("How many do you need?", "Please enter an amount more than 0\n", int)


get_cost = num_check("How many does it cost?", "Please enter an amount more than 0\n", float)
