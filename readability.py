import cs50

#calculate letters
def letters (inpt):
    letter = 0;
    for i in range (0, len(inpt), 1):
        if inpt[i] >= 'A' and inpt[i] <= 'Z' or inpt[i] >= 'a' and inpt[i] <= 'z':
             letter+=1
    
    return letter

#calculate words
def words (inpt):
    word = 0
    for i in range (0, len(inpt), 1):
         if ord(inpt[i]) == 32:
            word += 1
    
    return word


#calcultae sentences
def sentences (inpt):
    sentence = 0
    for i in range (0, len(inpt), 1):
         if ord(inpt[i]) == 46 or ord(inpt[i]) == 33 or ord(inpt[i]) == 63:
            sentence += 1
    
    return sentence
    

def main():
    
    inpt = cs50.get_string("Text: ");

    #calculate each type
    letter = letters(inpt);
    wordz = words(inpt);
    word = wordz + 1;
    sentence = sentences(inpt);

    print(f"Letters: {letter} Words: {word} Sentences: {sentence}");

    #calculation for coleman liau
    l = (letter / word) * 100;
    s = (sentence / word) * 100;
    indx = 0.0588 * l - 0.296 * s - 15.8;
    #find round
    index = round(indx);

    #print grade level
    
    if index < 1:
        print("Before Grade 1\n")
    elif index >= 1 and index <16:
        print(f"Grade {index}")
    elif index >= 16:
        print(f"Grade 16+")

if __name__ == "__main__":
    main()