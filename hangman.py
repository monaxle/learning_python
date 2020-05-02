def hangman():
    # to play the hangman word game
    import webbrowser
    from random_word import RandomWords
    r = RandomWords()
    word = r.get_random_word(hasDictionaryDef="true", minLength=5, maxLength=7, minDictionaryCount=1)
    word = list(word)
    result = word.copy()  # to compare answer with.
    print("\nLet's play Hangman!")
    print('-' * 19, '\n')

    answer = '-' * len(word)
    answer = list(answer)
    noose = 0

    def picture():
        # prints the gallows in stages
        if noose == 1:
            print('________')
        elif noose == 2:
            print('    |')
            print('    |')
            print('    |')
            print('    |')
            print('    |')
            print('    |')
            print('____|____')
        elif noose == 3:
            print('     ____')
            print('    |')
            print('    |')
            print('    |')
            print('    |')
            print('    |')
            print('    |')
            print('____|____')
        elif noose == 4:
            print('     ____')
            print('    |    |')
            print('    |')
            print('    |')
            print('    |')
            print('    |')
            print('    |')
            print('____|____')
        elif noose == 5:
            print('     ____')
            print('    |    |')
            print('    |    O')
            print('    |')
            print('    |')
            print('    |')
            print('    |')
            print('____|____')
        elif noose == 6:
            print('     ____')
            print('    |    |')
            print('    |    O')
            print('    |    |')
            print('    |')
            print('    |')
            print('    |')
            print('____|____')
        elif noose == 7:
            print('     ____')
            print('    |    |')
            print('    |    O')
            print('    |   \|')
            print('    |')
            print('    |')
            print('    |')
            print('____|____')
        elif noose == 8:
            print('     ____')
            print('    |    |')
            print('    |    O')
            print('    |   \|/')
            print('    |')
            print('    |')
            print('    |')
            print('____|____')
        elif noose == 9:
            print('     ____')
            print('    |    |')
            print('    |    O')
            print('    |   \|/')
            print('    |    |')
            print('    |')
            print('    |')
            print('____|____')
        elif noose == 10:
            print('     ____')
            print('    |    |')
            print('    |    O')
            print('    |   \|/')
            print('    |    |')
            print('    |   / ')
            print('    |')
            print('____|____')
        elif noose == 11:
            print('     ____')
            print('    |    |')
            print('    |    O')
            print('    |   \|/')
            print('    |    |')
            print('    |   / \ ')
            print('    |')
            print('____|____')
            x = ''.join(result)
            print('\nYOU\'RE DEAD!!! The word was', x.upper() + '.')
            wp = 'https://www.onelook.com/?w=' + x
            webbrowser.open(wp)
            hangman()

    gl = []
    while answer != result:
        guess = input('\nGuess a letter: ')
        gl.extend(guess)
        glj = ','.join(gl)

        if guess not in word:
            print(f'\nBad luck! {guess} is not in the word. Have another go. \n\nLetters guessed so far are: {glj.upper()}')
            ad = ''.join(answer)
            print('\n', ad.upper())
            noose += 1
            picture()

        else:
            guessindex = word.index(guess)
            answer.pop(guessindex)
            answer.insert(guessindex, guess)
            word.pop(guessindex)
            word.insert(guessindex, '-')
            display = ''.join(answer)
            print(display.upper())

    print('Well done! You got it!', display.upper(), 'was the word.')
    wp = 'https://www.onelook.com/?w=' + display
    webbrowser.open(wp)
    hangman()


hangman()