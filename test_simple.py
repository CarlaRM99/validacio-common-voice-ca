#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave

SetLogLevel(0)

if not os.path.exists("model"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("model")
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)
#rec.SetPartialWords(True)

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        ...
        #print(rec.Result())
    else:
        #print(rec.PartialResult())

        # EDIT
        nom = str(sys.argv[1]).replace("clips00/", "")
        nom = nom.replace(".mp3.wav", ".txt")

        f = open("./resultats/"+ nom, "w")
        f.write(rec.FinalResult())
        f.close()
        

# print(rec.FinalResult())

