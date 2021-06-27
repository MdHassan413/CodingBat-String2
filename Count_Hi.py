# Return the number of times that the string "hi" appears anywhere in the given string.


# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

inp_hi = input("Enter Your Tence With 'Hi' to Count : ")

for i in range(0,len(inp_hi)):
    if inp_hi[i] == "h" and inp_hi[i+1] == "i" :
        Count =+ 1
        print(Count, end='')