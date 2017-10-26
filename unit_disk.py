# An Optimal Bound for the MST Algorithm to Compute Energy Efficient Broadcat Strees in Wireless Networks

# Izrek: Vsota kvadratov dolzin povezav v minimalnem vpetem drevesu s poljubnimi tockami v enotskem disku, kjer
# je sredisce tocka v setu poljubnih tock, je skoraj 6.


# uvoz knjiznic
import numpy
import math


# Funkcija, ki generira tocke

def generator_tock_krog(polmer, st_tock):
    '''Funkcija sprejme polmer in stevilo tock, ki jih nakljucno izbere znotraj kroga s srediscem v (0,0).
    Tocke vrne v paru koordinat.'''
    seznam_tock = []                                          # seznam, v katerega shranjujemo slovarje nakljucnih tock
    while len(seznam_tock) < st_tock:                         # iscemo nakljucne tocke, dokler v seznamu ni dovolj tock
        x = numpy.random.uniform(-polmer, polmer)             # x in y koordinato izberemo nakljucno, enakomerno porazdeljeno na intervalu polmera
        y = numpy.random.uniform(-polmer, polmer)             # s tem dobimo tocke znotraj kvadrata s stranico iste dolzine kot premer kroga
        if math.sqrt(x ** 2 + y ** 2)  <= polmer:             # pogledamo, ce je tocka znotraj kroga
            seznam_tock.append({'x' : x, 'y' : y})            # ce je, koordinati zapisemo v slovar in ju shranimo v seznam tock
    return seznam_tock                                        # vrnemo seznam slovarjev tock



