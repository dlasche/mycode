#!/usr/bin/env python3

#FizzBuzz Challenge

def main():
    x = 0
    while x < 100:
        x+=1
        if x%3 == 0 and x%5 == 0:
            print('FizzBuzz')
        elif x%3 == 0:
            print('Fizz')
        elif x%5==0:
            print('Buzz')
        else:
            print('Value of x is:', x)


if __name__ == '__main__':
    main()
