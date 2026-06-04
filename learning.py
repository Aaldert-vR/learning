import sys
version="1.2.0"
if len(sys.argv)>1:
  if sys.argv[1]=="--version":
    print(f'learning {version}')
    sys.exit()
import json
import webbrowser
from random import *
from time import *
from termcolor import colored, cprint
import sys
import os
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfile
import keyboard
from colorama import init
from termcolor import colored

exeFile=__file__
exeDir=exeFile[0:-len(exeFile.split('\\')[-1])]
goodOrFalse=[]
knowAll=False
init()

print(colored(f'learning {version}\nDoor Aaldert van Reenen','green'))

if not (os.path.exists(exeDir+"settings.json")):
  print("Het bestand 'settings.json' is niet gevonden. Druk op een toets om door te gaan.")
  keyboard.read_key()
  sys.exit()
f_path=""
fileIsOpen=False
if len(sys.argv)>1:
  f_path=sys.argv[1]
  fileIsOpen=True
else:
  f_path = askopenfilename(initialdir="/",
        title="Kies een bestand", filetypes=(("learning files","*.learn*"),("All files","*.*")))
try:
  f = open(f_path)
except:
  print("Het bestand is niet gevonden. Probeer nog een keer.")
else:
  dat = json.load(f)
  f.close()
  fileIsOpen=True
  for i in range(len(list(dat.keys()))):
    goodOrFalse.append(i)
f = open(exeDir+"settings.json")
settings = json.load(f)
f.close()
print(settings)
print("Engelse woordjes leren")
print("voor hulp, typ '//help'")
print("Nieuwe woorden toevoegen? Typ j of n.")
new = False
x = input()
if x == "j":
  new = True
good = 0
total = 0


goedrekenen=settings["optie 'toch goedrekenen'"]


def openFile():
  global f_path,fileIsOpen,goodOrFalse
  print(f_path)
  f_path = askopenfilename(initialdir="/",
        title="Kies een bestand", filetypes=(("learning files","*.learn*"),("All files","*.*")))
  try:
    f=open(f_path,"w")
    f.write("{}")
    f.close()
    f=open(f_path,"r")
  except:
    print("Het bestand is niet gevonden. Probeer nog een keer.")
    fileIsOpen=False
  else:
    dat=json.load(f)
    f.close()
    fileIsOpen=True
  
def settingsHelp():
  pass

def helpMe(opdracht):
  pass

def draaiOm(a):
  b=list(a.keys())
  c=list(a.values())
  d=dict()
  for i in range(len(b)):
    e=b[i]
    f=c[i]
    if "\\" in e:
      ee=e.split("\\")
      eee=ee[2].split(" | ")
      ff=ee[0]+"\\"+f+"\\"+eee[0]+" | "+f
      f=ff
      e=eee[1]
    d[f]=e
  return d

def menu():
  print("----------------------------MENU----------------------------")
  print("opties:")
  print("\t-instellingen")
  print("\t-help")
  print("\t-sluit bestand")
  print("\t-open bestand")
  print("\t-nieuw bestand")
  print("\t-sluit menu")
  inp=input('menu>>')
  if inp=="sluit menu":
    execute("")
  execute(inp)

def makeSettings():
  global goedrekenen,f_path
  settingsF=open(exeDir+"settings.json","r")
  inst=json.load(settingsF)
  settingsF.close()
  print("------------------------INSTELLINGEN------------------------")
  for i in inst.keys():
    print(i)
  while True:
    inp=input(colored("instellingen>>",'light_blue','on_black'))
    if inp[0:2]=="//":
      execute(inp[2:])
    else:
      if inp=="help":
        settingsHelp()
      elif inp=="lijst":
        print(inst)
      elif inp=="goedrekenen aan":
        goedrekenen=True
      elif inp=="goedrekenen uit":
        goedrekenen=False
      elif inp=="sluit":
        break
      elif inp=="sla instellingen op":
        settingsF=open(exeDir+"settings.json","r")
        json.dump(inst,settingsF,indent=2)
        settingsF.close()
      else:
        if ': ' in inp:
          inp=inp.split(": ")
          try:
            settings[inp[0]]=inp[1]
          except:
            pass

def newFile():
  global f_path
  f = asksaveasfile(initialdir="/",
        title="Sla op", defaultextension=".learn", filetypes=(("learning files","*.learn*"),("All files","*.*")))
  try:
    f_path=f.name
    f.close()
  except:
    pass
  try:
    f=open(f_path,"w")
    f.write("{}")
    f.close()
    f=open(f_path,'r')
  except:
    print("Er trad een fout op tijdens het opslaan. Probeer nog een keer.")
  else:
    dat=json.load(f)
    f.close()
    fileIsOpen=True


opdrachten=["sluit: sluit dit programma","verwijder woorden: begin met het verwijderen van woorden"]
def execute(command):
  global new,dat,f_path,fileIsOpen
  if command == "verwijder woorden":
    print("Woorden:")
    for item in dat.items():
      print(item[0] + ": " + item[1])
    removing = True
    while removing:
      r = input("Verwijderen>> ")
      if r == "sluit":
        removing = False
      elif r == "toon lijst":
        for item in dat.items():
          print(item[0]+": "+item[1])
      elif r == "alle woorden":
        sure = input("Weet je zeker dat je alle woorden wilt verwijderen?\nDat kun je niet ongedaan maken.\nTyp ja of nee.")
        if sure == "ja":
          dat.clear()
          f = open(f_path,"w")
          json.dump(dat,f)
          f.close()
          print("Alle woorden zijn verwijderd")
      elif r[0] == "-":
        if r[1:] in dat.keys():
          dat.pop(r[1:])
          f = open(f_path,"w")
          json.dump(dat,f)
          f.close()
        else:
          print("'"+r[1:]+"' is niet in de woordenlijst")
      else:
        print("'"+r+"' is geen opdracht.")
  elif command == "sluit":
    sys.exit()
  
  elif command == "help":
    print("Typ het antwoord op een vraag achter de dubbelepunt(:).")
    print("Opdrachten, bijvoorbeeld het veranderen van instellingen of het verwijderen van woorden, geef je door er "+colored("//","yellow","on_black")+" voor te typen.")
    for o in opdrachten:
      print(o)
    while True:
      opdracht = input("Typ 'help' + waarmee je geholpen wilt worden"+
                       "\nbijvoorbeeld help verwijder bestanden, of"+
                       "\nsluit om af te sluiten.\n")
      if opdracht == "sluit":
        break
      elif opdracht.split(" ") == [0] == "help":
        helpMe(opdracht[5:])
  elif command=="nu leren":
    new=False
  elif command=="voeg nieuwe toe":
    new=True
  elif command=="instellingen":
    makeSettings()
  elif command=="menu":
    menu()
  elif command=="sluit bestand":
    del dat
    fileIsOpen=False
  elif command=="nieuw bestand":
    newFile()
  elif command=="leerrichting omdraaien":
    dat=draaiOm(dat)

while True:
  if not(fileIsOpen):
    while True:
      inp=input("open een bestand\n")
      if inp=="open":
        openFile()
        break
      elif inp[0:2]=="//":
        execute(inp[2:])
  if new:
    inp = input(colored('toevoegen>>','green','on_black'))
    if inp[0:2] == "//":
      execute(inp[2:])
    else:
      inp = inp.split(": ")
      if len(inp)==2:
        dat[inp[0]] = inp[1]
      else:
        print(colored("Probeer het nog een keer",'yellow','on_black'))
      f = open(f_path,"w")
      json.dump(dat,f)
      f.close()
  else:
    if len(list(dat.keys())) == 0:
      print("Voeg eerst woorden toe.")
      new = True
    else:
      k = list(dat.keys())
      a=bool(randint(0,1))
      if len(goodOrFalse)==0 and knowAll==False:
        wilverder=input("Je kent alle woorden. Wil je stoppen? (J/N)\n").upper()
        while True:
          if wilverder=="J":
            sys.exit()
          elif wilverder=="N":
            knowAll=True
            break
      if a and len(goodOrFalse)>0:
        n=goodOrFalse[randint(0,len(goodOrFalse)-1)]
      else:
        n = randint(0,len(k)-1)
      question = k[n]
      if question.count('\\')%2==0:
        q2=question.split('\\')
        for i in range(int((len(q2)-1)/2)):
          print(q2[2*i], end='')
          print(colored(q2[2*i+1], 'blue', 'on_black', attrs=['bold']),end='')
        q3=q2[-1]
      else:
        q3=question
      ans = input(q3 + ":\t")
      if ans[0:2] == "//":
        execute(ans[2:])
      else:
        if ans == dat[question]:
          print(colored("goed zo!\r",'green','on_black'))
          good += 1
          if n in goodOrFalse:
            goodOrFalse.remove(n)
        else:
          print(colored("jammer. Het goede andwoord is: ",'red','on_black') + colored(dat[question],'yellow','on_black') + "\r")
          if goedrekenen=="aan":
            tochGoed=input("Wil je het toch goedrekenen? (ja=j/nee/n)\n").lower()
            if tochGoed=="ja" or tochGoed=="j":
              good+=1
              if n in goodOrFalse:
                goodOrFalse.remove(n)
            else:
              if not n in goodOrFalse:
                goodOrFalse.append(n)
        total += 1
        sleep(0.5)
        print(str(good)+"/"+str(total)+"\r")
        sleep(1)
