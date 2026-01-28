from hamming_vectoren_classes import Hamming_37_pariteitsvector_verzekerd
from hamming_vectoren_classes import Pariteits_controle_vector
from random import randrange 
from Reverse_Bit_converter import omzetten

Omschakel_kans = 100 #De 1 op de x kans dat een 1 met een 0 verwisseld (of andersom)

def Verzenden_verstoren(oorspronkelijke_data):
    """Verstoord de data van vectoren om hamming-code tot uiting te laten komen"""
    verstoorde_vectoren = []
    for vector in oorspronkelijke_data: #Schakeld met een bepaalde kans de binaire waarde om van elk kental binnen de Hamming-vector
        verstoorde_vector = Hamming_37_pariteitsvector_verzekerd((int(str(vector)[1])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[3])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[5])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[7])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[9])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[11])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[13])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[15])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[17])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[19])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[21])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[23])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[25])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[27])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[29])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[31])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[33])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[35])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[37])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[39])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[41])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[43])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[45])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[47])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[49])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[51])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[53])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[55])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[57])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[59])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[61])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[63])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[65])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[67])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[69])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[71])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2,(int(str(vector)[73])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2)
        verstoorde_vectoren.append(verstoorde_vector)

    return [verstoorde_vectoren,oorspronkelijke_data]

def gewogen_vector(lijst,aantal):
    """Kijkt democratisch naar de vectoren of er een 1 of 0 moet staan."""
    gemiddelde = Hamming_37_pariteitsvector_verzekerd()
    for vector in lijst: #Telt alle vectoren bij elkaar op 
        gemiddelde = gemiddelde + vector
    #Indien de meerderheid 1 is resulteert het in een 1 anders 0
    d1 = int(str(gemiddelde)[1])//(aantal//2+1)
    d2 = int(str(gemiddelde)[3])//(aantal//2+1)
    d3 = int(str(gemiddelde)[5])//(aantal//2+1)
    d4 = int(str(gemiddelde)[7])//(aantal//2+1)
    d5 = int(str(gemiddelde)[9])//(aantal//2+1)
    d6 = int(str(gemiddelde)[11])//(aantal//2+1)
    d7 = int(str(gemiddelde)[13])//(aantal//2+1)
    d8 = int(str(gemiddelde)[15])//(aantal//2+1)
    d9 = int(str(gemiddelde)[17])//(aantal//2+1)
    d10 = int(str(gemiddelde)[19])//(aantal//2+1)
    d11 = int(str(gemiddelde)[21])//(aantal//2+1)
    d12 = int(str(gemiddelde)[23])//(aantal//2+1)
    d13 = int(str(gemiddelde)[25])//(aantal//2+1)
    d14 = int(str(gemiddelde)[27])//(aantal//2+1)
    d15 = int(str(gemiddelde)[29])//(aantal//2+1)
    d16 = int(str(gemiddelde)[31])//(aantal//2+1)
    d17 = int(str(gemiddelde)[33])//(aantal//2+1)
    d18 = int(str(gemiddelde)[35])//(aantal//2+1)
    d19 = int(str(gemiddelde)[37])//(aantal//2+1)
    d20 = int(str(gemiddelde)[39])//(aantal//2+1)
    d21 = int(str(gemiddelde)[41])//(aantal//2+1)
    d22 = int(str(gemiddelde)[43])//(aantal//2+1)
    d23 = int(str(gemiddelde)[45])//(aantal//2+1)
    d24 = int(str(gemiddelde)[47])//(aantal//2+1)
    p1 = int(str(gemiddelde)[49])//(aantal//2+1)
    p2 = int(str(gemiddelde)[51])//(aantal//2+1)
    p3 = int(str(gemiddelde)[53])//(aantal//2+1)
    p4 = int(str(gemiddelde)[55])//(aantal//2+1)
    p5 = int(str(gemiddelde)[57])//(aantal//2+1)
    p6 = int(str(gemiddelde)[59])//(aantal//2+1)
    p7 = int(str(gemiddelde)[61])//(aantal//2+1)
    p8 = int(str(gemiddelde)[63])//(aantal//2+1)
    p9 = int(str(gemiddelde)[65])//(aantal//2+1)
    p10 = int(str(gemiddelde)[67])//(aantal//2+1)
    p11 = int(str(gemiddelde)[69])//(aantal//2+1)
    p12 = int(str(gemiddelde)[71])//(aantal//2+1)
    p13 = int(str(gemiddelde)[73])//(aantal//2+1)
    #Retourneert de democratisch besloten bits in de vorm van een nieuwe Hamming-vector
    return Hamming_37_pariteitsvector_verzekerd(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13)

def corrigeren(vectoren,onverstuurde_data):
    """Indien ongewenste pariteitsvector opnieuw opsturen van data totdat het gewenste resultaat is bereikt"""
    index = 0 
    Correcte_data = [] 
    Kopieën = [] #Telt het aantal kopieën die verstuurd zijn tot correcte data is bereikt

    for vector in vectoren:
        gemiddelde = [vector] 
        gemiddelde.append(vector)
        while str("H_d"*gemiddelde[-1]) != str(Pariteits_controle_vector(0,0,0,0,0,0,0,0,0,0,0,0,0)): #Indien incorrect, twee maal opnieuw versturen
            gemiddelde.pop()       
            gemiddelde.append((Verzenden_verstoren([onverstuurde_data[index]]))[0][0])
            gemiddelde.append((Verzenden_verstoren([onverstuurde_data[index]]))[0][0])
            gemiddelde.append(gewogen_vector(gemiddelde,len(gemiddelde)))

        Correcte_data.append(gemiddelde[-1])
        Kopieën.append(len(gemiddelde)-1)
        index = index + 1
    return omzetten(Correcte_data,Kopieën)