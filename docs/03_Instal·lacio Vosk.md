# Instal·lació de Vosk
Passos per instal·lar Vosk amb un terminal de Linux.

## 1. Crear carpeta de treball
```
$ mkdir ~/Vosk
$ cd ~/Vosk
```

## 2. Descarregar PyAudio si cal i Vosk
```
$ sudo apt-get install portaudio19-dev python3-pyaudio
$ pip3 install pyaudio
$ pip3 install vosk
$ git clone https://github.com/alphacep/vosk-api
$ cd vosk-api/python
```

## 3. Descarregar model en català
```
$ mkdir catalan
$ cd catalan
$ wget https://alphacephei.com/vosk/models/vosk-model-small-ca-0.4.zip
$ unzip vosk-model-small-ca-0.4.zip
$ mv vosk-model-small-ca-0.4 model
```
