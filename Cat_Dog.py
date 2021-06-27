# Return True if the string "cat" and "dog" appear the same number of times in the given string.


# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

inp_CD = input("Enter Your Tence With 'Dog and Cat' : ")
Dcount = 0
Ccount = 0
for i in range(0,len(inp_CD)):
    if inp_CD[i:i+3] == "dog":
        Dcount =+ 1
        print("True")
    elif inp_CD[i:i+3] == "cat":
        Ccount =+ 1
        print("True")
    else:
        print("False")
        

