#!/bin/bash

cd ~/bin
rm git-send
echo `curl -L https://raw.githubusercontent.com/viktor-chiarcos/Programms/refs/heads/main/git-send.sh` > git-send
chmod a+x git-send
echo "git-send ist auf dem neuesten Stand"
