class Hamming_24_vector_onverzekerd:
    """Slechts de 4*6 bits in de vorm van een binaire vector"""
    def __init__(self, d1=0, d2=0, d3=0, d4=0, d5=0, d6=0, d7=0, d8=0, d9=0, d10=0, d11=0, d12=0, d13=0, d14=0, d15=0, d16=0, d17=0, d18=0, d19=0, d20=0, d21=0, d22=0, d23=0, d24=0):
        self.a = d1
        self.b = d2
        self.c = d3
        self.d = d4
        self.e = d5
        self.f = d6
        self.g = d7
        self.h = d8
        self.i = d9
        self.j = d10
        self.k = d11
        self.l = d12
        self.m = d13
        self.n = d14
        self.o = d15
        self.p = d16
        self.q = d17
        self.r = d18
        self.s = d19
        self.t = d20
        self.u = d21
        self.v = d22
        self.w = d23
        self.x = d24

    def __mul__(self, other):
        #Slechts de vermenigvuldiging met de H_e-matrix links en vector rechts is correct
        return print("Verkeerde volgorde of foutieve vermenigvuldiging")

    def __rmul__(self,other):
        #Slechts de vermenigvuldiging met de H_e-matrix links en vector rechts is correct
        if other == "H_e":
            sommatie = (self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + self.i + self.j + self.k + self.l + self.m + self.n + self.o + self.p + self.q + self.r + self.s + self.t + self.u + self.v + self.w + self.x)%2
            #Retouneert een verzekerde Hamming-vector door 13 pariteitbits toe te voegen
            return Hamming_37_pariteitsvector_verzekerd(self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i, self.j, self.k, self.l, self.m, self.n, self.o, self.p, self.q, self.r, self.s, self.t, self.u, self.v, self.w, self.x, (sommatie - self.n - self.u)%2, (sommatie - self.m - self.t)%2, (sommatie - self.l - self.t)%2, (sommatie - self.k - self.s)%2, (sommatie - self.j - self.s)%2, (sommatie - self.i - self.r)%2, (sommatie - self.h - self.r - self.x)%2, (sommatie - self.g - self.q - self.x)%2, (sommatie - self.f - self.q - self.w)%2, (sommatie - self.e - self.p - self.w)%2, (sommatie - self.d - self.p - self.v)%2, (sommatie - self.c - self.o - self.v)%2, (sommatie - self.b - self.o - self.u)%2)
        else:
            return print("Verkeerde volgorde of foutieve vermenigvuldiging")
        
    def __str__(self):
        #Print de vector in een getransponeerde vorm uit
        return "(" + str(self.a) + "," + str(self.b) + ","+ str(self.c) + ","+ str(self.d) + "," + str(self.e) + "," + str(self.f) + ","+ str(self.g) + ","+ str(self.h) + "," + str(self.i) + "," + str(self.j) + ","+ str(self.k) + ","+ str(self.l) + "," + str(self.m) + "," + str(self.n) + ","+ str(self.o) + ","+ str(self.p) + "," + str(self.q) + "," + str(self.r) + ","+ str(self.s) + ","+ str(self.t) + "," + str(self.u) + "," + str(self.v) + ","+ str(self.w) + ","+ str(self.x) +")^T"

    
class Hamming_37_pariteitsvector_verzekerd:
    """37 bits vector in binaire vorm dat verzekerd is door middel van 13 pariteitbits"""
    def __init__(self, d1=0, d2=0, d3=0, d4=0, d5=0, d6=0, d7=0, d8=0, d9=0, d10=0, d11=0, d12=0, d13=0, d14=0, d15=0, d16=0, d17=0, d18=0, d19=0, d20=0, d21=0, d22=0, d23=0, d24=0, p1=0, p2=0, p3=0, p4=0, p5=0, p6=0, p7=0, p8=0, p9=0, p10=0, p11=0, p12=0, p13=0):
        self.a = d1
        self.b = d2
        self.c = d3
        self.d = d4
        self.e = d5
        self.f = d6
        self.g = d7
        self.h = d8
        self.i = d9
        self.j = d10
        self.k = d11
        self.l = d12
        self.m = d13
        self.n = d14
        self.o = d15
        self.p = d16
        self.q = d17
        self.r = d18
        self.s = d19
        self.t = d20
        self.u = d21
        self.v = d22
        self.w = d23
        self.x = d24
        self.y = p1
        self.z = p2
        self.aa = p3
        self.ab = p4
        self.ac = p5
        self.ad = p6
        self.ae = p7
        self.af = p8
        self.ag = p9
        self.ah = p10
        self.ai = p11
        self.aj = p12
        self.ak = p13

    def __add__(self, other):
    #Sommeerd de vectoren, let op de vector is niet in modulo-2
        return Hamming_37_pariteitsvector_verzekerd(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d, self.e + other.e, self.f + other.f, self.g + other.g, self.h + other.h, self.i + other.i, self.j + other.j, self.k + other.k, self.l + other.l, self.m + other.m, self.n + other.n, self.o + other.o, self.p + other.p, self.q + other.q, self.r + other.r, self.s + other.s, self.t + other.t, self.u + other.u, self.v + other.v, self.w + other.w, self.x + other.x, self.y + other.y, self.z + other.z, self.aa + other.aa, self.ab + other.ab, self.ac + other.ac, self.ad + other.ad, self.ae + other.ae, self.af + other.af, self.ag + other.ag, self.ah + other.ah, self.ai + other.ai, self.aj + other.aj, self.ak + other.ak)
 
    def __mul__(self, other):
    #Slechts de vermenigvuldiging met de H_d-matrix links en vector rechts is correct
        return print("Verkeerde volgorde of foutieve vermenigvuldiging")
   
    def __rmul__(self,other):
    #Slechts de vermenigvuldiging met de H_d-matrix links en vector rechts is correct
        if other == "H_d":
            Sommatie = (self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + self.i + self.j + self.k + self.l + self.m + self.n + self.o + self.p + self.q + self.r + self.s + self.t + self.u + self.v + self.w + self.x)%2
            #Retouneert een correctie vector waarbij de pariteitbits opnieuw uitgerekent worden
            return Pariteits_controle_vector((self.y -(Sommatie - self.n - self.u))%2, (self.z -(Sommatie - self.m - self.t))%2, (self.aa -(Sommatie - self.l - self.t))%2, (self.ab -(Sommatie - self.k - self.s))%2, (self.ac -(Sommatie - self.j - self.s))%2, (self.ad -(Sommatie - self.i - self.r))%2, (self.ae -(Sommatie - self.h - self.r - self.x))%2, (self.af -(Sommatie - self.g - self.q - self.x))%2, (self.ag -(Sommatie - self.f - self.q - self.w))%2, (self.ah -(Sommatie - self.e - self.p - self.w))%2, (self.ai -(Sommatie - self.d - self.p - self.v))%2, (self.aj -(Sommatie - self.c - self.o - self.v))%2, (self.ak -(Sommatie - self.b - self.o - self.u))%2)
        else:
            return print("Verkeerde volgorde of foutieve vermenigvuldiging")     
        
    def __str__(self):
        #Print de vector in een getransponeerde vorm uit
        return "(" + str(self.a) + "," + str(self.b) + ","+ str(self.c) + ","+ str(self.d) + "," + str(self.e) + "," + str(self.f) + ","+ str(self.g) + ","+ str(self.h) + "," + str(self.i) + "," + str(self.j) + ","+ str(self.k) + ","+ str(self.l) + "," + str(self.m) + "," + str(self.n) + ","+ str(self.o) + ","+ str(self.p) + "," + str(self.q) + "," + str(self.r) + ","+ str(self.s) + ","+ str(self.t) + "," + str(self.u) + "," + str(self.v) + ","+ str(self.w) + ","+ str(self.x) + ","+ str(self.y) + "," + str(self.z) + "," + str(self.aa) + ","+ str(self.ab) + ","+ str(self.ac) + "," + str(self.ad) + "," + str(self.ae) + ","+ str(self.af) + ","+ str(self.ag) + "," + str(self.ah) + "," + str(self.ai) + ","+ str(self.aj) + ","+ str(self.ak) + ")^T"
    

class Pariteits_controle_vector:
    """13-delige vector die controleert of er geen fouten zijn opgetreden bij het overzetten van data"""
    def __init__(self, d1=0, d2=0, d3=0, d4=0, d5=0, d6=0, d7=0, d8=0, d9=0, d10=0, d11=0, d12=0, d13=0):
        self.a = d1
        self.b = d2
        self.c = d3
        self.d = d4
        self.e = d5
        self.f = d6
        self.g = d7
        self.h = d8
        self.i = d9
        self.j = d10
        self.k = d11
        self.l = d12
        self.m = d13
    
    def __str__(self):
        #Print de vector in een getransponeerde vorm uit
        return "(" + str(self.a) + "," + str(self.b) + ","+ str(self.c) + ","+ str(self.d) + "," + str(self.e) + "," + str(self.f) + ","+ str(self.g) + ","+ str(self.h) + "," + str(self.i) + "," + str(self.j) + ","+ str(self.k) + ","+ str(self.l) + "," + str(self.m) +")^T"
