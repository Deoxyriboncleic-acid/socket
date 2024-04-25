#!/bin/bash

rm HelloWorld.html
rm fuck.html
python3 client.py 123.60.221.93 12000 HelloWorld.html
python3 client.py 123.60.221.93 12000 fuck.html

ls -l fuck.html HelloWorld.html  --time-style=long-iso --time=atime

