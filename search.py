number = input("Please think of a number between 0 and 100!")
low = 1
high = 100
ans = str((low + high) / 2)
answer = ''
find = False

while not(find):
    ans = int((low + high) / 2)

    while True:
        print('Is your secret number {}?'.format(ans))
        answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        if answer != 'c' and answer != 'h' and answer != 'l':
            print('Your input is invalid.You can type just "c", "l" or "h"')
        else:
            break

    if answer == 'h':
        low = ans
    elif answer == 'l':
        high = ans
    elif answer == 'c':
        print('Game over. Your secret number was:{}'.format(number))
        find = True
