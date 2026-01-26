from Bit_converter import omschakelaar_tot_binair 
from Randomizer import corrigeren

tekst = input("Welk stukje tekst wil je overzetten?:")

corrigeren(omschakelaar_tot_binair(tekst)[0],omschakelaar_tot_binair(tekst)[1])