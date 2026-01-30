# Programmeren-Wiskunde – Hamming & Bitwise Codes, Pepijn-Frank
Eindproject van Frank & Pepijn over foutdetectie en foutcorrectie met Hamming-codes en bitwise implementaties.

## Introductie
In dit project vergelijken we twee manieren (bitwise-hamming) om bitfouten te detecteren en recht te zetten tijdens datatransmissie:
- **Hamming-code (37,24)**  
  24 databits + 13 pariteitsbits, geïmplementeerd met matrixvermenigvuldiging en classes. Trager maar overzichtelijker en intuïtief beter te begrijpen.
- **Bitwise-code (7,4)**  
  4 databits + 3 pariteitsbits, geïmplementeerd met bitwise XOR-operaties en strings. Sneller (**minimaal 4x**) alleen abstracter 


## Werking van de code
1. Invoer van tekst via 'Main.py' (Hamming) of 'Main_bitwise.py' (Bitwise)
2. Tekst naar binair via 'Bit_converter.py'/'Bitwise_converter'
3. Toevoegen van pariteitsbits voor verzekering van data
4. Simulatie van transmissiefouten en rechtzetten als fout geïmplementeerd via 'Verzender_controlepost.py'/'Biwise_verzender_controlepost.py'
6. Binair → tekst via 'Reverse_bit_converter.py'/'Reverse_Bitwise_converter.py'

Tijdens het proces wordt tussentijdse output geprint, inclusief het aantal pogingen dat nodig was om foutloze data te ontvangen.


## Bestandsstructuur
- 'Main.py' – startpunt Hamming-(37,24)
- 'Main_bitwise.py' – startpunt Bitwise-(7,4)
- 'Bit_converter.py' – tekst naar binair plus partiteitsbits verzekering Hamming
- 'Bitwise_xor_verzekeraar.py' - tekst naar binair plus pariteitsbits verzekering Bitwise
- 'Verzender_controlepost.py' – foutinjectie en correctie Hamming
- 'Bitwise_verzender_controlepost.py' - foutinjectie en correctie Bitwise
- 'Reverse_bit_converter.py' – binair naar tekst Hamming
- 'Reverse_Bitwise_converter.py' - Binair naar tekst Bitwise
- 'hamming_vectoren_classes.py' - Verzamel plaats van alle classes die gebruikt zijn met hun karakteristieke functies

  
## Voorbeeld met opmerkingen
Nu gaat de tekst "Zo werken de volgende codes nou echt!" door de codes heen met een omschakelkans van 20, met andere woorden 5% van de bits krijgt een bitfout.   
1-Merk op dat spaties tellen ook als karakters  
2-Merk op dat Hamming verzendt grotere blokken (37 bits), waardoor vaker hertransmissie nodig is.  
3-Merk op dat Bitwise kan incidenteel fouten doorlaten bij meerdere (>2) bitfouten binnen één blok.  
  
Main.py (Hamming-(37,24)):  
1  
Zo w  
3  
Zo werke    
3  
Zo werken de   
1  
Zo werken de vol  
5  
Zo werken de volgend  
5  
Zo werken de volgende co  
1  
Zo werken de volgende codes   
3  
Zo werken de volgende codes nou   
7  
Zo werken de volgende codes nou echt  
3  
Zo werken de volgende codes nou echt!  
  
Main_bitwise.py (Bitwise-(7,4)):  
1  
Z  
3  
Zo  
1  
Zo   
3  
Zo w  
1  
Zo we  
3  
Zo wer  
3  
Zo werk  
1  
Zo werkl  
1  
Zo werkln  
1  
Zo werkln  
3  
Zo werkln d  
1  
Zo werkln de  
1  
Zo werkln de  
3  
Zo werkln de v  
1  
Zo werkln de vo  
1  
Zo werkln de vol  
3  
Zo werkln de volg  
1  
Zo werkln de volge  
1  
Zo werkln de volgen  
5  
Zo werkln de volgend  
1  
Zo werkln de volgende  
1  
Zo werkln de volgende  
1  
Zo werkln de volgende c  
1  
Zo werkln de volgende co  
3  
Zo werkln de volgende cod  
3  
Zo werkln de volgende code  
3  
Zo werkln de volgende codes  
1  
Zo werkln de volgende codes  
5  
Zo werkln de volgende codes n  
3  
Zo werkln de volgende codes no  
3  
Zo werkln de volgende codes nou  
1  
Zo werkln de volgende codes nou  
1  
Zo werkln de volgende codes nou e  
1  
Zo werkln de volgende codes nou ec  
3  
Zo werkln de volgende codes nou ech  
3  
Zo werkln de volgende codes nou ech$  
1  
Zo werkln de volgende codes nou ech$!  
  
# Downloads nodig
Zelf hadden wij de volgende dingen gedownload om de code werkende te krijgen:  
-Pylance, v2025.10.4  
-Python, v2026.0.0  
-Python Environments v1.16.0
