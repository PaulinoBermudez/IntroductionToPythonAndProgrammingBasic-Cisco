#!/bin/bash

# Script de subida de contenidos
git pull
git add ../contents/*
git nota "Contents"
git sube
git add ../images/*
git nota "Images"
git sube
git add jupyterNotebook.py
git nota "JupyterNoteBook Demo"
git sube
git add README.md
git nota "README"
git sube
git add subida/*
git nota "Push the content in GitHub"
git sube
sleep 5
clear
git add .
git nota "Others"
git sube
