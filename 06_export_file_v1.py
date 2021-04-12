import pandas

# frames and content for export

variable_dict = {
    "Item": ["Mugs", "Printing", "Packaging"],
    "Quantity": [300, 300, 50],
    "Price": [1, .5, .75]
}

fixed_dict = {
    "item": ["Rent", "Artwork", "Advertising"],
    "price": [25, 35, 10]
}

variable_frame = pandas.DataFrame(variable_dict)
fixed_frame = pandas.DataFrame(fixed_dict)

product_name = "Custom Mugs"
profit_target = "$100.00"
required_sales = "$200.00"
recommended_price = "$5.00"

print(variable_frame)

# change data frame to string (so it can be writen to a txt file)
variable_txt = pandas.DataFrame.to_string(variable_frame)

# write to file...
# create file to hold data (add .txt extension)
file_name = "{}.txt".format(product_name)
text_file = open(file_name, "w+")

# heading
text_file.write("*** Fund Raising - {}"
                "***\n\n".format(product_name))

text_file.write(variable_txt)

#


# close file
text_file.close()

