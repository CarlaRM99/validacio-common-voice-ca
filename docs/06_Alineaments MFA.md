# Alineament forçat amb Montreal Forced Aligner
Passos per obtenir alineaments amb MFA.

# 1. Obtenir clips00
```
$ ~/get_audios_validated.sh
```

# 2. Alinear
```
$ mfa align ~/mfa_ca/clips00 ~/mfa_ca/dict_ipa.txt ~/mfa_ca/ca_acoustic_model_ipa.zip ~/mfa_ca/clips00_aligned --clean -j 4
```
