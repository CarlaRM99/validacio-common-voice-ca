import os
import datetime
from src import textgrid


# Traducció Festival-IPA
def festival_a_ipa(i):
    if i == "ax":   i = "ə"    # neutra
    elif i == "a1": i = "a"    # a
    elif i == "e1": i = "e"    # e tancada
    elif i == "E1": i = "ε"    # e oberta
    elif i == "i1": i = "i"    # i
    elif i == "O1": i = "ɔ"    # o oberta
    elif i == "o1": i = "o"    # o tancada
    elif i == "u1": i = "u"    # u
    
    elif i == "S":  i = "ʃ"    # ix
    elif i == "Z":  i = "ʒ"    # j
    elif i == "J":  i = "ɲ"    # ny
    elif i == "L":  i = "ʎ"    # ll
    elif i == "r":  i = "ɾ"    # r sorda
    elif i == "rr": i = "r"    # r sonora

    elif i == "pau": i = ""    # silenci

    return i


# Crear fitxer de resultats 
tsv = open("compare.tsv", "w", encoding='utf-8')
tsv.write("nom" + "\t" + "voice_festival" + "\t" + "voice_mfa" + "\t " + "difference" + "\n")

n = 1
ntotal = len(os.listdir("clips00_ipa_aligned (MFA)"))
totaltime_fest = 0
totaltime_mfa = 0

# Recórrer carpeta d'alineaments MFA
for mfa_file in os.listdir("clips00_ipa_aligned (MFA)"):
    
    nom = mfa_file.replace(".TextGrid", "")

    # Obrir fitxer alineament Festival si existeix
    nom_fest = mfa_file.replace(".TextGrid", ".mp3.lab")
    path_fest = "lab00 (Festival)/" + nom_fest
    if os.path.isfile(path_fest):
        f = open(path_fest, "r", encoding='utf-8')
        fest_lines = f.readlines()

        # Obrir fitxer alineament MFA
        path_mfa = "clips00_ipa_aligned (MFA)/" + mfa_file
        m = textgrid.TextGrid.fromFile(path_mfa)

        # Crear nou fitxer alineament TextGrid
        path_comp = "compare/" + nom + ".txt"
        os.makedirs(os.path.dirname(path_comp), exist_ok=True)
        comp = open(path_comp, "w", encoding='utf-8')

        # Extracció de dades Festival
        c = 1
        voicetime_fest = 0
        start = 0

        for l in fest_lines:
            if c>3: 
                contingut = l.split()

                end = contingut[0][:-3]
                fonema = festival_a_ipa(contingut[2])

                if fonema != "":
                    voicetime_fest += float(end)-float(start)
                
                comp.write(str(start) + "\t" + fonema + "\t" + str(end) + "\n")
                
                start = end

            c+=1
        
        comp.write("\n")

        # Extracció de dades MFA
        size = len(m[1]) # Número d'intervals
        c = 0
        voicetime_mfa = 0

        while c < size:
            mark = str(m[1][c].mark).replace("(", "")
            mark = mark.replace(")", "")
            mark = mark.replace("'", "")
            mark = mark.replace(",", "")

            comp.write(str(m[1][c].minTime) + "\t" + mark + "\t" + str(m[1][c].maxTime) + "\n")

            if m[1][c].mark != "":
                voicetime_mfa += m[1][c].duration()

            c += 1

        dif = voicetime_mfa - voicetime_fest

        # Resultat
        tsv.write(nom + "\t" + f'{voicetime_fest:.2f}' + "\t" + f'{voicetime_mfa:.2f}' + "\t" + f'{dif:.2f}' + "\n")
        
        # Càlcul de temps de veu
        totaltime_fest += voicetime_fest
        totaltime_mfa += voicetime_mfa

        f.close()
        comp.close()

    print(str(n) + " / " + str(ntotal) + "\r", end="")
    n += 1


# Resultat de temps de veu per consola
print("\n\nTotal Festival  " + str(datetime.timedelta(seconds=totaltime_fest)))
print("Total MFA       " + str(datetime.timedelta(seconds=totaltime_mfa)))


tsv.close()




