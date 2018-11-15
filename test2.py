'''
Author Name = Anjie Zhao
GT ID: 903334981
'''

from collections import defaultdict

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
case = input("Which option?")


def diff(li1, li2):
    return [itm for itm in li1 if itm not in li2]


def intersection(li1, li2):
    li3 = [value for value in li1 if value in li2]
    return li3


def sortPority(data):
    temp = [(int(s[:s.find("-")]), s) for s in data]
    temp.sort(key=lambda x: x[0])
    return [t[1] for t in temp]


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
    input_list[int(item[j])] = int(myInput[j-1])


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

fault_list = defaultdict(list)

for i in range(1, num+1):
    if i in input_list.keys():
        if list_of_wire[i] == 1:
            fault_list[i].append(str(i) + '-' + '0')
        else:
            fault_list[i].append(str(i) + '-' + '1')

print fault_list

count = 1

while count != 0:
    for index in range(len(myline) - 2):
        line = myline[index].strip('\n').split()
        if line[0] == 'BUF' and (int(line[1]) in fault_list.keys()) \
                and fault_list[int(line[1])] != line[1] + '-' + str(list_of_wire[int(line[1])]) \
                and (list_of_wire[int(line[1])] == 1) and (int(line[2]) not in fault_list.keys()):
            fault_list[int(line[2])] += fault_list[int(line[1])]
            fault_list[int(line[2])].append(line[2] + '-' + '0')
        elif line[0] == 'BUF' and (int(line[1]) in fault_list.keys()) \
                and fault_list[int(line[1])] != line[1] + '-' + str(list_of_wire[int(line[1])]) \
                and (list_of_wire[int(line[1])] == 0) and (int(line[2]) not in fault_list.keys()):
            fault_list[int(line[2])] += fault_list[int(line[1])]
            fault_list[int(line[2])].append(line[2] + '-' + '1')
        elif line[0] == 'INV' and (int(line[1]) in fault_list.keys()) \
                and fault_list[int(line[1])] != line[1] + '-' + str(list_of_wire[int(line[1])]) \
                and (list_of_wire[int(line[1])] == 0) and (int(line[2]) not in fault_list.keys()):
            fault_list[int(line[2])] += fault_list[int(line[1])]
            fault_list[int(line[2])].append(line[2] + '-' + '0')
        elif line[0] == 'INV' and (int(line[1]) in fault_list.keys()) \
                and fault_list[int(line[1])] != line[1] + '-' + str(list_of_wire[int(line[1])]) \
                and (list_of_wire[int(line[1])] == 1) and (int(line[2]) not in fault_list.keys()):
            fault_list[int(line[2])] += fault_list[int(line[1])]
            fault_list[int(line[2])].append(line[2] + '-' + '1')
        elif line[0] == 'AND' and (int(line[1]) in fault_list.keys()) and (int(line[2]) in fault_list.keys()) \
                and (list_of_wire[int(line[1])] == 1) and (list_of_wire[int(line[2])] == 1)\
                and (int(line[3]) not in fault_list.keys()):
            fault_list[int(line[3])] += fault_list[int(line[1])]
            fault_list[int(line[3])] += fault_list[int(line[2])]
            fault_list[int(line[3])].append(line[3] + '-' + '0')
        elif line[0] == 'AND' and (int(line[1]) in fault_list.keys()) and (int(line[2]) in fault_list.keys()) \
                and (list_of_wire[int(line[1])] == 0 or list_of_wire[int(line[2])] == 0) \
                and (int(line[3]) not in fault_list.keys()):
            if list_of_wire[int(line[1])] == 0 and list_of_wire[int(line[2])] != 0:
                fault_list[int(line[3])] += diff(fault_list[int(line[1])], fault_list[int(line[2])])
            elif list_of_wire[int(line[2])] == 0 and list_of_wire[int(line[1])] != 0:
                fault_list[int(line[3])] += diff(fault_list[int(line[2])], fault_list[int(line[1])])
            elif list_of_wire[int(line[1])] == 0 and list_of_wire[int(line[2])] == 0:
                fault_list[int(line[3])] = intersection(fault_list[int(line[1])], fault_list[int(line[2])])
            fault_list[int(line[3])].append(line[3] + '-' + '1')
        elif line[0] == 'OR' and (int(line[1]) in fault_list.keys()) and (int(line[2]) in fault_list.keys()) \
                and (list_of_wire[int(line[1])] == 0) and (list_of_wire[int(line[2])] == 0) \
                and (int(line[3]) not in fault_list.keys()):
            fault_list[int(line[3])] += fault_list[int(line[1])]
            fault_list[int(line[3])] += fault_list[int(line[2])]
            fault_list[int(line[3])].append(line[3] + '-' + '1')
        elif line[0] == 'OR' and (int(line[1]) in fault_list.keys()) and (int(line[2]) in fault_list.keys()) \
                and (list_of_wire[int(line[1])] == 1 or list_of_wire[int(line[2])] == 1) \
                and (int(line[3]) not in fault_list.keys()):
            if list_of_wire[int(line[1])] == 1 and list_of_wire[int(line[2])] != 1:
                fault_list[int(line[3])] += diff(fault_list[int(line[1])], fault_list[int(line[2])])
            elif list_of_wire[int(line[2])] == 1 and list_of_wire[int(line[1])] != 1:
                fault_list[int(line[3])] += diff(fault_list[int(line[2])], fault_list[int(line[1])])
            elif list_of_wire[int(line[1])] == 1 and list_of_wire[int(line[2])] == 1:
                fault_list[int(line[3])] = intersection(fault_list[int(line[1])], fault_list[int(line[2])])
            fault_list[int(line[3])].append(line[3] + '-' + '0')
        elif line[0] == 'NAND' and (int(line[1]) in fault_list.keys()) and (int(line[2]) in fault_list.keys()) \
                and (list_of_wire[int(line[1])] == 1) and (list_of_wire[int(line[2])] == 1) \
                and (int(line[3]) not in fault_list.keys()):
            fault_list[int(line[3])] += fault_list[int(line[1])]
            fault_list[int(line[3])] += fault_list[int(line[2])]
            fault_list[int(line[3])].append(line[3] + '-' + '1')
        elif line[0] == 'NAND' and (int(line[1]) in fault_list.keys()) and (int(line[2]) in fault_list.keys()) \
                and (list_of_wire[int(line[1])] == 0 or list_of_wire[int(line[2])] == 0) \
                and (int(line[3]) not in fault_list.keys()):
            if list_of_wire[int(line[1])] == 0 and list_of_wire[int(line[2])] != 0:
                fault_list[int(line[3])] += diff(fault_list[int(line[1])], fault_list[int(line[2])])
            elif list_of_wire[int(line[2])] == 0 and list_of_wire[int(line[1])] != 0:
                fault_list[int(line[3])] += diff(fault_list[int(line[2])], fault_list[int(line[1])])
            elif list_of_wire[int(line[1])] == 0 and list_of_wire[int(line[2])] == 0:
                fault_list[int(line[3])] = intersection(fault_list[int(line[1])], fault_list[int(line[2])])
            fault_list[int(line[3])].append(line[3] + '-' + '0')
        elif line[0] == 'NOR' and (int(line[1]) in fault_list.keys()) and (int(line[2]) in fault_list.keys()) \
                and (list_of_wire[int(line[1])] == 0) and (list_of_wire[int(line[2])] == 0) \
                and (int(line[3]) not in fault_list.keys()):
            fault_list[int(line[3])] += fault_list[int(line[1])]
            fault_list[int(line[3])] += fault_list[int(line[2])]
            fault_list[int(line[3])].append(line[3] + '-' + '0')
        elif line[0] == 'NOR' and (int(line[1]) in fault_list.keys()) and (int(line[2]) in fault_list.keys()) \
                and (list_of_wire[int(line[1])] == 1 or list_of_wire[int(line[2])] == 1) \
                and (int(line[3]) not in fault_list.keys()):
            if list_of_wire[int(line[1])] == 1 and list_of_wire[int(line[2])] == 1:
                fault_list[int(line[3])] = intersection(fault_list[int(line[1])], fault_list[int(line[2])])
            elif list_of_wire[int(line[1])] == 1:
                fault_list[int(line[3])] += diff(fault_list[int(line[1])], fault_list[int(line[2])])
            elif list_of_wire[int(line[2])] == 1:
                fault_list[int(line[3])] += diff(fault_list[int(line[2])], fault_list[int(line[1])])
            fault_list[int(line[3])].append(line[3] + '-' + '1')

    count = 0

    for item in list_of_wire.keys():
        if item not in fault_list.keys():
            count += 1


print output_list.values()
print fault_list

res = []
res2 = []
res3 = []
for item in output_list.keys():
    res += fault_list[item]

res2 = sortPority(list(set(res)))

print res2
print len(res2)

fileOutput = open("output.txt", "w")
fileOutput.write(str(output_list.values()))

if case == 'a':
    fileFault = open("faultlist.txt", "w")
    fileFault.write(str(res2))
elif case == 'b':
    fileInputFault = open('inputFault.txt', 'r')
    myInput = fileInputFault.readline()
    line = myInput.strip('\n').split()
    for item in line:
        if item in res2:
            res3.append(item)
    fileFault = open("faultlist.txt", "w")
    fileFault.write(str(res3))


f.close()
fileInput.close()
fileOutput.close()
fileFault.close()

