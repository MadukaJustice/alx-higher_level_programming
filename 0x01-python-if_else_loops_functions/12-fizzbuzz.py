#!/usr/bin/python3

def fizzbuzz():
    for n in range(1, 101):
        if n % 15 == 0:
            print(f'FizzBuzz ', end='')
        elif n % 3 == 0:
            print(f'Fizz ', end='')
        elif n % 5 == 0:
            print(f'Buzz ', end='')
        else:
            print('{} '.format(n), end='')
