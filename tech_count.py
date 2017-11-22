# nest a dict within a dictionary
from sys import argv
import re
import operator
import csv


# functions

def count_words(f, target_dict):
    for line in f:
        for word in line.split(','):
            word = word.strip()
            if "\t" in word:
                word = re.sub("\t", ', ', word)

            if word == '':
                continue
            else:
                if word not in target_dict.keys():
                    target_dict[word] = 1
                else:
                    target_dict[word] += 1

def to_txt():
    pass


## to enable file input at run using argv
# script, input_file = argv

## to enable output to new output file
# target = open('output_test.txt', 'w')


# defining init lists and dictionaries
tech_list = []
t_list2 = []
tech_dict = {}


# opening the .csv file (currently hardcoded)
with open('sample.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        items = list(row.items())
        tech_list.append(items)

# print(tech_list)

for item in tech_list:
    for key, value in item:
        if key not in tech_dict.keys():
            count = 1
            tech_dict[key] = [value] # dict = {value : count}
        elif key in tech_dict.keys():
            if value not in tech_dict[key]:
                tech_dict[key].append(value)





        # if key in tech_dict.keys():
        #     if value not in tech_dict[key].values():
        #         tech_dict[key] = {value : 0}
        #     else:
        #         continue



for entry in tech_dict.items():
    for item in entry[1]:
        if "," in item:
            item = item.split(',')
            for word in item:
                word = word.strip()
                t_list2.append(word)
        else:
            t_list2.append(item)



output_dict = {}
total_items = 0

for item in t_list2:
    if item == '':
        continue
    else:
        if item not in output_dict.keys():
            output_dict[item] = 1
        else:
            output_dict[item] += 1

    total_items += 1

output_sorted = sorted(output_dict.items(), key=operator.itemgetter(1), reverse=True)




for t in output_sorted:
    print(t)
print("\n" + str(total_items) + " total items in the list")
# target.write(str(tech_dict.items()))
# target.close()

print(tech_dict)










        # create the 'fruit' key in tech_dict







            # if title not in tech_dict.keys():
                # tech_dict[title] = value
            # print(title, value)
    # for row in reader:
    #     target.write(str(row.items()[0]) + "\n\n")

# print(tech_dict)

# target.close
# print("Complete")
