#!/usr/bin/bash

# Ordena les frases
sudo cat ~/train.tsv | tail -n +2 | tr "\t" "~" | cut -d"~" -f 1,2,3 | sort > ~/train.data

# Crea carpeta de treball si no existeix
mkdir -p ~/mfa_ca/train

# Variables
id_ant=0
speaker=0
nline=0
count=$(wc ~/train.data)
nlines=$(echo $count|cut -d' ' -f1)

# Llegeix cada línia del fitxer .data
while read line; do

    # Retalla l'ID d'usuari (0-127) i el nom del fitxer (caràcters 129-152)
    id=${line:0:128}
    nom=${line:129:24}

    # Crea carpeta de speaker només si el speaker és diferent a l'anterior o és el primer de la llista
    if [ "$id" != "$id_ant" ] ; then
        ((speaker++))
        mkdir -p ~/mfa_ca/train/speaker$speaker
    fi 

    # Extreu el número d'àudio i els primers 4 dígits
    num=${line:145:8} 
    pre=${line:145:4} 

    # Busca el fitxer i el mou a la carpeta train
    mv ~/clips/$pre/$nom.mp3 ~/mfa_ca/train/speaker$speaker

    # Crea el fitxer .lab
    frase=${line:158} 
    echo "$frase" > ~/mfa_ca/train/speaker$speaker/$nom.lab ;

    # Assignem aquest ID per comparar amb el següent de la llista
    id_ant=$id

    # Missatge per consola
    ((nline++))
    echo -ne "$nline / $nlines\r"

done < ~/train.data

echo -e "\nDone!"
