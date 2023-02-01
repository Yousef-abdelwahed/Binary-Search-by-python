from pickle import FALSE
print('Please think of a number between 0 and 100')
low = 0
high = 100
mid = (low+high)//2
state = True

while state:
    print('is your number is ' + str(mid))
    guess = input(" 'h' high, 'l' low, 'S' seccess ")
    if guess == 's':
        print('Game Over Your Secret Number was :' + str(med))
        state = FALSE
    elif guess == 'h':
        high = med
        med = (high + low)//2
    elif guess == 'l':
        low = mid
        mid = (high + low) // 2
    else:
        print('sorry , I did not unerstand you')
