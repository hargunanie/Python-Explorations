run = True
while run:
    filename = input('What is this class called? You will need to remember this for choosing where to pull sticks: ')
    classsize = int(input('What is the size of your class?'))
    classroster = []
    for student in range(classsize):
        studentname = input("What is this student's name? ")
        if student < classsize:
            classroster.append(f'{studentname}\n')
        else:
            classroster.append(studentname)
    with open(f'{filename}.txt', 'w+') as file:
        file.writelines(classroster)
    cont = input('Do you have another class that you would like to add? Type y or n: ')
    if cont.lower() == 'n':
        run = False
    else:
        continue
