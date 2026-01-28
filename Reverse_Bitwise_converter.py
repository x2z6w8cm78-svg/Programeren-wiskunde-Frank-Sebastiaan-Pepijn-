def Max(a,b):
    if a > b:
        return a
    else:
        return b
    
def Bitwise_omzetten(bits,Kopieën):
    """Zet de bits weer terug om in tekst voor gewenst resultaat"""
    eindtekst = ""

    for index in range(0,len(bits)//2):
        #Zet binair terug om in decimalen
        waarde = 128*int((bits[2*index])[0])+64*int((bits[2*index])[1])+32*int((bits[2*index])[2])+16*int((bits[2*index])[3])+8*int((bits[2*index+1])[0])+4*int((bits[2*index+1])[1])+2*int((bits[2*index+1])[2])+int((bits[2*index+1])[3])
        karakter = chr(waarde)
        eindtekst = eindtekst + karakter

        #Tussentijdse print met aantal kopieën nodig    
        print(Max(Kopieën[2*index],Kopieën[2*index+1]))
        print(eindtekst)
    return 