import re,random,time,sys,os
import time

operator2times={}

# welche Aufgaben?
# - Primzahlzerlegung
# - Division mit Rest
# - jeweils unabhängig zeiten erfassen, drei durchläufe frei, danach ziel: median der letzten 3 minus 5%, dann sukzessive um je 5% erweitern
# - timeout wie fehler

primzahlen=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

def dividiere_mit_rest(zahl: int, teiler:int):
	ergebnis=zahl/teiler
	return (int(ergebnis), int((ergebnis-int(ergebnis))*teiler))

def zerlege(zahl: int, timeout=2, start=None):
	if start==None:
		start=time.time()
	if time.time()-start>timeout:
		raise TimeoutError("timeout")

	zahl=int(zahl)

	if zahl in primzahlen:
		return [zahl]
	
	for cand in range(primzahlen[-1]+1,1+int(zahl/2)):
		if len(zerlege(cand,timeout=timeout, start=start))==1:
			primzahlen.append(cand)

	for p in primzahlen:
		if zahl/p==float(int(zahl/p)):
			return [p]+zerlege(zahl/p,timeout=timeout, start=start)

	return [zahl]

def generiere_zahl(attempts=0, maximum=100, teilermax=20, primes=3):
	ziel=None

	attempts=0

	while True:
		try:
			if attempts<10:
				ziel=(random.choice(primzahlen)*random.choice(primzahlen))+random.choice([-2,+2])*random.choice([1,2,4])
				if ziel < 2 or ziel > maximum:
					continue

				zerlegung=zerlege(ziel)
				if zerlege(ziel)[0]>10 or zerlege(ziel)[-1]>teilermax: 
					#print("nö:",ziel,zerlege(ziel))
					attempts+=1
					continue
				break
			else:
				ziel=random.choice(primzahlen[:primes])*random.choice([1,random.choice(primzahlen[:primes]),random.choice(primzahlen[:primes])*random.choice(primzahlen[:primes])])
				break
		except RecursionError:
			pass
		except TimeoutError:
			pass

	return ziel

problem2zeiten={ 
	"Division mit Rest": { 2 : [] },
	"Primzahlzerlegung" : { 1: [], 2: []}
}

zeiten_log="./mathe_log.json"
if os.path.exists(zeiten_log):
	with open(zeiten_log,"rt", errors="ignore") as content:
		problem2zeiten=json.loads(content)

while(True):
	try:

		ziel=generiere_zahl()

		problem=random.choice(list(problem2zeiten.keys()))
		subproblem=list(problem2zeiten[problem].keys())[0]

		zerlegung=None
		teiler=None

		if problem == "Primzahlzerlegung":
			zerlegung=zerlege(ziel)
			subproblem=len(zerlegung)
		elif problem == "Division mit Rest":
			teiler = random.choice(range(2,12))
			while(teiler>ziel/2):
				teiler = random.choice(range(2,12))
			subproblem=teiler
		else:
			raise Exception("unknown problem, use one of "+", ".join(sorted(problem2zeiten.keys())))

		if not subproblem in problem2zeiten[problem]:
			problem2zeiten[problem][subproblem]=[]

		sys.stderr.write(problem+" für ")
		if problem=="Primzahlzerlegung":
			sys.stderr.write(f"{ziel} (trenne Zahlen mit ,) = ")
			sys.stderr.flush()
			while(True):
				try:
					response=input()
					response=sorted([ int(x) for x in response.split(",") ])
					response=", ".join([str(r) for r in response])
					zerlegung=sorted([int(x) for x in zerlegung])
					zerlegung=", ".join([str(r) for r in zerlegung])
					break
				except Exception:
					if response.strip()!="":
						sys.stderr.write(f"Sorry, ich konnte {response} nicht verarbeiten.\n")
					sys.stderr.write("Bitte nochmal: ")
					sys.stderr.flush()
			if response==zerlegung:
				sys.stderr.write("Richtig!\n")
			else:
				sys.stderr.write("leider nicht\n")
				sys.stderr.write("du hattest: "+response+"\n")
				sys.stderr.write("richtig ist "+zerlegung+"\n")
		elif problem=="Division mit Rest":
			sys.stderr.write(f"{ziel}/{teiler} (schreibe erst die Zahl, dann 'R', dann den Rest) = ")
			sys.stderr.flush()
			ergebnis,rest=dividiere_mit_rest(ziel,teiler)
			gold=f"{int(ergebnis)} R{int(rest)}"
			while(True):
				try:
					response=input().strip()
					if not "R" in response:
						ergebnis=response
						rest=0
					else:
						ergebnis,rest=response.split("R")
					ergebnis=int(ergebnis)
					rest=int(rest)
					response=f"{ergebnis} R{rest}"
					if response==gold:
						sys.stderr.write("super!\n")
					else:
						sys.stderr.write("leider nicht\n")
						sys.stderr.write("du hattest: "+response+"\n")
						sys.stderr.write("richtig ist "+gold+"\n")
					break
				except Exception:
					if response.strip()!="":
						sys.stderr.write(f"Sorry, ich konnte {response} nicht verarbeiten.\n")
					sys.stderr.write("Bitte nochmal: ")
					sys.stderr.flush()
		sys.stderr.write("\n")
	except KeyboardInterrupt:
		sys.stderr.write("\n")
		break

sys.exit()

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


