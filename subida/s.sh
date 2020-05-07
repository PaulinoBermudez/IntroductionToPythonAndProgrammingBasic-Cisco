#!/bin/bash

# Script de subida de contenidos
git pull
git add ../_ENTREGAS/.
git nota "Soluciones de mis prácticas obligatorias - DEVNET"
git sube
git add ../contents/.
git nota "Contents"
git sube
git add ../Model Driven Programmability - DevnNet20/.
git nota "Model Driven Programmability - Exercises"
git sube
git add ../images/.
git nota "Images"
git sube
git add ../jupyterNotebook.py
git nota "JupyterNoteBook Demo"
git sube
git add README.md
git nota "README"
git sube
git add subida/.
git nota "Push the content in GitHub"
git sube
sleep 5
clear
git add .
git nota "Others"
git sube
echo "Fin del script"
sleep 5
clear
echo "Vamos con calma"
sleep 300

sh s.sh
