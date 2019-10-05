import random

r = random.randint(1, 9)
while True:
    print('Enter a number to guess:')
    n = int(input())
    if n < r:
        print('Your number is too small,try again.')
        continue
    elif n > r:
        print('Your number is too large,try agin.')
        continue
    else:
        print('You are right,the number is '+str(r))
        break


    
