#!/bin/bash

echo ("Python Request")
 
python pip install --upgrade pip
python pip install jupyter

echo ("Jupyter location")
where jupyter
echo ("Python version")
python -V

echo ("Open Jupyter")
/usr/bin/open -a "Firefox" 'http://localhost:8888'