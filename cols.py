import re
import operator
import csv

tech_list = []

with open('banking_sample_large.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        items = list(row.items())
        tech_list.append(items)

col_choice = input("Column Choice? ")

if col_choice.title() in tech_dict.keys():
    col_list = []
    col_dict = {}

    for items in tech_dict[col_choice.title()]:
        if "," in items:
            items = items.split(',')


            for item in items:
                if item == '' or item == ' ':
                    continue
                else:
                    col_list.append(item)

        for item in col_list:
            if item not in col_dict:
                item = item.strip()
                col_dict[item] = 1
            else:
                col_dict[item] += 1

    col_dict = sorted(col_dict.items(), key=operator.itemgetter(1),
    reverse=True)

    # print(col_dict)

    o_file = input("What would you like to name the output file?\n> ")
    o_file = o_file + ".txt"
    target = open(o_file, 'w')
    target.write("**" + col_choice.title() + "**\n\n")

    for tech, count in col_dict:
        target.write(str(tech) + ": " + str(count) + "\n")

    target.close()
    print("Completed!")
