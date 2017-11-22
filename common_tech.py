# used_technologies = {}
#
# for technology in tech_list:v
#   if technology in used_technologies:
#     used_technologies['count'] += 1
#   else:
#     technology


# dict = {
#   'collaboration' :
#       { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#   'data bases' :
#       { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# }

## 1st version -- select all technologies (without titles) in a column and paste
## into a .txt file for parsing.


from sys import argv
import re
import operator

# script, input_file = argv

new_file = input("What would you like to name the output file? ")
new_file = new_file + '.txt'
target = open(new_file, 'w')

f = open(input_file)

tech_list = {}

for line in f:
    for word in line.split(','):
        word = word.strip()
        if "\t" in word:
            word = re.sub("\t", ', ', word)
        if word == '':
            continue
        else:
            if word not in tech_list.keys():
                tech_list[word] = 1
            else:
                tech_list[word] += 1


sorted_tech = sorted(tech_list.items(), key=operator.itemgetter(1), reverse=True)

for k, v in sorted_tech:
    target.write(f"{v} : {k}\n")

target.close

print("Print Completed")
