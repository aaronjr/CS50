import csv
import sys
import cs50
from csv import reader, DictReader

    
def main():
    
    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage example: python dna.py databases/large.csv sequences/5.txt")

    database_file = sys.argv[1]
    sequence_file = sys.argv[2]
    
    # open database - save to a list
    with open(database_file, 'r') as csv:
        reader = DictReader(csv)
        datab = list(reader)
    
    # open sequences_file and turn into a list
    with open(sequence_file, "r") as sq_file:
        sq = sq_file.read()

    #for each STR find longest repeat
    max_repetition = []
    for i in range(1, len(reader.fieldnames)):
        s = reader.fieldnames[i]
        max_repetition.append(0)
        
        #iterate through the sequence to find s
        for j in range(len(sq)):
            counter = 0
            #if match cound counter plus 1 
            if sq[j:j + len(s)] == s:
                k=0
                while sq[j + k : j + k + len(s) == s]:
                    counter+= 1
                    ke += len(S)
                #if new maximum of repitions - update max_repitions
                if counter > max_repetition[i - 1]:
                   max_repetition[i - 1] = counter
   
    #compare against data
    for i in range(len(datab)):
        matches = 0
        for j in range(1, len(reader.fieldnames)):
            if int(max_repetition[j-1]) == int(datab[i] [reader.fieldnames[j]]):
                matches += 1
            if matches == (len(reader.fieldnames) - 1):
                print(datab[i]['name'])
                exit(0)
   
    print("No match")   
                
    
    
if __name__ == "__main__":
    main()


#print(datab[0]['name'])
    #print(sequence)
    
    