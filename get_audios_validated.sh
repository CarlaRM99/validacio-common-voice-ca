#!/usr/bin/bash

# Crea carpeta de treball si no existeix
mkdir -p ~/mfa_ca/clips00

# Variables
id_ant=0
speaker=1
nline=0
count=$(wc ~/validated2.data)
nlines=$(echo $count|cut -d' ' -f1)

# Llegeix cada línia del fitxer .data
while read line; do

    # Retalla el nom del fitxer (caràcters 0-27)
    nom=${line:0:24}

    # Extreu el número d'àudio i els primers 4 dígits
    num=${nom:22:2} 
    pre=${nom:16:4} 

    if [[ $num == 00 ]] ; then
        # Busca el fitxer i el mou a la carpeta train
        mv ~/clips/$pre/$nom.mp3 ~/mfa_ca/clips00

        # Crea el fitxer .lab
        frase=${line:29} 
        echo "$frase" > ~/mfa_ca/clips00/$nom.lab ;
    fi

    # Missatge per consola
    ((nline++))
    echo -ne "$nline / $nlines\r"

done < ~/validated2.data

echo -e "\nDone!"
