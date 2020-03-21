'''Question 1.4

@author: Francisco Carrillo-Perez
'''

string = 'never odd or even'

def palin_per(string):
    hash_table = {}
    string_ = string.replace(' ', '')
    # create hash table
    for ch in string_:
        if ch not in hash_table.keys():
            hash_table[ch] = 1
        else:
            hash_table[ch] += 1
    odd = 0
    for value in hash_table.values():
        if odd > 1:
            return False
        elif value % 2 != 0:
            odd += 1

    return True

if palin_per(string):
    print('{} is the permutation of a palindrome'.format(string))
else:
    print('{} is not the permutation of a palindrome'.format(string))
