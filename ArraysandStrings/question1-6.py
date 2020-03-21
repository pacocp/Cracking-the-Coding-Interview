'''Question 1.6

@author: Francisco Carrillo-Perez
'''

def compression(string):
    previous = string[0]
    counter = 1
    new_string = ''

    for i in range(1, len(string)):
        if string[i] == previous:
            counter += 1
        else:
            if counter == 1:
                new_string += previous
            else:
                new_string += previous + str(counter)
            previous = string[i]
            counter = 1
    if counter == 1:
        new_string += string[-1]
    else:
        new_string += previous + str(counter)
    return new_string

string = 'aaabbccaa'
print('original string {}; compressed string {}'.format(string, compression(string)))
