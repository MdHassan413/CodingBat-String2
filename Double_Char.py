# Given a string, return a string where for every char in the original, there are two chars.


# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

name = input("Enter Your Name to 'Extra 1 Each' : ")

for i in range(0,len(name),1):
    re = name[i] + name[i]
    print(re, end='')
