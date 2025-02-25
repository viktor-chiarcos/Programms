#!/usr/bin/python3

import os
os.system ("""
	lxterminal -e \"python3 -c '
		wollen1 = input(
			\\\"Sind sie sicher dass sie die Datei git-send 
				ins /usr/local/bin Verzeichnis verschieben 
				wollen? [ENTER (Taste für Ja)/n]: \\\"); 
		if wollen1 == '':
			os.system (
				\\\"lxterminal -e 
					\\\\\"sudo ln -s git-send.sh 
						 /usr/local/bin/git-send;
						 sudo chmod a+x git-send; 
						 echo zum Ausführen von git-send 
						 sagen sie nur git-send\\\\\"
				\\\") else: exit()
		\"
		""");
