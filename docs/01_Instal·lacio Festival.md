# Instal·lació de Festival
Passos per instal·lar Festival amb un terminal de Linux.

1. Crear carpeta de treball 
```
$ mkdir Festival
$ cd Festival
```

2. Instal·lar la llibreria de desenvolupament "libncurses-dev" i el compilador "g++".
```
$ sudo apt-get install libncurses-dev g++
```

3. Descarregar els arxius de Festival executant el script "download_festival.sh" i descomprimir-los a la carpeta Festival.
```
$ mv ../download_festival.sh .
$ bash download_festival.sh
$ for f in *tar.gz ; do ( tar zxvf $f ) ; done
```

4. Instal·lar Speech Tools
```
$ cd speech_tools
$ ./configure --prefix=~/Festival/speech_tools
$ make
$ make install
```

5. Instal·lar FestVox
```
$ cd ../festvox
$ ./configure --prefix=~/Festival/festvox
$ make
```

6. Instal·lar Festival
```
$ cd ../festival
$ ./configure --prefix=~/Festival/festival
$ make
$ make install
```

7. Crear el fitxer "~/.festivalrc"
```
$ cd ~
$ touch .festivalrc
```
Escriure-hi els següents paràmetres:
```
(Parameter.set 'Audio_Command "paplay -n festival $FILE")
(Parameter.set 'Audio_Method 'Audio_Command)
(Parameter.set 'Audio_Required_Format 'snd)
```

8. Editar el fitxer "~/.bashrc" (canviant user)
```
# set FESTIVAL variables and path

export ESTDIR=/home/user/Festival/speech_tools
export FESTVOXDIR=/home/user/Festival/festvox
export FESTIVALDIR=/home/user/Festival/festival
PATH=".:$PATH:$ESTDIR/bin:$FESTIVALDIR/bin"
```

9. Instal·lar les veus en català
```
$ cd ~/Festival/
$ wget http://festcat.talp.cat/download/upc_ca_bet_clunits-1.2.tgz
$ wget http://festcat.talp.cat/download/upc_ca_pol_clunits-1.2.tgz
$ tar xzvf upc_ca_pol_clunits-1.2.tgz
$ sudo mv upc_ca_pol_clunits ./festival/lib/voices/catalan
$ tar xzvf upc_ca_bet_clunits-1.2.tgz
$ sudo mv upc_ca_bet_clunits ./festival/lib/voices/catalan
```

10. Instal·lar el fitxer base del català
```
$ wget http://festcat.talp.cat/download/upc_ca_base-3.0.6.tgz
$ tar xzvf upc_ca_base-3.0.6.tgz
$ sudo mv upc_ca_base-3.0.6/festival/lib/dicts/upc ./festival/lib/dicts
$ sudo mv upc_ca_base-3.0.6/festival/lib/upc_catalan ./festival/lib
```

11. Editar el fitxer '$FESTIVALDIR/lib/languages.scm' i modificar els paràmetres pel català
```
(define (language_catalan)
"(language_catalan)
Set up language parameters for Catalan."
    (set! female1 voice_upc_ca_bet_clunits)
    (set! male1   voice_upc_ca_pol_clunits)
    (female1)
    (Parameter.set 'Language 'catalan)
)

((equal? language 'catalan) 
(language_catalan))
```
