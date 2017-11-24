import re
import operator
import csv

function = input("""Please select the function you would like to perform
(to select a function, enter the corresponding number)
1) Parse a .csv
2) Rank potential opportunies
------------------------------------------------------
> """)

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

def get_col_titles(i_dict, o_col_list):
    for title in i_dict.keys():
        if "company" in title.lower():
            continue
        else:
            o_col_list.append(title)

def count_all(i_dict, o_list, o_dict):
    for entry in i_dict.items():
        if "company" in entry[0].lower():
            continue

        for item in entry[1]:
            if "," in item:
                item = item.split(',')
                for word in item:
                    word = word.strip()
                    o_list.append(word)
            else:
                o_list.append(item)

    for item in o_list:
        if item == '':
            continue

        if item not in o_dict.keys():
            o_dict[item] = 1
        else:
            o_dict[item] += 1

    return o_dict







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
        get_col_titles(tech_dict, col_list)

        print("Detected the following columns -- which would you like to parse?")
        print("Type 'all' if you would like to parse all columns...")

        for col_title in col_list:
            print(col_title)
        col_choice = input("> ")




        if col_choice.lower() == 'all':
            col_choice = []
            col_choice_dict = {}

            print("Parsing all columns..." )
            count_all(tech_dict, col_choice, col_choice_dict)

            all_sorted = sorted(col_choice_dict.items(),
            key=operator.itemgetter(1), reverse=True)

            o_file = input("What would you like to name the output file?\n> ")
            o_file = o_file + ".txt"
            target = open(o_file, 'w')
            target.write("**ALL TECHNOLOGIES**\n\n")

            for item, count in all_sorted:
                target.write(str(item) + ": " + str(count) + "\n")

            target.close()

            print("Sort complete!")

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
