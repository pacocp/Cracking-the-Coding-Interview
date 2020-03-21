'''Question 1.2

@author: Francisco Carrillo-Perez
'''
from collections import OrderedDict
string1 = 'hello'
string2 = 'lleoh'
hst1 = {}
hst2 = {}

for c1, c2 in zip(string1, string2):
    if c1 not in hst1.keys():
        hst1[c1] = 1
    else:
        hst1[c1] += 1

    if c2 not in hst2.keys():
        hst2[c2] = 1
    else:
        hst2[c2] += 1

orderedhst1 = OrderedDict(sorted(hst1.items()))
orderedhst2 = OrderedDict(sorted(hst2.items()))

if orderedhst1.items() == orderedhst2.items():
    print('{} and {} are a permutation'.format(string1, string2))
else:
    print("{} and {} aren't a permutation".format(string1, string2))

