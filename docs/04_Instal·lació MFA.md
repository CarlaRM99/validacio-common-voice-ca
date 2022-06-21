# Instal·lació de MFA
Passos per instal·lar Montreal Forced Aligner amb un terminal de Linux, seguint la documentació oficial (https://montreal-forced-aligner.readthedocs.io/en/latest/installation.html).

# 1. Obrir directori
```
$ cd ~/mfa_ca
```

# 2. Instal·lar Conda
```
$ wget https://repo.anaconda.com/miniconda/Miniconda3-4.7.12.1-Linux-x86_64.sh
$ Miniconda3-4.7.12.1-Linux-x86_64.sh
```
Reiniciar el terminal a continuació.

# 3. Crear entorn de Conda
```
$ conda create -n aligner -c conda-forge montreal-forced-aligner
```
Si dona problemes, esborrar l'arxiu "~/.condarc" i tornar a provar.

# 4. Activar entorn
Aquest pas s'ha de fer cada vegada que s'obre de nou el terminal.
```
$ conda activate aligner
```
