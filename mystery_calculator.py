def mystery_calculator():
    '''Simple arithmetic to calculate a chosen number between 1 and 63. Inspired by a Christmas cracker insert.'''

    print('****Check out the mystery calculator****\n')
    print('Think of a number between 1 and 63. Keep the number secret. Don\'t tell anyone!\n')


    b1 = [(i + j) for i in range(0, 64, 2) for j in range(1, 2)]
    b2 = [(i + j) for i in range(1, 64, 4) for j in range(1, 3)]
    b3 = [(i + j) for i in range(1, 64, 8) for j in range(3, 7)]
    b4 = [(i + j) for i in range(1, 64, 16) for j in range(7, 15)]
    b5 = [(i + j) for i in range(1, 64, 32) for j in range(15, 31)]
    b6 = [(i + j) for i in range(1, 64, 64) for j in range(31, 63)]


    aa1 = (input(f'Is your number any of these {b1}.  Please enter y or n: ')).lower()
    if aa1 == 'y':
        aa1 = int(b1[0])
    else: aa1 = 0


    aa2 = (input(f'\nIs your number any of these {b2}.  Please enter y or n: ')).lower()
    if aa2 == 'y':
        aa2 = int(b2[0])
    else: aa2 = 0


    aa3 = (input(f'\nIs your number any of these {b3}.  Please enter y or n: ')).lower()
    if aa3 == 'y':
        aa3 = int(b3[0])
    else: aa3 = 0


    aa4 = (input(f'\nIs your number any of these {b4}.  Please enter y or n: ')).lower()
    if aa4 == 'y':
        aa4 = int(b4[0])
    else: aa4 = 0


    aa5 = (input(f'\nIs your number any of these {b5}.  Please enter y or n: ')).lower()
    if aa5 == 'y':
        aa5 = int(b5[0])
    else: aa5 = 0


    aa6 = (input(f'\nIs your number any of these {b6}.  Please enter y or n: ')).lower()
    if aa6 == 'y':
        aa6 = int(b6[0])
    else: aa6 = 0


    ans = aa1 + aa2 + aa3 + aa4 + aa5 + aa6


    print('\nThe number you picked is:',ans)
    print('\nThank you for playing the Mystery Calculator.')

mystery_calculator()



