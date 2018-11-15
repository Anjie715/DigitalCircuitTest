# from collections import defaultdict
#
# map = defaultdict(list)
#
# # for i in range(10):
# #     map[i].append(i)
# #
# # for i in range(10):
# #     map[i].append(i)

# print map

from collections import defaultdict


def Diff(li1, li2):
    return (list(set(li1) - set(li2)))


def diff(li1, li2):
    return [itm for itm in li1 if itm not in li2]


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


test = True

fault_list = defaultdict(list)
fault_list[1] = [1, 2, 3]
fault_list[2] = [4, 5, 6]
fault_list[1] += fault_list[2]

if 3 not in fault_list.keys():
    test = False


def takeKey(elem):
    return elem[0]


li1 = ['10-5', '15', '20', '25', '30', '35', '40']
li2 = ['10-6', '9', '55']
li2.sort(key=takeKey)

print li2
print(diff(li1, li2))
print fault_list[1]
print test
print intersection(li1, li2)

