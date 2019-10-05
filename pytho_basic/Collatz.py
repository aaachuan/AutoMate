def Collatz(number):
    while number != 1:
        if number % 2 == 0:
            print(number // 2)
            return Collatz(number // 2)
        else:
            print(3 * number + 1)
            return Collatz(3 * number + 1)


print('Enter number:')
try:
    n = int(input())
except ValueError:
    print('Error: Invalid input,it must be a number.')
Collatz(n)
