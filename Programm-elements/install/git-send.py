#!/usr/bin/python3

wollen1 = input('Sind sie sicher dass sie die Datei git-send ins /usr/local/bin Verzeichnis verlinken wollen [ENTER (Taste für Ja)/n]: ')
if wollen1 == '':
	os.system("sudo ln -s git-send.sh /usr/local/bin/git-send")
	print('zum Ausführen von git-send sagen sie nur git-send im beliebigen Verzeichnis.')
	os.system("bash")
else: exit()