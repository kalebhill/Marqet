import re
import operator
import csv

function = input("""Please select the function you would like to perform
(to select a function, enter the corresponding number)
1) Parse a .csv
2) Rank potential opportunies
------------------------------------------------------
>""")

# functions

def get_csv():
    while True:
        input_f = input("Enter the .csv file you would like to parse\n> ")
        # maybe use [-4:0] == '.csv' to make sure .csv is the extension
        if ".csv" in input_f:
            return input_f
        else:
            print("Please enter a file with a .csv extension\n")

def open_csv(i_file, o_list):
    with open(i_file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            items = list(row.items())
            o_list.append(items)
    return o_list

def convert_csv_list(i_list, o_dict):
    for item in i_list:
        for key, value in item:
            if key not in o_dict.keys():
                o_dict[key] = [value]
            elif key in o_dict.keys():
                if value not in o_dict[key]:
                    o_dict[key].append(value)

# def get_col_titles(i_dict, o_col_list):
#     for entry in i_dict.items():
#         if "company" in entry[0].lower():
#             continue
#
#         title = entry[0]
#         for title in i_dict.items():
#             o_col_list.append(title)
#
#     return o_col_list


 # Branch to parse a .csv
while True:
    if int(function) == 1:
        # create an empty list & dictionary
        tech_list = []
        tech_dict = {}
        col_list = []

        # prompt the user to enter a file containing .csv
        input_csv = get_csv()

        # open the csv file, output to empty list
        open_csv(input_csv, tech_list)

        # convert list to dictionary
        convert_csv_list(tech_list, tech_dict)

        # debug check
        # for item in tech_dict.items():
        #     print(item)

        # get column titles from tech_dict

        print(col_list)

        break
    elif int(function) == 2:
        print("You chose option 2!")
        break
    else:
        print("Please enter a valid option, or press CTRL-C to exit.")



# if int(function) == 2:
#         while True:
#             input_f = input("Enter the .csv file you would like to parse\n> ")
#             if ".csv" in input_f:
#                 break
#             else:
#                 print("Please enter a file with a .csv extension\n")
