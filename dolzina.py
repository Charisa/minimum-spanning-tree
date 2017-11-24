import numpy
import math

#Funkcija, ki izračuna dolžine med točkami

#Komentar: Pri dolocanju O-notacije je n = dolzini seznama slovarjev

def dolzina_med_tockami(seznam_slovarjev):
#Funkcija sprejme seznam slovarjev iz katerega generira seznam seznamov. Vsak podseznam predstavlja razdalje od določene točke do vseh ostalih točk.
#Da nebi razdalje dvojno računali, bomo izračunali razdaljo med točkama le enkrat tako, da dobimo zgornje trikotno matriko, ki ji bomo na koncu prišteli vrednost iste transponirane matrike
    seznam = []                                                                     #seznam, kamor bomo shranili podsezname
    for i in seznam_slovarjev:       #O(n^3)                                        #za vsako tocko bomo izracunali razdalje do njenih sosed
        podseznam = []                                                              #podseznam, kjer bomo shranili razdalje za neko tocko
        for k in seznam_slovarjev:   #O(n^2)                                        #zanka, po kateri bomo izracunali dolzino
            if seznam_slovarjev.index(k) <= seznam_slovarjev.index(i):    #O(n)     #zanka, ki pogleda, če smo dolžino za določeni točki že izračunali
                    podseznam.append(0)                                             #če smo dolžino že izračunali, doda vrednost 0
            else:
                dolzina = math.sqrt((i["y"] - k["y"])**2 + (i["x"] - k["x"])**2)   #O(1)   #izracunamo dolzino med glavno tocko in njeno sosedo
                podseznam.append(dolzina)                                          #O(1)   #dodamo dolzino v podseznam

        seznam.append(podseznam)                                                    #O(1)   #v seznam damo podsseznam za neko tocko.
    matrika=numpy.array(seznam)                                                     #seznam spremenimo v matriko. Dobimo zgornjetrikotno matriko 

    matrika = matrika + matrika.transpose()                          #O(n^2)         #matriki prištejemo njeno transponirano vrednost
    return matrika
    


