# Entrenament de model acústic MFA
Passos per realitzar l'entrenament del model acústic amb MFA.

# 1. Classificar els clips
Primer s'han classificat els àudios en carpetes segons els primers 4 dígits del número. Això s'ha fet creant el script "classify.bat" i executant-lo amb el terminal de Windows.
Abans, cal canviar el path del directori on s'han guardat tots els clips.
```
classify.bat
```
Amb això s'han generat totes les carpetes numerades dins de la carpeta "clips", que s'ha de traslladar al directori de Linux que s'estigui utilitzant.
Es recomana el següent directori:
```
~/clips
```
Aquest pas és útil per no col·lapsar l'explorador d'arxius de Windows.

# 2. Obtenir els àudios d'entrenament
A partir d'aquest punt s'ha de treballar amb el terminal de Linux i l'entorn de Conda.
```
$ ~/get_audios_train.sh
```
El script "get_audios_train.sh" utilitza el sistema de carpetes del pas 1. 

# 3. Entrenar el model G2P i crear diccionari adaptat
```
$ chmod -R a+rx train
$ mfa train_g2p ~/mfa_ca/dict_ipa80.txt ~/mfa_ca/ca_ipa.zip --clean -j 4
$ mfa g2p ~/mfa_ca/ca_ipa.zip ~/mfa_ca/train ~/mfa_ca/dict_ipa.txt --clean -j 4
$ chmod a+rx ~/mfa_ca/dict_ipa.txt
```
En aquest nou diccionari cal borrar, si s'escau, les línies que comencin amb caràcters extranys (que no siguin de l'alfabet). Es pot fer manualment editant el fitxer de text.

# 4. Entrenar el model acústic
```
$ mfa train ~/mfa_ca/train ~/mfa_ca/dict_ipa.txt ~/mfa_ca/train_ipa -o ~/mfa_ca/ca_acoustic_model_ipa --clean --phone_set IPA -j 4
```
Això genera el model "ca_acoustic_model_ipa.zip".