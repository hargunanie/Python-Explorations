import random
classprompt = 'Which class are you teaching? Type Science, Math, English, or Cultures? '
prompt = "Please type in the name of the class that you would like to draw a random name from: \n Orange, Pink, Red, or Yellow? "
#maxmum = 0

overrun = True
#doc = open("English/pink.txt","r")


def english():
  rerun = True
  while rerun == True:
    answer = input(prompt).lower()
    

    if answer == "orange":
      return 'orange' 
      rerun = False

    elif answer == "pink":
      return 'pink'
      rerun = False
      
    elif answer == "red":
      return 'red'
      rerun = False

    elif answer == "yellow":
      return 'yellow'
      rerun = False

    else:
      print("Invalid answer, please try again")
      rerun = True

def cultures():
  rerun = True
  while rerun == True:
    answer = input(prompt).lower()
    

    if answer == "orange":
      return 'orange'
      rerun = False

    elif answer == "pink":
      return 'pink'
      rerun = False

    elif answer == "red":
      return 'red'
      rerun = False

    elif answer == "yellow":
      return 'yellow'
      rerun = False

    else:
      print("Invalid answer, please try again")
      rerun = True

def math():
  rerun = True
  while rerun == True:
    answer = input(prompt).lower()
    

    if answer == "orange":
      return 'orange'
      rerun = False

    elif answer == "pink":
      return 'pink'
      rerun = False

    elif answer == "red":
      return 'red'
      rerun = False

    elif answer == "yellow":
      return 'yellow'
      rerun = False

    else:
      print("Invalid answer, please try again")
      rerun = True

def science():
  rerun = True
  while rerun == True:
    answer = input(prompt).lower()
    
    if answer == "orange":
      return 'orange'
      rerun = False

    elif answer == "pink":
      return 'pink'
      rerun = False

    elif answer == "red":
      return 'red'
      rerun = False

    elif answer == "yellow":
      return 'yellow'
      rerun = False

    else:
      print("Invalid answer, please try again")
      rerun = True

classrun = True
while classrun == True:

  classanswer = input(classprompt).lower()

  if classanswer == 'cultures':
    subclass = cultures()
    if subclass == 'orange':
      doc = open('Cultures/orange.txt','r')
      #insert maxmum
    elif subclass == 'pink':
      doc = open('Cultures/pink.txt','r')
      #insert maxmum
    elif subclass == 'red':
      doc = open('Cultures/red.txt','r')
      #insert maxmum
    elif subclass == 'yellow':
      doc = open('Cultures/yellow.txt','r')
      maxmum = 14
    classrun = False

  elif classanswer == 'english':
    subclass = english()
    if subclass == 'orange':
      doc = open('English/orange.txt','r')
      maxmum = 16
    elif subclass == 'pink':
      doc = open('English/pink.txt','r')
      maxmum = 15
    elif subclass == 'red':
      doc = open('English/red.txt','r')
      maxmum = 14
    elif subclass == 'yellow':
      doc = open('English/yellow.txt','r')
      maxmum = 15
    classrun = False

  elif classanswer == 'math':
    subclass = math()
    if subclass == 'orange':
      doc = open('Math/orange.txt','r')
      #insert maxmum
    elif subclass == 'pink':
      doc = open('Math/pink.txt','r')
      #insert maxmum
    elif subclass == 'red':
      doc = open('Math/red.txt','r')
      maxmum = 16
    elif subclass == 'yellow':
      doc = open('Math/yellow.txt','r')
      #insert maxmum
    classrun = False

  elif classanswer == 'science':
    subclass = science()
    if subclass == 'orange':
      doc = open('Science/orange.txt','r')
      maxmum = 17
    elif subclass == 'pink':
      doc = open('Science/pink.txt','r')
      maxmum = 14
    elif subclass == 'red':
      doc = open('Science/red.txt','r')
      maxmum = 15
    elif subclass == 'yellow':
      doc = open('Science/yellow.txt','r')
      maxmum = 14
    classrun = False

  else: 
    print("Invalid answer, please try again")
    classrun = True 

people = doc.readlines()
while overrun == True:
  if maxmum == -1:
    print("You've picked all of the people!")
    exit()
  randomnum = random.randint(0, maxmum)
  print(people[randomnum])
  del people[randomnum]
  continuequery = input('Would you like to draw another stick? Click enter or type no. ').lower()
  if continuequery == 'no':
    overrun = False
    exit()
  else:
    overrun = True
    maxmum = maxmum - 1

doc.close()