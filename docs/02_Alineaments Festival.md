# Make CLunits
Passos per crear CLunits amb un terminal de Linux.

## 1. Crear carpeta
```
$ cd Festival
```

## 2. Preparar les dades dels clips00
```
$ mkdir commonvoice
$ cd commonvoice
```
En aquesta carpeta s'ha de copiar el fitxer "validated.tsv" i la carpeta de clips00 convertits a WAV.
```
$ cp ~/validated.tsv .
$ cp ~/clips00 .
$ cd clips00
$ for f in *.mp3 ; do ( ffmpeg -i $f $f.wav ) ; done
$ rm -f *.mp3
```
El fitxer "validated.data" ha de contenir el nom de l'àudio i la transcripció entre cometes, que s'extreuen del fitxer "validated.tsv" proporcionat per Common Voice.
```
$ cd ..
$ mv ~/festival_validated_00.sh .
$ festival_validated_00.sh
```

## 3. Descarregar paquet de builder i descomprimir
```
$ cd ..
$ mkdir make_clunits
$ cd make_clunits
$ wget https://github.com/FestCat/festcat-clunits-builder/archive/master.zip
$ unzip master
$ cd festcat-clunits-builder-master
```

## 4. Executar el script
S'han de configurar els paràmetres de la veu TTS i el directori d'àudios que es vol utilitzar.
```
$ INST="upc" VOX="com" GENDER="male" DIALECT="central" CLOSESTVOICE="upc_ca_pol_clunits" PROMPTS="~/Festival/commonvoice/com.data" WAVDIR="~/Festival/commonvoice/clips00" ./train_voice "configure_template"
``` 
En el fitxer Makefile que s'ha generat, editar els següents paràmetres (canviant user):
```
ESTDIR=/home/user/Festival/speech_tools
FESTVOXDIR=/home/user/Festival/festvox
```

## 5. Executar l'alineament
```
$ make setup
$ make prompts
$ make labs
```
Les etiquetes es troben a la carpeta "lab".
