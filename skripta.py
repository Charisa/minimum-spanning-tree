###########################################################
# Skripta vsebuje funkcije za shranjevanje rezultatov     #
# (klicemo ze napisane funkcije                           #
###########################################################

import generator_tock
import dolzina
import minimalno_vpeto_drevo
import ploscine
import shrani
import math
import time
import narisi

mapa_rezultatov = "rezultati"
polmeri = [1, 1.5, 2, 5, 10]
st_tock = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 50]
ponovitve = 1000

# KROG

ime_datoteke_krog = "rezultati_krog.txt"

def shrani_krog(polmeri, st_tock, ponovitve, mapa = None, ime_datoteke = None, shrani_txt = False):
    '''Funkcija zgenerira tocke, izracuna dolzine med njimi in minimalno vpeto drevo in vsoto kvadratov, in to ponavlja
    ter shrani rezultate v datoteko (ce dano na True).'''
    sez_krog = []
    for polmer in polmeri:
        for tocke in st_tock:
            maksimum = 0
            for i in range(ponovitve):
                a = generator_tock.krog(polmer, tocke)
                b = dolzina.dolzina_med_tockami(a)
                c = minimalno_vpeto_drevo.prim(a, b)[1]
                if maksimum < c:
                    maksimum = c
            sez_krog.append(maksimum)
    if shrani_txt:
        shrani.shrani(mapa, ime_datoteke, sez_krog)
    return sez_krog


# KVADRAT

ime_datoteke_kvadrat = "rezultati_kvadrat.txt"

def shrani_kvadrat(polmeri, st_tock, ponovitve, mapa = None, ime_datoteke = None, shrani_txt = False):
    '''Funkcija zgenerira tocke v kvadratu, izracuna dolzine, najde minimalno drevo in vsoto. Poskus ponovi, kolikor
    dano, rezultate pa spravi v datoteko (ce vrednost na True).'''
    stranice = [ploscine.ploscina(k, "kvadrat") for k in polmeri]
    sez_kvadrat  =[]
    for stranica in stranice:
        for tocke in st_tock:
            maksimum = 0
            for i in range(ponovitve):
                a = generator_tock.kvadrat(stranica, tocke)
                b = dolzina.dolzina_med_tockami(a)
                c = minimalno_vpeto_drevo.prim(a, b)[1]
                if maksimum > c:
                    pass
                else:
                    maksimum = c
            sez_kvadrat.append(maksimum)
    if shrani_txt:
        shrani.shrani(mapa, ime_datoteke, sez_kvadrat)
    return sez_kvadrat


# PRAVOKOTNIK

ime_datoteke_pravokotnik = "rezultati_pravokotnik.txt"

def shrani_pravokotnik(polmeri, st_tock, ponovitve, mapa = None, ime_datoteke = None, shrani_txt = False):
    '''Funkcija zgenerira tocke v pravokotniku, izracuna dolzine, najde minimalno drevo in vsoto. Poskus ponovi, kolikor
        dano, rezultate pa spravi v datoteko (ce vrednost dana na True).'''
    stranici = [ploscine.ploscina(k, "pravokotnik") for k in polmeri]
    sez_pravokotnik = []
    for i in range(len(stranici)):
        ax = stranici[i][0]
        by = stranici[i][1]
        for tocke in st_tock:
            maksimum = 0
            for i in range(ponovitve):
                a = generator_tock.pravokotnik(ax, by, tocke)
                b = dolzina.dolzina_med_tockami(a)
                c = minimalno_vpeto_drevo.prim(a, b)[1]
                if maksimum > c:
                    pass
                else:
                    maksimum = c
            sez_pravokotnik.append(maksimum)
    if shrani_txt:
        shrani.shrani(mapa, ime_datoteke, sez_pravokotnik)
    return sez_pravokotnik


# ELIPSA

ime_datoteke_elipsa = "rezultati_elipsa.txt"

def shrani_elipsa(polmeri, st_tock, ponovitve, mapa = None, ime_datoteke = None, shrani_txt = False):
    '''Funkcija zgenerira tocke v elipsi, izracuna dolzine, najde minimalno drevo in vsoto. Poskus ponovi, kolikor
        dano, rezultate pa spravi v datoteko (ce vrednost dana na True).'''
    stranice_ax = [ploscine.ploscina(k, "elipsa")[0] for k in polmeri]
    stranice_by = [ploscine.ploscina(k, "elipsa")[1] for k in polmeri]
    sez_elipsa  =[]
    for i in range(len(stranice_ax)):
        for tocke in st_tock:
            maksimum = 0
            for k in range(ponovitve):
                a = generator_tock.elipsa(stranice_ax[i], stranice_by[i], tocke)
                b = dolzina.dolzina_med_tockami(a)
                c = minimalno_vpeto_drevo.prim(a, b)[1]
                if maksimum > c:
                    pass
                else:
                    maksimum = c
            sez_elipsa.append(maksimum)
    if shrani_txt:
        shrani.shrani(mapa, ime_datoteke, sez_elipsa)
    return sez_elipsa


# ENAKOSTRANICNI TRIKOTNIK

ime_datoteke_trikotnik = "rezultati_trikotnik.txt"

def shrani_trikotnik(polmeri, st_tock, ponovitve, mapa = None, ime_datoteke = None, shrani_txt = False):
    '''Funkcija zgenerira tocke v enakostraničnem trikotniku, izracuna dolzine, najde minimalno drevo in vsoto. Poskus ponovi, kolikor
        dano, rezultate pa spravi v datoteko (ce vrednost dana na True).'''
    stranica_a = [ploscine.ploscina(k, "trikotnik") for k in polmeri]
    sez_trikotnik  =[]
    for stranica in stranica_a:
        for tocke in st_tock:
            maksimum = 0
            for i in range(ponovitve):
                a = generator_tock.trikotnik(stranica, tocke)
                b = dolzina.dolzina_med_tockami(a)
                c = minimalno_vpeto_drevo.prim(a, b)[1]
                if maksimum > c:
                    pass
                else:
                    maksimum = c
            sez_trikotnik.append(maksimum)
    if shrani_txt:
        shrani.shrani(mapa, ime_datoteke, sez_trikotnik)
    return sez_trikotnik



# KLICANJE FUNKCIJ (zakomentirano, da se ne izvede ob "run" skripta)

# Klicanje funkcij (vrne sezname, vrednost za shranjevanje nastavljena na False)
#tocke_krog = shrani_krog(polmeri, st_tock, ponovitve)
#tocke_kvadrat = shrani_kvadrat(polmeri, st_tock, ponovitve)
#tocke_pravokotnik = shrani_pravokotnik(polmeri, st_tock, ponovitve)
#tocke_elipsa = shrani_elipsa(polmeri, st_tock, ponovitve)
#tocke_trikotnik = shrani_trikotnik(polmeri, st_tock, ponovitve)


# Ce zelimo shraniti zgornje vrednosti v datoteke, vsak seznam v svojo
#shrani_tocke_krog = shrani_krog(polmeri, st_tock, ponovitve, mapa_rezultatov, ime_datoteke_krog, True)
#shrani_tocke_kvadrat = shrani_kvadrat(polmeri, st_tock, ponovitve, mapa_rezultatov, ime_datoteke_kvadrat, True)
#shrani_tocke_pravokotnik = shrani_pravokotnik(polmeri, st_tock, ponovitve, mapa_rezultatov, ime_datoteke_pravokotnik, True)
#shrani_tocke_elipsa = shrani_elipsa(polmeri, st_tock, ponovitve, mapa_rezultatov, ime_datoteke_elipsa, True)
#shrani_tocke_trikotnik = shrani_trikotnik(polmeri, st_tock, ponovitve, mapa_rezultatov, ime_datoteke_trikotnik, True)




# VSOTE GLEDE NA STEVILO TOCK ZA PLOSCINO π oz. polmer 1 - graf narisan v R

ime_datoteke1 = "vsota_glede_st_tock.txt"
polmer1 = [1]
def vsota_glede_st_tock(mapa_rezultatov, ime_datoteke1, polmer1, st_tock, ponovitve):
    '''Funkcija, ki izracuna vsote vseh likov s ploscino π za razlicno stevilo danih tock.'''
    # KROG
    tocke_krog = []
    for polmer in polmer1:
        for tocke in st_tock:
            vsota1 = 0
            for i in range(ponovitve):
                a = generator_tock.krog(polmer, tocke)
                b = dolzina.dolzina_med_tockami(a)
                vsota2 = minimalno_vpeto_drevo.prim(a, b)[1]
                if vsota2 > vsota1:
                    vsota1 = vsota2
            tocke_krog.append(vsota1)
    shrani.shrani(mapa_rezultatov, ime_datoteke1, tocke_krog)
    # KVADRAT
    stranice = [ploscine.ploscina(k, "kvadrat") for k in polmer1]
    tocke_kvadrat = []
    for stranica in stranice:
        for tocke in st_tock:
            vsota3 = 0
            for i in range(ponovitve):
                a = generator_tock.kvadrat(stranica, tocke)
                b = dolzina.dolzina_med_tockami(a)
                vsota4 = minimalno_vpeto_drevo.prim(a, b)[1]
                if vsota4 > vsota3:
                    vsota3 = vsota4
            tocke_kvadrat.append(vsota3)
    shrani.shrani(mapa_rezultatov, ime_datoteke1, tocke_kvadrat)
    # PRAVOKOTNIK
    stranici = [ploscine.ploscina(k, "pravokotnik") for k in polmer1]
    tocke_pravokotnik = []
    for i in range(len(stranici)):
        ax = stranici[i][0]
        by = stranici[i][1]
        for tocke in st_tock:
            vsota5 = 0
            for i in range(ponovitve):
                a = generator_tock.pravokotnik(ax, by, tocke)
                b = dolzina.dolzina_med_tockami(a)
                vsota6 = minimalno_vpeto_drevo.prim(a, b)[1]
                if vsota6 > vsota5:
                    vsota5 = vsota6
            tocke_pravokotnik.append(vsota5)
    shrani.shrani(mapa_rezultatov, ime_datoteke1, tocke_pravokotnik)
    # ELIPSA
    stranice_ax = [ploscine.ploscina(k, "elipsa")[0] for k in polmer1]
    stranice_by = [ploscine.ploscina(k, "elipsa")[1] for k in polmer1]
    tocke_elipsa = []
    for i in range(len(stranice_ax)):
        for tocke in st_tock:
            vsota7 = 0
            for k in range(ponovitve):
                a = generator_tock.elipsa(stranice_ax[i], stranice_by[i], tocke)
                b = dolzina.dolzina_med_tockami(a)
                vsota8 = minimalno_vpeto_drevo.prim(a, b)[1]
                if vsota8 > vsota7:
                    vsota7 = vsota8
            tocke_elipsa.append(vsota7)
    shrani.shrani(mapa_rezultatov, ime_datoteke1, tocke_elipsa)
    # TRIKOTNIK
    stranica_a = [ploscine.ploscina(k, "trikotnik") for k in polmer1]
    tocke_trikotnik = []
    for stranica in stranica_a:
        for tocke in st_tock:
            vsota9 = 0
            for i in range(ponovitve):
                a = generator_tock.trikotnik(stranica, tocke)
                b = dolzina.dolzina_med_tockami(a)
                vsota10 = minimalno_vpeto_drevo.prim(a, b)[1]
                if vsota10 > vsota9:
                    vsota9 = vsota10
            tocke_trikotnik.append(vsota9)
    shrani.shrani(mapa_rezultatov, ime_datoteke1, tocke_trikotnik)
    return
# klicanje funkcije:
# vsota_glede_st_tock(mapa_rezultatov, ime_datoteke1, polmer1, st_tock, ponovitve)


# VSOTE GLEDE NA NARASCAJOC POLMER - graf narisan v R

ime_datoteke2 = "vsota_glede_polmer.txt"
def vsote_glede_polmer(mapa_rezultatov, ime_datoteke2, polmeri, st_tock, ponovitve):
    '''Funkcija za klicanje vseh ostalih funkcij za vse like, ki vrne seznam maksimalne vsote, ter rezultat spravi v
    tekstovno datoteko.'''
    # maksimalne vrednosti po točkah za polmere
    # krog
    seznam_krog = []
    for polmer in polmeri:
        maksimum1 = 0
        for tocke in st_tock:
            maksimum2 = 0
            for i in range(ponovitve):
                a = generator_tock.krog(polmer, tocke)
                b = dolzina.dolzina_med_tockami(a)
                c = minimalno_vpeto_drevo.prim(a, b)[1]
                if maksimum2 < c:
                    maksimum2 = c
            if maksimum2 > maksimum1:
                maksimum1 = maksimum2
        seznam_krog.append(maksimum1)
    shrani.shrani(mapa_rezultatov, ime_datoteke2, seznam_krog)
    # kvadrat
    stranice = [ploscine.ploscina(k, "kvadrat") for k in polmeri]
    seznam_kvadrat = []
    for stranica in stranice:
        maksimum3 = 0
        for tocke in st_tock:
            maksimum4 = 0
            for i in range(ponovitve):
                a = generator_tock.kvadrat(stranica, tocke)
                b = dolzina.dolzina_med_tockami(a)
                c = minimalno_vpeto_drevo.prim(a, b)[1]
                if maksimum4 < c:
                    maksimum4 = c
            if maksimum4 > maksimum3:
                maksimum3 = maksimum4
        seznam_kvadrat.append(maksimum3)
    shrani.shrani(mapa_rezultatov, ime_datoteke2, seznam_kvadrat)
    # pravokotnik
    stranici = [ploscine.ploscina(k, "pravokotnik") for k in polmeri]
    seznam_pravokotnik = []
    for i in range(len(stranici)):
        maksimum5 = 0
        ax = stranici[i][0]
        by = stranici[i][1]
        for tocke in st_tock:
            maksimum6 = 0
            for i in range(ponovitve):
                a = generator_tock.pravokotnik(ax, by, tocke)
                b = dolzina.dolzina_med_tockami(a)
                c = minimalno_vpeto_drevo.prim(a, b)[1]
                if maksimum6 < c:
                    maksimum6 = c
            if maksimum6 > maksimum5:
                maksimum5 = maksimum6
        seznam_pravokotnik.append(maksimum5)
    shrani.shrani(mapa_rezultatov, ime_datoteke2, seznam_pravokotnik)
    # elipsa
    stranice_ax = [ploscine.ploscina(k, "elipsa")[0] for k in polmeri]
    stranice_by = [ploscine.ploscina(k, "elipsa")[1] for k in polmeri]
    seznam_elipsa = []
    for i in range(len(stranice_ax)):
        maksimum7 = 0
        for tocke in st_tock:
            maksimum8 = 0
            for k in range(ponovitve):
                a = generator_tock.elipsa(stranice_ax[i], stranice_by[i], tocke)
                b = dolzina.dolzina_med_tockami(a)
                c = minimalno_vpeto_drevo.prim(a, b)[1]
                if maksimum8 < c:
                    maksimum8 = c
            if maksimum8 > maksimum7:
                maksimum7 = maksimum8
        seznam_elipsa.append(maksimum7)
    shrani.shrani(mapa_rezultatov, ime_datoteke2, seznam_elipsa)
    # trikotnik
    stranica_a = [ploscine.ploscina(k, "trikotnik") for k in polmeri]
    seznam_trikotnik = []
    for stranica in stranica_a:
        maksimum9 = 0
        for tocke in st_tock:
            maksimum10 = 0
            for i in range(ponovitve):
                a = generator_tock.trikotnik(stranica, tocke)
                b = dolzina.dolzina_med_tockami(a)
                c = minimalno_vpeto_drevo.prim(a, b)[1]
                if maksimum10 > c:
                    pass
                else:
                    maksimum10 = c
            if maksimum10 > maksimum9:
                maksimum9 = maksimum10
        seznam_trikotnik.append(maksimum9)
    shrani.shrani(mapa_rezultatov, ime_datoteke2, seznam_trikotnik)
    return
# klicanje funkcije:
vsote_glede_polmer(mapa_rezultatov, ime_datoteke2, polmeri, st_tock, ponovitve)



# IZRACUN MAKSIMALNE VSOTE KROG

# seznam tock, pri katerih je vsota kvadratov razdalj enaka 6
seznam = [{'x':0, 'y':0}, {'x':1, 'y':0}, {'x':-1, 'y':0}, {'x':0.5, 'y':math.sqrt(3)/2}, {'x':-0.5, 'y':math.sqrt(3)/2}, {'x':0.5, 'y':-math.sqrt(3)/2}, {'x':-0.5, 'y':-math.sqrt(3)/2}]

def vsota_6(seznam):
    '''Funkcija sprejme seznam tock in izracuna razdalje med njimi in najde minimalno vpeto drevo. Krog tudi narisemo.'''
    dolzine = dolzina.dolzina_med_tockami(seznam)
    drevo = minimalno_vpeto_drevo.prim(seznam, dolzine)
    vsota = drevo[1]
    narisi.narisi_krog(1, seznam, drevo[0], "drevo")
    return vsota
# klicanje funkcije:
# vsota = vsota_6(seznam)



# Koliko casa porabimo za generacijo, izracun dolzin in minimalnega drevesa ob vecanju stevila tock (preizkusimo za krog)

tocke = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 50, 60, 70, 100, 150, 200, 250]

def cas_glede_st_tock(tocke, polmer = 1, shrani_txt = True, mapa = mapa_rezultatov, ime = "cas.txt"):
    '''Funkcija sprejme stevilo tock in vrne ter shrani seznam s casi, potrebnimi za generiranje, izracun dolzine
    in iskanje minimalnega vpetega drevesa. Graf narisan v R.'''
    cas = []
    for i in tocke:
        stevilo = 0
        for k in range(100):
            start_time = time.time()
            a = generator_tock.krog(polmer, i)
            b = dolzina.dolzina_med_tockami(a)
            minimalno_vpeto_drevo.prim(a, b)[1]
            elapsed_time = time.time() - start_time
            stevilo += elapsed_time
        cas.append(stevilo/100)
    if shrani_txt:
        shrani.shrani(mapa, ime, cas)
    return cas
#cas = cas_glede_st_tock(tocke)
#print(cas)
