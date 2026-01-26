def omzetten(bits,Kopieën):
    """Zet de bits weer terug om in tekst voor gewenst resultaat"""
    eindtekst = ""
    index = 0
    for vector in bits:
        index += 1
        #Zet binair terug om in decimalen
        waarde1 = int(str(vector)[1])*32 + int(str(vector)[3])*16 + int(str(vector)[5])*8 + int(str(vector)[7])*4 + int(str(vector)[9])*2 + int(str(vector)[11])
        waarde2 = int(str(vector)[13])*32 + int(str(vector)[15])*16 + int(str(vector)[17])*8 + int(str(vector)[19])*4 + int(str(vector)[21])*2 + int(str(vector)[23])
        waarde3 = int(str(vector)[25])*32 + int(str(vector)[27])*16 + int(str(vector)[29])*8 + int(str(vector)[31])*4 + int(str(vector)[33])*2 + int(str(vector)[35])
        waarde4 = int(str(vector)[37])*32 + int(str(vector)[39])*16 + int(str(vector)[41])*8 + int(str(vector)[43])*4 + int(str(vector)[45])*2 + int(str(vector)[47])
        if waarde1 < 1:
            eindtekst = eindtekst #0 opvullingen voor einde tekst
        elif waarde1 < 3:
            eindtekst = eindtekst + chr(waarde1+31) #spatie en uitroepteken
        elif waarde1 < 9:
            eindtekst = eindtekst + chr(waarde1+33) #speciale karakters
        elif waarde1 < 37:
            eindtekst = eindtekst + chr(waarde1+54) #A-Z
        else:
            eindtekst = eindtekst + chr(waarde1+60) #a-z
        
        if waarde2 < 1:
            eindtekst = eindtekst
        elif waarde2 < 3:
            eindtekst = eindtekst + chr(waarde2+31)
        elif waarde2 < 9:
            eindtekst = eindtekst + chr(waarde2+33)
        elif waarde2 < 37:
            eindtekst = eindtekst + chr(waarde2+54)
        else:
            eindtekst = eindtekst + chr(waarde2+60)

        if waarde3 < 1:
            eindtekst = eindtekst
        elif waarde3 < 3:
            eindtekst = eindtekst + chr(waarde3+31)
        elif waarde3 < 9:
            eindtekst = eindtekst + chr(waarde3+33)
        elif waarde3 < 37:
            eindtekst = eindtekst + chr(waarde3+54)
        else:
            eindtekst = eindtekst + chr(waarde3+60)
        
        if waarde4 < 1:
            eindtekst = eindtekst
        elif waarde4 < 3:
            eindtekst = eindtekst + chr(waarde4+31)
        elif waarde4 < 9:
            eindtekst = eindtekst + chr(waarde4+33)
        elif waarde4 < 37:
            eindtekst = eindtekst + chr(waarde4+54)
        else:
            eindtekst = eindtekst + chr(waarde4+60)
        #Tussentijdse print met aantal kopieën nodig    
        print(Kopieën[index-1])
        print(eindtekst)
    return 