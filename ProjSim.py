'''
Author Name = Anjie Zhao
GT ID: 903334981
'''

fName = input("What is the file name?")
f = open(fName, 'r')
fileInput = open('input.txt', 'r')
myline = f.readlines()
length = len(myline)
myInput = fileInput.readline()

input_list = {}
output_list = {}
list_of_wire = {}

num = input("What is largest line number in this circuit?")

for i in range(1, num+1):
    list_of_wire[i] = None

for index in range(len(myline)):
    line = myline[index].strip('\n').split()
    if line[0] == 'INPUT':
        iNum = index
    elif line[0] == 'OUTPUT':
        oNum = index
        break


for j in range(1, len(myline[iNum].split()) - 1):
    item = myline[iNum].split()
    list_of_wire[int(item[j])] = int(myInput[j-1])


for index in range(1, len(myline[oNum].split()) - 1):
    item = myline[oNum].split()
    output_list[int(item[index])] = None


count = 1

while count != 0:
    for index in range(len(myline) - 2):
        line = myline[index].strip('\n').split()
        if line[0] == 'AND' and (list_of_wire[int(line[1])] == 0 or list_of_wire[int(line[2])] == 0):
            list_of_wire[int(line[3])] = 0
        elif line[0] == 'OR' and (list_of_wire[int(line[1])] == 1 or list_of_wire[int(line[2])] == 1):
            list_of_wire[int(line[3])] = 1
        elif line[0] == 'NAND' and (list_of_wire[int(line[1])] == 0 or list_of_wire[int(line[2])] == 0):
            list_of_wire[int(line[3])] = 1
        elif line[0] == 'NOR' and (list_of_wire[int(line[1])] == 1 or list_of_wire[int(line[2])] == 1):
            list_of_wire[int(line[3])] = 0
        elif line[0] == 'INV' and (list_of_wire[int(line[1])] is not None) and (list_of_wire[int(line[2])] is None):
            if list_of_wire[int(line[1])] == 1:
                list_of_wire[int(line[2])] = 0
            else:
                list_of_wire[int(line[2])] = 1
        elif line[0] == 'BUF' and (list_of_wire[int(line[1])] is not None) and (list_of_wire[int(line[2])] is None):
            list_of_wire[int(line[2])] = list_of_wire[int(line[1])]
        elif line[0] == 'AND' and (list_of_wire[int(line[1])] is not None) and (list_of_wire[int(line[2])] is not None) \
                and (list_of_wire[int(line[3])] is None):
            list_of_wire[int(line[3])] = 1 if (list_of_wire[int(line[1])] and list_of_wire[int(line[2])]) else 0
        elif line[0] == 'OR' and (list_of_wire[int(line[1])] is not None) and (list_of_wire[int(line[2])] is not None) \
                and (list_of_wire[int(line[3])] is None):
            list_of_wire[int(line[3])] = 1 if (list_of_wire[int(line[1])] or list_of_wire[int(line[2])]) else 0
        elif line[0] == 'NAND' and (list_of_wire[int(line[1])] is not None) and (list_of_wire[int(line[2])] is not None) \
                and (list_of_wire[int(line[3])] is None):
            list_of_wire[int(line[3])] = 1 if (not (list_of_wire[int(line[1])] and list_of_wire[int(line[2])])) else 0
        elif line[0] == 'NOR' and (list_of_wire[int(line[1])] is not None) and (list_of_wire[int(line[2])] is not None) \
                and (list_of_wire[int(line[3])] is None):
            list_of_wire[int(line[3])] = 1 if (not (list_of_wire[int(line[1])] or list_of_wire[int(line[2])])) else 0

        count = 0
        for item in list_of_wire.keys():
            if list_of_wire[item] is None:
                count += 1

print list_of_wire


for item in output_list:
    output_list[item] = list_of_wire[item]

fileOutput = open("output.txt", "w")
fileOutput.write(str(output_list.values()))

f.close()
fileInput.close()
fileOutput.close()

print output_list.values()
