# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.


# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

str1 = input("Enter Your First String : ")
for i in range(len(str1)):
    if str1[i] != '.' and str1[i+1:i+4] == 'xyz':
        print("True")
    elif str1[0:3] == 'xyz':
        print("True")
    else:
        print("False")