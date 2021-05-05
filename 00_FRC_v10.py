# import libraries
import pandas
import math

# ***** Functions Go Here *****


# checks that input is either a float or an integer that is more that zero
# takes in custom error messages.
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


# check that string is not blank
def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("[]. \nPlease try again. \n".format(error))
            continue

        return response


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# gets expenses, returns list which has the data frame and sub total
def get_expenses(var_fixed):
    # set up dictionary and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }
    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name, quantity and item
        item_name = not_blank("* Item name:", "The component name can't be blank.")

        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":
            print()
            quantity = num_check("Quantity:", "The amount must be a whole number more then zero", int)

        else:
            quantity = 1

        print()
        price = num_check("How much for a single item? $", "The price must be a number <more than 0>", float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # find sub total
    sub_total = expense_frame['Cost'].sum()

    # currency formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]


# prints expense frames
def expense_print(heading, frame, subtotal):
    print()
    print("*** {} Costs ***".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))
    return ""


# work out profit goal and total sales required
def profit_goal(total_costs):

    # Initialise variables and error message
    error = "please enter a valid profit goal\n"

    valid = False
    while not valid:

        # ask for profit goal...
        print()
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
            print()
            dollar_type = yes_no("Do you mean ${:.2f}. "
                                 "ie ${:.2f} dollars? ,"
                                 "(y/n)". format(amount, amount))
            print()

            # set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no("Do you mean {}%? ,"
                                  "(y/n)".format(amount))
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


# rounding function
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


# string checker
def string_check(choice, options):

    is_valid = ""
    chosen = ""

    for var_list in options:

        # if the snack is in one of the lists, return the full name
        if choice in var_list:

            # Get full name of snack and put it
            # in title case so it locks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen snack is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


# function to show instructions if necessary
def instructions(options):
    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = yes_no("*** Would you like to read the instructions? (y/n) ")
        show_help = string_check(show_help, options)

    if show_help == "Yes":
        print()
        print("*** Instructions ***")
        print()
        print("* Answer all the questions asked in the way you will be asked to. *")

    return ""

# ***** Main Stuff *****

# valid options for yes/no questions
y_n = [
    ["yes", "y"],
    ["no", "n"]
]

instructions(y_n)

# get product name
print()
product_name = not_blank("* Product name: ", "The product name can't be blank.")
print()

how_many = num_check("How many items will you be producing?",
                     "The number of items must be a whole number more than zero", int)

print()
print("** Please enter your variable costs below...")
# get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("** Do you have fixed costs? (y/n)")

if have_fixed == "yes":
    # get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]
else:
    fixed_sub = 0
    fixed_frame = 0

# work out total costs and profit target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal(all_costs)

# calculates total sales needed to reach goal
sales_needed = all_costs + profit_target

# ask user for rounding
round_to = num_check("Round to nearest...? $", "Can't be zero", int)
print()

# calculate recommended price
selling_price = sales_needed / how_many
# print("Selling Price (unrounded): ${:.2f}".format(selling_price))

# recommended price
recommended_price = round_up(selling_price, round_to)

# write data to file
write_to_file = yes_no("Would you like the data writen to file? (y/n) ")
if write_to_file == "yes":

    variable_txt = pandas.DataFrame.to_string(variable_frame)
    if have_fixed == "yes":
        fixed_txt = pandas.DataFrame.to_string(fixed_frame)
    else:
        fixed_txt = 0

    # write to file...
    # create file to hold data (add .txt extension)
    file_name = "{}.txt".format(product_name)
    text_file = open(file_name, "w+")

    # heading
    text_file.write("*** Fund Raising - {}"
                    "***\n\n".format(product_name))

    # list holding stuff to print / write to file
    to_write = [variable_txt, fixed_txt]

    # write to file...
    # create file to hold data (add .txt extension)
    file_name = "{}.txt".format(product_name)
    text_file = open(file_name, "w+")

    title_write = "*** Fund Raising - {} *** \n \n".format(product_name)
    text_file.write(title_write)

    # heading
    for item in to_write:
        text_file.write(str(item))
        text_file.write("\n\n")

    total_cost_write = "Total Cost: ${:.2f} \n \n".format(all_costs)
    text_file.write(total_cost_write)

    profit_sales_write = "Profit & Sales Targets: \n \n Profit Target: ${:.2f} \n " \
                         "Total Sales: ${:.2f} \n \n".format(profit_target, all_costs + profit_target)
    text_file.write(profit_sales_write)

    # pricing
    pricing_write = "Pricing: \n \n Minimum Price: ${:.2f} \n " \
                    "Recommended Price: ${:.2f}".format(selling_price, recommended_price)
    text_file.write(pricing_write)

    # close file
    text_file.close()

else:
    print()


# *** Printing area ***

print()
print("*** Fund Raising - {} ***".format(product_name))
print()
expense_print("Variable", variable_frame, variable_sub)

if have_fixed == "yes":
    expense_print("Fixed", fixed_frame[['Cost']], fixed_sub)

print()
print("*** Total Costs: ${:.2f} ***".format(all_costs))
print()

print()
print("*** Profit & Sales Targets ***")
print("Profit Target: ${:.2f}".format(profit_target))
print("Total Sales: ${:.2f}".format(all_costs + profit_target))

print()
print("*** Pricing ***")
print("Minimum Price: ${:.2f}".format(selling_price))
print("Recommended Price: ${:.2f}".format(recommended_price))
