prompt = 'Do you have any pets?'
var = input(prompt)
if var == 'no':
    print('Okay')
    exit()
secprompt = 'What kind of pets?'
secva = input(secprompt)
petinfo = [var, secva]
if var == 'y':
    if secva == 'dog':
        print('You do have a common pet, which is a dog.')
    elif secva == 'cat':
        print('You do have a common pet, which is a cat.')
    else:
        print("You don't have a common pet, which is a", secva)
print(petinfo[0])
