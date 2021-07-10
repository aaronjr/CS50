from cs50 import get_int

cc = get_int("Enter credit card number: ")
str = str(cc)
len = len(str)




if len == 15:
    if str[0] == "3" and str[1] == "4" or str[1] == "7":
        print("AMEX")
elif len == 16:
    if str[0] == "5" and str[1] == "1" or str[1] == "2" or str[1] == "3" or str[1] == "4" or str[1] == "5":
        print("MASTERCARD")
    elif str[0] == 4:
        print("VISA")
elif len == 13 or len == 16:
    if str[0] == "4":
        print("VISA")
else:
    print("INVALID")
