import random
comp_num=random.randint(1, 100)
prompt='What is your guess? Between 1 and 100. '
num_guesses=0
while True:
  person_guess=raw_input(prompt)
  if (comp_num==int(person_guess)):
    num_guesses=num_guesses+1
    print "You're Correct!"
    print 'Number of guesses: ',
    print num_guesses
    break
  elif (comp_num>int(person_guess)):
    print 'Too low!'
    num_guesses=num_guesses+1
  elif (int(person_guess)>100):
    raise RuntimeError('Invalid input')
  else:
    print 'Too High!'
    num_guesses=num_guesses+1
  if (num_guesses==5):
    print 'game over'
    print ' '
    print 'The correct number was ',
    print comp_num
    print 'Nice try!'
    break
