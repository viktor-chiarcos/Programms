#!/bin/bash

printf "Klicke ENTER um die Installation zu starten oder drücke Strg/Control+C zum abbrechen"
read
if [ -e ~/bin ]
then echo "~/bin Ordner muss nicht erstellt werden, da er bereits exestiert"
else mkdir ~/bin
fi
cd ~/bin
echo `curl -L https://raw.githubusercontent.com/viktor-chiarcos/Programms/refs/heads/main/git-send.sh` > git-send
chmod a+x git-send
echo "Das Programm ist heruntergeladen"
