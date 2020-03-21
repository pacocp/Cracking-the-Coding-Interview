'''Question1.1

@author: Francisco Carrillo-Perez
'''

string = 'hello'
hash_table = {}
correct = True

for character in string:
    if character not in hash_table.keys():
        hash_table[character] = 0
    else:
        print('{} does not have  all unique characters'.format(string))
        correct = False
        break

if correct:
    print('{} has all unique characters'.format(string))
