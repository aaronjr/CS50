from cs50 import get_int

#prompt for answer
answer = get_int("Pick a number between 1 - 8: ")
#if answer < 1 or < 8 re-prompt
while answer < 1 or answer > 8:
    print("Number must be between 1 & 8")
    answer = get_int("Pick a number between 1 and 8: ")
#make pyramid print blank space first, then hash, then gap then hahs
for i in range (answer):
    for j in range (answer - i- 1):
        print(" ", end=" ")
    for h in range (i + 1):
        print("#", end = "")
    print(" ", end = "")
    for l in range (i + 1):
        print("#", end = "")
    print(" ")