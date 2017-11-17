import os

#funkcija sprejme ime mape, ime datoteke in seznam. Seznam pretvori v niz in ga shrani na namizje v mapo.
#pri ime_datoteke je potrebno napisati v kaksni obliki zelimo shraniti naso datoteko. Najbolj uporabno je shraniti kar v tekstovni datoteki, kjer imenu dodamo končnico .txt
def shrani(mapa, ime_datoteke, seznam):
    text=""
#najprej bomo seznam spremenili v niz stevil, da ga bo RStudio lahko pretvoril v tabelo
    for i in seznam:
#zanka, ki vsak element i iz seznama spremeni v string in ga doda nizu
        text=text + str(i) + " "

#pogledamo, ce mapa ze obstaja, drugace pa naredimo novo
    os.makedirs(mapa, exist_ok=True)
#shranimo pot po kateri lahko najdemo naso apo na racunalniku
    pot = os.path.join(mapa, ime_datoteke)
#shranimo nas text v datoteko pod kodni nabor utf-8
#oznaka 'w' pomeni, da bomo pisali v datoteko
    with open(pot, 'a', encoding = 'utf-8') as datoteka:
        datoteka.write(text + "\n")
    return None
