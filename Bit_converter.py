from hamming_vectoren_classes import Hamming_24_vector_onverzekerd
from Verzender_controlepost import Verzenden_verstoren

def omschakelaar_tot_binair(tekst):
    """Zet de tekst om in stukken van 24 bits"""

    stukjes_tekst = [] #Tekst wordt opgesplits in stukken van vier karakters
    for i in range(0,len(tekst)//4+1):
        stukjes_tekst.append(tekst[4*i:4*i+4])

    onofficieel_binair  = [] #Zet de stukjes tekst om in een zelfbedachte binaire code van 6*4 karakters
    for knip in stukjes_tekst:
        bits = ""
        for karakter in knip:
            value = ord(karakter)
            if value>96:
                new_value = value-60 #a-z
            elif value>62:
                new_value = value-54 #A-Z
            elif value>39:
                new_value = value-33 #speciale karakters
            else:
                new_value = value-31 #spatie en uitroepteken
            bits = bits+(str((new_value -new_value%32)//32)+str((new_value%32 -new_value%16)//16)+str((new_value%16 -new_value%8)//8)+str((new_value%8 -new_value%4)//4)+str((new_value%4 -new_value%2)//2)+str(new_value%2))

        if len(bits) != 24: #Opvulling van nullen bij te weinig karakters
            bits = bits + (24-len(bits))*"0" 

        onofficieel_binair.append(bits)
    return Verzekeren(onofficieel_binair)

def Verzekeren(data):
    """Zet de onofficiële binaire data om in Hamming-classes en verzekerd ze vervolgens met pariteitsbits"""
    Verzend_lijst = []
    for Hamming_vector in data:
        vector = Hamming_24_vector_onverzekerd(int(Hamming_vector[0]),int(Hamming_vector[1]),int(Hamming_vector[2]),int(Hamming_vector[3]),int(Hamming_vector[4]),int(Hamming_vector[5]),int(Hamming_vector[6]),int(Hamming_vector[7]),int(Hamming_vector[8]),int(Hamming_vector[9]),int(Hamming_vector[10]),int(Hamming_vector[11]),int(Hamming_vector[12]),int(Hamming_vector[13]),int(Hamming_vector[14]),int(Hamming_vector[15]),int(Hamming_vector[16]),int(Hamming_vector[17]),int(Hamming_vector[18]),int(Hamming_vector[19]),int(Hamming_vector[20]),int(Hamming_vector[21]),int(Hamming_vector[22]),int(Hamming_vector[23]))
        pariteits_vector = "H_e" * vector #Voegt pariteitsbits toe om data te verzekeren door middel van een matrix multiplicatie
        Verzend_lijst.append(pariteits_vector)
    return Verzenden_verstoren(Verzend_lijst)