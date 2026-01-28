#!/bin/bash

if [ !e $HOME/bin ]
then mkdir ~/bin
fi
cd ~/bin

echo `curl -L https://raw.githubusercontent.com/viktor-chiarcos/Programms/refs/heads/main/git-send.sh` > git-send
chmod a+x git-send
echo "Das Programm ist heruntergeladen"
