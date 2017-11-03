import math


#funkcija sprejme parametra polmer kroga in ime lika, ter nam vrne stranice zeljenega lika, pri katerih ima lik isto ploscino kot krog s polmerom
#upostevamo ploscino kroga: S = math.pi*(polmer)**2
#funkcija bo pogledala, s katerim imenom lika se nas parameter lik ujema in bo izracunala potrebne stranice, s katerimi sta ploscini lika in kroga enaki
def ploscina( polmer, lik ):
#če je naš lik kvadrat nam izracuna stranico a, da dobimo enako ploscino.Ploscina kvadrata je S = a**2
    if lik == "kvadrat":
        a=polmer*math.sqrt(math.pi)
        return a
#ce je nas lik pravokotnik, obstaja neskoncno par stranic a in b, da dobimo isto ploscino, vendar v nalogi to ni pomembno,
#zato brez skode za splosnot privzamemo stranici, kot sta napisani v nadaljevanju. S=a*b
    elif lik == "pravokotnik":
        a=math.pi*polmer
        b=polmer
        return a,b
#Pri elipsi je podoben problem s stranicami kot pri pravokotniku, zato lahko spet izberemo dve stranici, da bo ploscina ista.
#S=math.pi*a*b
    elif lik == "elipsa":
        a=2*polmer
        b=polmer/2
        return a,b
#ce je nas lik enakostranicen trikotnik, potem obstaja samo ena moznost. Stranico izracunamo iz formule S = (math.sqrt(3) * a**2)/4
    elif lik == "trikotnik":
        a = math.sqrt((4*math.pi*(polmer)**2)/math.sqrt(3))
        return a
    else:
        return "NAPAKA"
