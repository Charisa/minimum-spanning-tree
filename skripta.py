import generator_tock
import dolzina
import minimalno_vpeto_drevo
import ploscine
import shrani
import math
import narisi

mapa = "rezultati"
polmeri = [1, 1.5, 2, 5, 10]
st_tock = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
ponovitve = 1000

# KROG

ime_datoteke_krog = "rezultati_krog.txt"

def shrani_krog(mapa, ime_datoteke, polmeri, st_tock, ponovitve):
    '''Funkcija zgenerira tocke, izracuna dolzine med njimi in minimalno vpeto drevo in vsoto kvadratov, in to ponavlja
    ter shrani rezultate v datoteko.'''
    sez_krog = []
    for polmer in polmeri:
        podseznam = []
        for tocke in st_tock:
            maksimum = 0
            for i in range(ponovitve):
                a = generator_tock.krog(polmer, tocke)
                b = dolzina.dolzina_med_tockami(a)
                c = minimalno_vpeto_drevo.prim(a, b)[1]
                if maksimum < c:
                    maksimum = c
            podseznam.append(maksimum)
        sez_krog.append(podseznam)

    shrani.shrani(mapa, ime_datoteke, sez_krog)
    return



# KVADRAT

ime_datoteke_kvadrat = "rezultati_kvadrat.txt"

def shrani_kvadrat(mapa, ime_datoteke, polmeri, st_tock, ponovitve):
    '''Funkcija zgenerira tocke v kvadratu, izracuna dolzine, najde minimalno drevo in vsoto. Poskus ponovi, kolikor
    dano, rezultate pa spravi v datoteko.'''
    stranice = [ploscine.ploscina(k, "kvadrat") for k in polmeri]
    sez_kvadrat  =[]
    for stranica in stranice:
        podseznam = []
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
            podseznam.append(maksimum)
        sez_kvadrat.append(podseznam)
    return


# PRAVOKOTNIK

ime_datoteke_pravokotnik = "rezultati_pravokotnik.txt"

def shrani_pravokotnik(mapa, ime_datoteke, st_tock, ponovitve):
    '''Funkcija zgenerira tocke v pravokotniku, izracuna dolzine, najde minimalno drevo in vsoto. Poskus ponovi, kolikor
        dano, rezultate pa spravi v datoteko.'''
    stranici = ploscine.ploscina(1, "pravokotnik")
    sez_pravokotnik = []
    for tocke in st_tock:
        maksimum = 0
        for i in range(ponovitve):
            a = generator_tock.pravokotnik(stranici[0], stranici[1], tocke)
            b = dolzina.dolzina_med_tockami(a)
            c = minimalno_vpeto_drevo.prim(a, b)[1]
            if maksimum > c:
                pass
            else:
                maksimum = c
        sez_pravokotnik.append(maksimum)
    return


# ELIPSA

ime_datoteke_elipsa = "rezultati_elipsa.txt"

def shrani_elipsa(mapa, ime_datoteke, polmeri, st_tock, ponovitve):
    '''Funkcija zgenerira tocke v elipsi, izracuna dolzine, najde minimalno drevo in vsoto. Poskus ponovi, kolikor
        dano, rezultate pa spravi v datoteko.'''
    stranice_ax = [ploscine.ploscina(k, "elipsa")[0] for k in polmeri]
    stranice_by = [ploscine.ploscina(k, "elipsa")[1] for k in polmeri]
    sez_elipsa  =[]
    for i in range(len(stranice_ax)):
        podseznam = []
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
            podseznam.append(maksimum)
        sez_elipsa.append(podseznam)
    return sez_elipsa


# ENAKOSTRANICNI TRIKOTNIK

ime_datoteke_trikotnik = "rezultati_trikotnik.txt"

def shrani_trikotnik(mapa, ime_datoteke, polmeri, st_tock, ponovitve):
    '''Funkcija zgenerira tocke v enakostraničnem trikotniku, izracuna dolzine, najde minimalno drevo in vsoto. Poskus ponovi, kolikor
        dano, rezultate pa spravi v datoteko.'''
    stranica_a = [ploscine.ploscina(k, "trikotnik") for k in polmeri]
    sez_trikotnik  =[]
    for stranica in stranica_a:
        podseznam = []
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
            podseznam.append(maksimum)
        sez_trikotnik.append(podseznam)
    return


# Klicanje funkcij
#shrani_krog(mapa, ime_datoteke_krog, polmeri, st_tock, ponovitve)
#shrani_kvadrat(mapa, ime_datoteke_kvadrat, polmeri, st_tock, ponovitve)
#shrani_pravokotnik(mapa, ime_datoteke_pravokotnik, st_tock, ponovitve)
#shrani_elipsa(mapa, ime_datoteke_elipsa, polmeri, st_tock, ponovitve)
#shrani_trikotnik(mapa, ime_datoteke_trikotnik, polmeri, st_tock, ponovitve)


# Izracun maksimalne vsote 6 za KROG

# seznam tock, pri katerih je vsota kvadratov razdalj enaka 6
seznam = [{'x':0, 'y':0}, {'x':1, 'y':0}, {'x':-1, 'y':0}, {'x':0.5, 'y':math.sqrt(3)/2}, {'x':-0.5, 'y':math.sqrt(3)/2}, {'x':0.5, 'y':-math.sqrt(3)/2}, {'x':-0.5, 'y':-math.sqrt(3)/2}]

def vsota_6(seznam):
    '''Funkcija sprejme seznam tock in izracuna razdalje med njimi in najde minimalno vpeto drevo.'''
    dolzine = dolzina.dolzina_med_tockami(seznam)
    drevo = minimalno_vpeto_drevo.prim(seznam, dolzine)
    vsota = drevo[1]
    return vsota
vsota = vsota_6(seznam)

