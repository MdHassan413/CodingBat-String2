# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.


# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2

inp_code = input("Enter Your Tence With 'Code' : ")
Dcount = 0
for i in range(0,len(inp_code)):
    if inp_code[i:i+2] == "co" and inp_code[i+3] == "e":
        Dcount =+ 1
        print(Dcount)
    else:
        print("False")