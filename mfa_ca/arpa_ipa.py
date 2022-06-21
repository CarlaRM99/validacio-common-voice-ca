# Comparació
import os
import sys

# Obrir diccionari i llegir
f = open("diccionari.tsv", "r", encoding='utf-8')
lines = f.readlines()

# Obrir nou diccionari que escriurem
res = open('dict_ipa.tsv', 'w', encoding='utf-8')


for l in lines:
    paraula = l.split()

    novaparaula = ""

    for i in paraula:
        if i == "AE":   i = "ə "    # neutra
        elif i == "EA": i = "ə "    # neutra
        elif i == "A":  i = "a "    # a
        elif i == "E":  i = "e "    # e tancada
        elif i == "EE": i = "ε "    # e oberta
        elif i == "I":  i = "i "    # i
        elif i == "AO": i = "ɔ "    # o oberta
        elif i == "O":  i = "o "    # o tancada
        elif i == "UO": i = "u "    # o àtona
        elif i == "U":  i = "u "    # u
        elif i == "Y":  i = "j "    # i diftong
        elif i == "W":  i = "w "    # u diftong
        
        elif i == "P":  i = "p "    # p
        elif i == "B":  i = "b "    # b
        elif i == "V":  i = "v "    # b (v)
        elif i == "BV": i = "β "    # b aproximant
        elif i == "T":  i = "t "    # t
        elif i == "D":  i = "d "    # d
        elif i == "DH": i = "ð "    # d aproximant
        elif i == "K":  i = "k "    # k
        elif i == "G":  i = "g "    # g
        elif i == "GH": i = "γ "    # g aproximant
        elif i == "CH": i = "tʃ "   # tx
        elif i == "C":  i = "dʒ "   # tj  
        elif i == "F":  i = "f "    # f
        elif i == "S":  i = "s "    # s sorda
        elif i == "Z":  i = "z "    # s sonora
        elif i == "SH": i = "ʃ "    # ix
        elif i == "J":  i = "ʒ "    # j
        elif i == "M":  i = "m "    # m
        elif i == "N":  i = "n "    # n
        elif i == "NY": i = "ɲ "    # ny
        elif i == "NG": i = "ŋ "    # ng
        elif i == "L":  i = "l "    # l
        elif i == "LY": i = "ʎ "    # ll
        elif i == "R":  i = "ɾ "    # r sorda
        elif i == "RR": i = "r "    # r sonora

        else:           i += "\t"

        novaparaula += i
    
    novaparaula += "\n"

    res.write(novaparaula)


f.close()
res.close()

