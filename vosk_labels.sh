#!/usr/bin/bash

rm -f ./resultats/*
mkdir -p ./resultats

for f in ./clips00/* ; do 
    test_simple.py $f
done