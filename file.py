prompt = 'Do you have any pets?'
var = input(prompt)
if(var == 'n'):
    print('Okay')
    exit()
secprompt = 'What kind of pets?'
secvar = input(secprompt)
petinfo = [var,secvar]
if(var == 'y'):
    if(secvar == 'dog'):
        print('You have a common pet, which is a dog.')
    elif(secvar == 'cat'):
        print('You have a common pet, which is a cat.')
    else:
        print('You do not have a common pet, which is a', secvar)
