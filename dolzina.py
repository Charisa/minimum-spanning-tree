import numpy
import math

#Funkcija, ki izračuna dolžine med točkami

def dolzina_med_tockami(seznam_slovarjev):

#Funkcija sprejme seznam slovarjev iz katerega generira seznam seznamov. Vsak podseznam predstavlja razdalje od določene točke do vseh ostalih točk.

    seznam = []                                                                    #seznam, kamor bomo shranili podsezname
    for i in seznam_slovarjev:                                                     #za vsako tocko bomo izracunali razdalje do njenih sosed
        podseznam = []                                                              #podseznam, kjer bomo shranili razdalje za neko tocko
        for k in seznam_slovarjev:                                                  #zanka, po kateri bomo izracunali dolzino 
            if seznam_slovarjev.index(k) <= seznam_slovarjev.index(i):              #zanka, ki pogleda, če smo dolžino za določeni točki že izračunali
                    podseznam.append(0)                                             #če smo dolžino že izračunali, doda vrednost 0
            else:
                dolzina = math.sqrt((i["y"] - k["y"])**2 + (i["x"] - k["x"])**2)       #izracunamo dolzino med glavno tocko in njeno sosedo
                podseznam.append(dolzina)                                              #dodamo dolzino v podseznam

        seznam.append(podseznam)                                                   #v seznam damo podsseznam za neko tocko
    return seznam
    
