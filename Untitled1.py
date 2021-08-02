for i in range(0,len(sq) + 10):
        
        if sq[i] == "A" and sq[i+1] == "G" and sq[i + 2] == "A" and sq[i + 3] == "T" and sq[i+4] =="C":
            AGATC += 1
        elif "TTTTTTCT" in sq:
            TTTTTTCT += 1
        elif "AATG" in sq:
            AATG += 1
        elif "GATA" in sq:
            GATA += 1
        elif "TATC" in sq:
            TATC += 1
        elif "GAAA" in sq:
            GAAA += 1
        elif "TCTG" in sq:
            TCTG += 1