from Bitwise_verzender_controlepost import Verzenden_verstoren

def omschakelaar_tot_binair(tekst):
    """Zet de tekst per letter om via ASCII in 2 stukken van 4 bits"""
    officieel_binair  = [] 
    #Zet elk karakter om in twee stukken van 4 bits
    for letter in tekst:
        waarde = ord(letter)
        officieel_binair.append(str((waarde%256 - waarde%128)//128)+str((waarde%128 - waarde%64)//64)+str((waarde%64 - waarde%32)//32)+str((waarde%32 - waarde%16)//16))
        officieel_binair.append(str((waarde%16 - waarde%8)//8)+str((waarde%8 - waarde%4)//4)+str((waarde%4 - waarde%2)//2)+str(waarde%2))    
    return Verzekeren(officieel_binair)

def Verzekeren(data):
    """Verzekert de 4 bits door middel van 3 pariteitsbits"""
    Verzend_lijst = []
    #paritietsbits uitrekenen door middel van de Xor-functie "^".
    for Bitwise in data:
        p1 = int(Bitwise[0])^int(Bitwise[1])^int(Bitwise[3])
        p2 = int(Bitwise[0])^int(Bitwise[2])^int(Bitwise[3])
        p3 = int(Bitwise[1])^int(Bitwise[2])^int(Bitwise[3])
        Verzend_lijst.append(Bitwise+str(p1)+str(p2)+str(p3))
    return Verzenden_verstoren(Verzend_lijst)