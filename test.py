import csv
import sys
import cs50

def main():

    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage example: python dna.py databases/large.csv sequences/5.txt")

    # Loads teams to a list
    datab = []
    filename = sys.argv[1]
    with open(filename) as f:
        datab = [{k:v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]


    file = open(sys.argv[2], "r")
    sq = file.read()

    AGATC = sq.count("AGATC")
    TTTTTTCT = sq.count("TTTTTTCT")
    AATG = sq.count("AATG")
    TCTAG = sq.count("TCTAG")
    GATA = sq.count("GATA")
    TATC = sq.count("TATC")
    GAAA = sq.count("GAAA")
    TCTG = sq.count("TCTG")
    
    print(datab)
    print(AGATC,TTTTTTCT,AATG,TCTAG,GATA,TATC,GAAA,TCTG)
    
    #for i in range(0, len(datab)):
    #    if datab[i]["name"] == 'Alice':
    #        print(datab[i]["name"])

    for i in range(0, len(datab)):
        if datab[i]["TTTTTTCT"] == str(TTTTTTCT):
            print(datab[i]["name"])
    
if __name__ == "__main__":
    main()


#print(datab[0]['name'])
    #print(sequence)
    
    