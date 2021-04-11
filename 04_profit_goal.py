# functions go here


# checks that user has entered yes / no to a question
def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no...\n")


def profit_goal(total_costs):

    # Initialise variables and error message
    error = "please enter a valid profit goal\n"

    valid = False
    while not valid:

        # ask for profit goal...
        response = input("What is your profit goal (eg $500)")
        # check if first character is $...
        if response[0] == "$":
            profit_type = "$"
            # get amount (everything after $)
            amount = response[1:]

        # check if last character is %
        elif response[-1] == "%":
            profit_type = "%"
            # get amount (everything before the &)
            amount = response[:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no("Do you mean ${:.2f}. "
                                 "ie ${:.2f} dollars? ,"
                                 "y / n". format(amount, amount))

            # set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no("Do you mean {}%? ,"
                                  " y / n".format(amount))
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main stuff
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal


# main stuff here
all_costs = 200

# loop for quick testing
for item in range(0, 6):
    profit_target = profit_goal(all_costs)
    print("Profit Target: ${:.2f}".format(profit_target))
    print("Total Sales: ${:.2f}".format(all_costs + profit_target))
    print()
