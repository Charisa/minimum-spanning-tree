import numpy
import math



###########################################################
# Funkcije, ki generirajo tocke znotraj razlicnih likov   #
# (klicanje: npr. generator_tock.krog(10,10))             #
###########################################################


def krog(polmer, st_tock):
    '''Funkcija sprejme polmer in stevilo tock, ki jih nakljucno izbere znotraj kroga s srediscem v (0,0).
    Fukcija vrne tocke v seznamu slovarjev oblike {'x' : x, 'y' : y}.'''
    seznam_tock = [{"x" : 0, "y" : 0}]                                          # seznam, v katerega shranjujemo slovarje nakljucnih tock
    while len(seznam_tock) < st_tock:                         # iscemo nakljucne tocke, dokler v seznamu ni dovolj tock
        x = numpy.random.uniform(-polmer, polmer)             # x in y koordinato izberemo nakljucno, enakomerno porazdeljeno na intervalu polmera
        y = numpy.random.uniform(-polmer, polmer)             # s tem dobimo tocke znotraj kvadrata s stranico iste dolzine kot premer kroga
        if math.sqrt(x ** 2 + y ** 2)  <= polmer:             # pogledamo, ce je tocka znotraj kroga
            seznam_tock.append({'x' : x, 'y' : y})            # ce je, koordinati zapisemo v slovar in ju shranimo v seznam tock
    return seznam_tock      


#Funkcija, ki izračuna dolžine med tockami

def dolzine_med_tockami(seznam_slovarjev):

#Funkcija sprejme seznam slovarjev iz katerega generira seznam seznamov. Vsak podseznam predstavlja razdalje od določene točke do vseh ostalih točk.

    seznam = []                                                                    #seznam, kamor bomo shranili podsezname
    for i in seznam_slovarjev:                                                     #za vsako tocko bomo izracunali razdalje do njenih sosed
        podseznam = []                                                             #podseznam, kjer bomo shranili razdalje za neko tocko
        for k in seznam_slovarjev:                                                 #zanka, po kateri bomo izracunali dolzino 
            dolzina = math.sqrt((i["y"] - k["y"])**2 + (i["x"] - k["x"])**2)       #izracunamo dolzino med glavno tocko in njeno sosedo
            podseznam.append(dolzina)                                              #dodamo dolzino v podseznam

        seznam.append(podseznam)                                                   #v seznam damo podsseznam za neko tocko
    return seznam



#Dijkstrov algoritem

def dijkstra(G):

    #Funkcija sprejme množico tock grafa G in vrne drevo najkrajsih poti. Izvora ne potrebujemo dodati, ker je v našem primeru izvor (0,0)
    #G predstavlja seznam slovarjev
    Q=G                               #Q je množica točk
    d=[]                              #razdalja od izvira do drugih tock
    pi=[]                             #oce v drevesu najkrasih poti
    dolzine = dolzine_med_tockami(G)  #vzamemo že izračunane dolžine med točkami
    for i in G:                       #v tej zanki pripravimo vrednosti v seznamu d in pi
        d.append(math.inf)
        pi.append(None)
    d[0] = 0                          #razdalja od izvira do izvira je 0

    while len(Q)>0:                   #ponavljamo postopek dokler nam ne zmanjka točk v množžici Q
        #u = d.index(min(d))          #tukaj je napaka!!! ne poišče točke iz Q,ki ima minimalno vrednost v d
        #del Q[u]
        for v in range(0,len(G)-1):   #za točko u pogledamo njene sosede
            if u == v:                #če sta u in v ista točka, preskočimo soseda v
                pass
            else:
                if d[v] > d[u] + dolzine[u][v]:   #pogledamo ali je trenutna dolžina od izvora do točke v daljša
                                                  #kot trenutna dolžina od izvora do točke u, kateri prištejemo dolžino med točkama u in v
                    
                    d[v] = d[u] + dolzine[u][v]   # če je zgornja neenačba pravilna, potem dolžino od izvora do točke v spremenimo
                    pi[v] = u                     # dodamo u v seznam očetov
                
    return d, pi
    
                









    
