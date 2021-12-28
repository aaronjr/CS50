from cs50 import get_int

# check if card is valid


def is_valid(cc):
    # take input convert to string and find length
    strg = str(cc)
    leng = len(strg)
    
    g = ""
    # use algorithm to jump though card number
    for i in range(leng - 2, - 1, - 2):
                        
        multiply = int(strg[i]) * 2
        g += str(multiply)
    
        missed = []
        
        for k in range(leng - 1, - 1, - 2):
            missed.append(int(strg[k]))
        
    total = 0
    # use algorithm to jump though card number
    for j in range(0, len(g), 1):
        total += int(g[j])
    
    p = 0
    # use algorithm to jump though card number
    for l in range(0, len(missed), 1):
        p += missed[l]
        
    sum = p + total
    
    if sum % 10 == 0:
        return 0
    else:
        return 1
        
# take cc number and checks which brand it is.


def number(cc):
    strg = str(cc)
    leng = len(strg)
    if leng == 15:
        if strg[0] == "3" and strg[1] == "4" or strg[1] == "7":
            print("AMEX")
    elif leng == 16:
        if strg[0] == "5" and strg[1] == "1" or strg[1] == "2" or strg[1] == "3" or strg[1] == "4" or strg[1] == "5":
            print("MASTERCARD")
        elif strg[0] == "4":
            print("VISA")
    elif leng == 13:
        if strg[0] == "4":
            print("VISA")
    else:
        print("INVALID")
    
    
# main function prompts user for their number


def main():        
    
    cc = get_int("Enter credit card number: ")
    
    answer = is_valid(cc)
    
    if answer == 0:
        number(cc)
    else:
        print("INVALID")


if __name__ == "__main__":
    main()