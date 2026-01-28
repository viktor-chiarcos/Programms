#!/bin/bash

printf "Klicke ENTER um die Installation zu starten oder drücke Strg/Control+C zum abbrechen"
read
if [ -e ~/bin ]
  else mkdir ~/bin ; cd ~/bin
fi

echo `curl -L https://raw.githubusercontent.com/viktor-chiarcos/Programms/refs/heads/main/git-send.sh` > git-send
chmod a+x git-send
echo "Das Programm ist heruntergeladen"
