import random
classfile = input('Which class would you like to pull sticks from? ')
with open(f'{classfile}.txt') as readfile:
    roster = readfile.readlines()

rosterrange = len(roster) - 1
run = True
while run:
    print(roster.pop(random.randint(0, rosterrange)))
    rosterrange = rosterrange - 1
    if rosterrange == -1:
        print("You've picked all the people!")
        break
    cont = input('Do you want to pull another stick? Type y or n')
    if cont == 'n':
        run = False
        print('Thanks for using Popsicle Stick Sim V2')
    else:
        continue
