def fizzbuzz(num):

    '''It would be be remiss not to include this...

    FizzBuzz is played in a group, where players take it in turns to say the next number in a sequence,
    counting one at a time. If the number is divisible by three, the player must say, "Fizz" instead of the number itself;
    if the number is divisible by five, the player must say, "Buzz"; and if the number is divisible by three and five,
    the player has to say, "Fizz buzz".'''

    num = int(num)
    for n in range(1, num + 1):
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(n)

fizzbuzz(input('Enter a number to FizzBuzz up to: '))
