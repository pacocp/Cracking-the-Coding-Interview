'''Question 1.3

@author: Francisco Carrillo-Perez
'''

def replace(string):
    new_string = ''
    for i in range(0, len(string)):
        if string[i] == ' ':
            if new_string[-3:] == '%20' and i != 0:
                return new_string[:-3]
            elif i == len(string)-1:
                return new_string
            else:
                new_string += '%20'
        else:
            new_string += string[i]
    return new_string

string = 'Mr John Smith   '
print(replace(string))
