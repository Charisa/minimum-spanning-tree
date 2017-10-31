# An Optimal Bound for the MST Algorithm to Compute Energy Efficient Broadcat Strees in Wireless Networks

# uvoz knjiznic
import numpy




###########################################################
# Funkcije, ki generirajo tocke znotraj razlicnih likov   #
# (klicanje: npr. generator_tock.krog(10,10))             #
###########################################################


def krog(polmer, st_tock):
    '''Funkcija sprejme polmer in stevilo tock, ki jih nakljucno izbere znotraj kroga s srediscem v (0,0).
    Fukcija vrne tocke v seznamu slovarjev oblike {'x' : x, 'y' : y}.'''
    seznam_tock = [{'x' : 0, 'y' : 0}]                        # seznam, v katerega shranjujemo slovarje nakljucnih tock
    while len(seznam_tock) < st_tock:                         # iscemo nakljucne tocke, dokler v seznamu ni dovolj tock
        x = numpy.random.uniform(-polmer, polmer)             # x in y koordinato izberemo nakljucno, enakomerno porazdeljeno na intervalu polmera
        y = numpy.random.uniform(-polmer, polmer)             # s tem dobimo tocke znotraj kvadrata s stranico iste dolzine kot premer kroga
        if math.sqrt(x ** 2 + y ** 2)  <= polmer:             # pogledamo, ce je tocka znotraj kroga
            seznam_tock.append({'x' : x, 'y' : y})            # ce je, koordinati zapisemo v slovar in ju shranimo v seznam tock
    return seznam_tock                                        # vrnemo seznam slovarjev tock


def kvadrat(dolzina_stranice, st_tock):
    '''Funkcija sprejme dolzino stranice kvadrata in st. tock, ki jih nakljucno izbere znotraj kvadrata s srediscem v (0,0).
    Funkcija vrne tocke v seznamu slovarjev.'''
    seznam_tock = [{'x' : 0, 'y' : 0}]
    for tocka in range(st_tock):                                                # iscemo nakljucne tocke v kvadratu, centriranega v koordinatnem izhodiscu,
        x = numpy.random.uniform(-dolzina_stranice/2, dolzina_stranice/2)       # zato gledamo interval od polovice dolzine stranic v negatino in pozitivno
        y = numpy.random.uniform(-dolzina_stranice/2, dolzina_stranice/2)
        seznam_tock.append({'x' : x, 'y' : y})
    return seznam_tock


def pravokotnik(dolzina_stranice_a, dolzina_stranice_b, st_tock):
    '''Funkcija sprejme dolzini stranic in st. tock, ki jih nakljucno izbere znotraj pravokotnika, ki ga centriramo v
    koordinatni sistem.
    Funkcija vrne tocke v seznamu slovarjev.'''
    seznam_tock = [{'x' : 0, 'y' : 0}]
    for tocka in range(st_tock):                                                # iskanje tock v pravokotniku je zelo slicno iskanju znotraj kvadrata
        x = numpy.random.uniform(-dolzina_stranice_a/2, dolzina_stranice_a/2)
        y = numpy.random.uniform(-dolzina_stranice_b/2, dolzina_stranice_b/2)
        seznam_tock.append({'x' : x, 'y' : y})
    return seznam_tock


def elipsa(dolzina_ax, dolzina_by, st_tock):
    '''Funkcija sprejme dolzini velike in male polosi elipse, ki predstavljata standardni "a" in "b" vrednosti.
    Elipsa je postavljena v srediscno lego.
    Funkcija vrne nakljucno zgenerirane tocke v seznamu slovarjev.'''
    seznam_tock = [{'x' : 0, 'y' : 0}]
    while len(seznam_tock) < st_tock:                               # Tocke iscemo najprej znotraj pravokotnika s stranicama dolzina_ax in dolzina_by
        x = numpy.random.uniform(-dolzina_ax/2, dolzina_ax/2)
        y = numpy.random.uniform(-dolzina_by/2, dolzina_by/2)
        if x ** 2 / dolzina_a ** 2 + y ** 2 / dolzina_b ** 2 <= 1:  # Ko dobimo nakljucno izbiro tock znotraj pravokotnika, preverimo, ce
            seznam_tock.append({'x': x, 'y': y})                    # je tocka znotraj elipse, tako da tocki vstavimo v neenabo za obmocje elipse.
    return seznam_tock


def trikotnik(dolzina_stranice, st_tock):
    '''Funkcija sprejme dolzino stranice enakostranicnega trikotnika in st. tock. Osnovna stranica lezi na y = 0
    in je simetricna glede na y. Funkcija vrne tocke v seznamu slovarjev.'''
    a1 = [-dolzina_stranice/2, 0]
    a2 = [dolzina_stranice/2, 0]
    a3 = [0, dolzina_stranice]
    # Izracunamo ploscino danega trikotnika
    A = 1 / 2 * (abs(a1[0] * a2[1] + a2[0] * a3[1] + a3[0] * a1[1] - a2[0] * a1[1] + a3[0] * a2[1] - a1[0] * a3[1]))
    seznam_tock = []
    while len(seznam_tock) < st_tock:
        x = numpy.random.uniform(-dolzina_stranice/2, dolzina_stranice/2)
        y = numpy.random.uniform(-dolzina_stranice/2, dolzina_stranice/2)
        # Izracunamo 3 ploscine, ki povezujejo novo nakljucno tocko z vsakim parom danih tock
        # Ce bo vsota treh ploscin enaka vsoti danega lika, tocka lezi znotraj trikotnika.
        B = 1/2 * (abs(x * a2[1] + a2[0] * a3[1] + a3[0] * y - a2[0] * y + a3[0] * a2[1] - x * a3[1]))
        C = 1/2 * (abs(a1[0] * y + x * a3[1] + a3[0] * a1[1] - x * a1[1] + a3[0] * y - a1[0] * a3[1]))
        D = 1/2 * (abs(a1[0] * a2[1] + a2[0] * y + x * a1[1] - a2[0] * a1[1] + x * a2[1] - a1[0] * y))
        if A == (B + C + D):                                # Ce tocka je znotraj trikotnika, jo damo v seznam tock.
            seznam_tock.append({'x': x, 'y': y})
    return seznam_tock