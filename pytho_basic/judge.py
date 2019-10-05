import sys

while True:
    print('input a number:')
    spam = int(input())
    if spam == 1:
        print('Hello.')
    elif spam == 2:
        print('Howdy.')
    else:
        print('Greetings!')
    respnse = input()
    if respnse == 'exit':
        sys.exit()
    print('You typed ' + respnse + '.')