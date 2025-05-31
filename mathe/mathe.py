import re,random,time,sys

operator2times={}

print("""Bitte löse die Aufgabe.
Wenn Du eine Antwort nicht schon auswendig kennst,
verwende die Nachbarschaftsmethode.""")

line="NIX"
while(line.strip()!=""):
		x=random.randint(1,10)
		y=random.randint(1,10)

		# zweier- und fünferreihe mit je mindestens 20%
		if(random.randint(1,5)==1):
			if random.randint(1,2)==1:
				x=5
			else:
				y=5
		elif random.randint(1,5)==1:
			if random.randint(1,2)==1:
				x=2
			else:
				y=2

		operator="*" # 30% andere operatoren
		if random.randint(1,10)==1:
			operator="+"
		elif random.randint(1,5)==1:
			operator="-"
			if x<y:
				x,y=y,x

		if not operator in operator2times:
			operator2times[operator]=[]
		operator2times[operator]=sorted(operator2times[operator])

		solution=x*y
		if operator=="+":
			solution=x+y
		if operator=="-":
			solution=x-y

		start_time=time.time()
		while line!="":
			try:
				line=input(f"{x}{operator}{y}=")
			except EOFError:
				line=""
			duration=time.time()-start_time
			start_time=time.time()
			line=line.strip()
			if line=="":
				print("Na jut, dann bis nächstes Mal.\n")
				for operator,times in operator2times.items():
					if len(times)>0:
						print(f"Für eine {operator}-Aufgabe hast du im Mittel {int(0.5+10*sum(times)/len(times))/10} (Median {int(0.5+10*times[int(len(times)/2)])/10}) Sekunden gebraucht \n")
				break
			try:
				if int(line)==solution:
					msg=random.choice(["Richtig, gut gemacht!", "Das passt, danke!", "Korrekt! Sehr gut.", "Fehlerfrei!", "Richtig gelöst ;)","Gut gemacht, mach weiter so!","Gut gemacht! Dranbleiben!"])
					if len(operator2times[operator])<=len(msg):
						pass
					elif duration>=operator2times[operator][-1]:
						msg="Gut, aber versuche, ein bisschen schneller zu werden."
					elif duration>=operator2times[operator][int(len(operator2times[operator])/2)]:
						pass
					elif duration>operator2times[operator][1+int(len(operator2times[operator])/10)]:
						msg="SUPER! Du wirst immer schneller!"
					elif duration>operator2times[operator][0]:
						msg="WOW! Flitzerbonus!"
					else:
						msg="GROSSARTIG! So fix bist Du heute noch gar nicht gewesen!"
					print(" "+msg+"\n\n")
					operator2times[operator].append(duration)
					break
				else:
					msg=["... ne, versuch nochmal.","Leider nicht. Hast Du die richtige Operation verwendet?"]
					print(f" {random.choice(msg)}\n\n")
			except Exception:
				print(" ... das war leider keine Zahl, probier nochmal\n\n")


