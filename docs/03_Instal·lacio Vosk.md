# Instal·lació de Vosk
Passos per instal·lar Vosk amb un terminal de Linux.

## 1. Crear carpeta de treball
```
$ mkdir -p ~/Vosk
$ cd ~/Vosk
```

## 2. Descarregar PyAudio, si cal, i Vosk
```
$ sudo apt-get install portaudio19-dev python3-pyaudio
$ pip install pyaudio
$ pip install vosk
$ git clone https://github.com/alphacep/vosk-api
$ cd vosk-api/python
```

## 3. Descarregar model en català i copiar clips00 (han de ser en format WAV)
```
$ mkdir catalan
$ cd catalan
$ wget https://alphacephei.com/vosk/models/vosk-model-small-ca-0.4.zip
$ unzip vosk-model-small-ca-0.4.zip
$ mv vosk-model-small-ca-0.4 model
$ cp ~/Festival/commonvoice/clips00 .
```

## 4. Preparar scripts
```
$ mv ~/vosk_labels.sh .
$ mv ~/test_simple.py .
```

## 5. Executar Vosk
```
$ vosk_labels.sh
```
