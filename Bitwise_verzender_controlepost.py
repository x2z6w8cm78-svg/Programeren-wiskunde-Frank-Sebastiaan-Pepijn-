from random import randrange 
from Reverse_Bitwise_converter import Bitwise_omzetten

Omschakel_kans = 100 #De 1 op de x kans dat een 1 met een 0 verwisseld (of andersom)

def Verzenden_verstoren(oorspronkelijke_data):
    """Verstoord de data van vectoren om Bitwise-foutdetectie tot uiting te laten komen"""
    verstoorde_vectoren = []
    for Bitwise in oorspronkelijke_data: #Schakeld met een bepaalde kans de binaire waarde om van elke losse waarde in de string
        verstoorde_vector = str((int(Bitwise[0])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2)+str((int(Bitwise[1])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2)+str((int(Bitwise[2])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2)+str((int(Bitwise[3])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2)+str((int(Bitwise[4])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2)+str((int(Bitwise[5])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2)+str((int(Bitwise[6])+randrange(0, Omschakel_kans)//(Omschakel_kans - 1))%2)
        verstoorde_vectoren.append(verstoorde_vector)

    return [verstoorde_vectoren,oorspronkelijke_data]

def gewogen_vector(lijst,aantal):
    """Kijkt democratisch naar de vectoren of er een 1 of 0 moet staan."""
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    p1 = 0
    p2 = 0
    p3 = 0
    for vector in lijst: #Telt alle vectoren bij elkaar op 
        d1 += int(vector[0])
        d2 += int(vector[1])
        d3 += int(vector[2])
        d4 += int(vector[3])
        p1 += int(vector[4])
        p2 += int(vector[5])
        p3 += int(vector[6])
    #Indien de meerderheid 1 is resulteert het in een 1 anders 0
    d1 = d1//(aantal//2+1)
    d2 = d2//(aantal//2+1)
    d3 = d3//(aantal//2+1)
    d4 = d4//(aantal//2+1)
    p1 = p1//(aantal//2+1)
    p2 = p2//(aantal//2+1)
    p3 = p3//(aantal//2+1)
    
    #Retourneert de democratisch besloten bits in de oorspronkelijke vorm
    return str(d1)+str(d2)+str(d3)+str(d4)+str(p1)+str(p2)+str(p3)

def corrigeren(vectoren,onverstuurde_data):
    """Indien ongewenste pariteitsvector opnieuw opsturen van data totdat het gewenste resultaat is bereikt"""
    index = 0 
    Correcte_data = [] 
    Kopieën = [] #Telt het aantal kopieën die verstuurd zijn tot correcte data is bereikt

    for vector in vectoren:
        gemiddelde = [vector] 
        gemiddelde.append(vector)
        #Rekent de pariteitsbits opnieuw na met de bit zelf zodat er 0 uit moet komen als het klopt
        controle_p1 = int(gemiddelde[-1][4])^int(gemiddelde[-1][0])^int(gemiddelde[-1][1])^int(gemiddelde[-1][3])
        controle_p2 = int(gemiddelde[-1][5])^int(gemiddelde[-1][0])^int(gemiddelde[-1][2])^int(gemiddelde[-1][3])
        controle_p3 = int(gemiddelde[-1][6])^int(gemiddelde[-1][1])^int(gemiddelde[-1][2])^int(gemiddelde[-1][3])
        while [controle_p1, controle_p2, controle_p3] != [0, 0, 0]: #Indien incorrect, twee maal opnieuw versturen
            gemiddelde.pop()       
            gemiddelde.append((Verzenden_verstoren([onverstuurde_data[index]]))[0][0])
            gemiddelde.append((Verzenden_verstoren([onverstuurde_data[index]]))[0][0])
            gemiddelde.append(gewogen_vector(gemiddelde,len(gemiddelde)))
            controle_p1 = int(gemiddelde[-1][4])^int(gemiddelde[-1][0])^int(gemiddelde[-1][1])^int(gemiddelde[-1][3])
            controle_p2 = int(gemiddelde[-1][5])^int(gemiddelde[-1][0])^int(gemiddelde[-1][2])^int(gemiddelde[-1][3])
            controle_p3 = int(gemiddelde[-1][6])^int(gemiddelde[-1][1])^int(gemiddelde[-1][2])^int(gemiddelde[-1][3])
        index += 1
        Correcte_data.append(gemiddelde[-1])
        Kopieën.append(len(gemiddelde)-1)
    return Bitwise_omzetten(Correcte_data,Kopieën)