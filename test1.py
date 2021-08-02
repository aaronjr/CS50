import csv
import sys
import cs50
from csv import reader, DictReader

    
def main():


    # Handle command line arguments and save to pre-variable
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)
    datab_file = sys.argv[1]
    sq_file = sys.argv[2]
    
    # Open CSV file and save to a dict
    with open(datab_file, "r") as csv:
        reader = DictReader(csv)
        datab= list(reader)
    # Open sequences file and convert to list
    with open(sq_file, "r") as file:
        sq = file.read()
        

    # For each STR, compute longest run of consecutive repeats in      sequence
    max_counter = []
    
    for i in range(1, len(reader.fieldnames)):
        s = reader.fieldnames[i]
        max_counter.append(0)
        
    # iterate through the sequence to find s
        for j in range(len(sq)):
            counter = 0
            # If match found, counter += 1
            if sq[j:j + len(s)] == s:
                k = 0
                while sq[j + k : j + k + len(s)] == s:
                    counter += 1
                    k += len(s)
                # if there is a  new maximum of repeats - update max_counter
                if counter > max_counter[i - 1]:
                    max_counter[i - 1] = counter

    # Compare against data
    for i in range(len(datab)):
        matches = 0
        for j in range(1, len(reader.fieldnames)):
            if int(max_counter[j - 1]) == int(datab[i]  [reader.fieldnames[j]]):
                matches += 1
            if matches == (len(reader.fieldnames) - 1):
                print(datab[i]['name'])
                exit(0)
    
    print("No match")

    
if __name__ == "__main__":
    main()

#print(datab[0]['name'])
    #print(sequence)