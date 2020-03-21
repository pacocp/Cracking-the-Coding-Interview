'''Question 1.9

@author: Francisco Carrillo-Perez
'''

def isSubstring(s1, s2):
    if s1 in s2:
        return True
    else:
        return False


s2 = 'waterbottle'
s1 = 'erbottlewat'
if isSubstring(s2, s1+s1):
    print('{} is a rotation of {}'.format(s2, s1))
else:
    print('{} is not a rotation of {}'.format(s2, s1))
