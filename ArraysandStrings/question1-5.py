'''Question 1.5

@author: Francisco Carrillo-Perez
'''

def check_change(string1, string2):
    diff = False
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            if diff:
                return False
            else:
                diff = True

    return True

def check_insert(string1, string2):
    index1 = 0
    index2 = 0
    while ((index2 < len(string2)) and (index1 < len(string1))):
        if string2[index2] != string1[index1]:
            if index1 != index2:
                return False
            else:
                index1 += 1
        else:
            index1 += 1
            index2 += 1
    return True

def check_edits(string1, string2):
    # check length
    if len(string1) == len(string2):
        return check_change(string1, string2)
    elif len(string2) == len(string1) + 1 or len(string2) == len(string1) -1 :
        return check_insert(string1, string2)
    else:
        return False

str1 = 'pale'
str2 = 'bke'

if check_edits(str1, str2):
    print('{} and {} have zero or one edits'.format(str1, str2))
else:
    print('{} and {} have more than one edits'.format(str1, str2))

