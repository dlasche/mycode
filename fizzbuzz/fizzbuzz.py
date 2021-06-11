def fizzbuzz(x):
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

def main():
    x = 0
    fizzbuzz(x)

if __name__ == '__main__':
    main()
