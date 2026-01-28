from Bitwise_verzender_controlepost import corrigeren
from Bitwise_xor_verzekeraar import omschakelaar_tot_binair 

tekst = input("Welk stukje tekst wil je overzetten?:")

corrigeren(omschakelaar_tot_binair(tekst)[0],omschakelaar_tot_binair(tekst)[1])