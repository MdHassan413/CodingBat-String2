# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.


# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

str_1 = input("Enter Your First String : ")
str_2 = input("Enter Your Second String : ")
a = str_1.lower()
b = str_2.lower()

if (a[-(len(b)):] == b or a == b[-(len(a)):]):
    print("True")
else:
    print("False")