def hangman():
    # to play the hangman word game
    import webbrowser  # will be used later to look up definition of word
    from random_word import \
        RandomWords  # to generate the word to be guessed. from https://pypi.org/project/Random-Word/
    r = RandomWords()
    word = r.get_random_word(hasDictionaryDef="true", minLength=5, maxLength=7, minDictionaryCount=1)
    word = list(word)  # cast the str to a list in order to index pop and insert later
    result = word.copy()  # to compare answer with as the word list above will be changing.

    print("\nLet's play Hangman!")
    print('-' * 19, '\n')

    answer = '_' * len(word)
    answer = list(
        answer)  # this an the line above provides the blank asnwer template. Made to a list for index pop and insert.
    noose = 0  # the incrementor for wrong guesses

    def gallows():
        # the function builds the gallows incrementally for each wrong answer
        if noose == 1:
            print('______')
        elif noose == 2:
            print('   |')
            print('   |')
            print('   |')
            print('   |')
            print('   |')
            print('   |')
            print('___|___')
        elif noose == 3:
            print('    ____')
            print('   |')
            print('   |')
            print('   |')
            print('   |')
            print('   |')
            print('   |')
            print('___|___')
        elif noose == 4:
            print('    ____')
            print('   |    |')
            print('   |')
            print('   |')
            print('   |')
            print('   |')
            print('   |')
            print('___|___')
        elif noose == 5:
            print('    ____')
            print('   |    |')
            print('   |    O')
            print('   |')
            print('   |')
            print('   |')
            print('   |')
            print('___|___')
        elif noose == 6:
            print('    ____')
            print('   |    |')
            print('   |    O')
            print('   |    |')
            print('   |')
            print('   |')
            print('   |')
            print('___|___')
        elif noose == 7:
            print('    ____')
            print('   |    |')
            print('   |    O')
            print('   |   \|')
            print('   |')
            print('   |')
            print('   |')
            print('___|___')
        elif noose == 8:
            print('    ____')
            print('   |    |')
            print('   |    O')
            print('   |   \|/')
            print('   |')
            print('   |')
            print('   |')
            print('___|___')
        elif noose == 9:
            print('    ____')
            print('   |    |')
            print('   |    O')
            print('   |   \|/')
            print('   |    |')
            print('   |')
            print('   |')
            print('___|___')
        elif noose == 10:
            print('    ____')
            print('   |    |')
            print('   |    O')
            print('   |   \|/')
            print('   |    |')
            print('   |   / ')
            print('   |')
            print('___|___')
        elif noose == 11:
            print('   ____')
            print('   |    |')
            print('   |    O')
            print('   |   \|/')
            print('   |    |')
            print('   |   / \ ')
            print('   |')
            print('___|___')
            x = ''.join(result)
            print('\nYOU\'RE DEAD!!! The word was', x.upper() + '.')
            wp = 'https://www.onelook.com/?w=' + x
            webbrowser.open(wp)
            hangman()

    gl = []  # creates a list to populate with guessed letters
    while answer != result:  # result is a copy of the original word (to be guessed) list
        guess = input('\nGuess a letter: ')
        gl.extend(guess)  # adds the guessed letter to the guessed letter list
        glj = ', '.join(gl)  # casts the list to s string as it can look nicer printed this way

        if guess not in word:
            print(
                f'\n"{guess.upper()}" is not in the word. Letters guessed so far are: {glj.upper()}. Have another go.')
            ad = ''.join(answer)  # ad is short for answerdisplay. Looks better formated as a string
            print('\n', ad.upper())
            noose += 1  # trigger for advancing build of the gallows
            gallows()  # initiates gallows function

        else:
            # while loop to check if guessed letter appears in word as index method will only find first one. pop removes
            # the first instance so if there any more of them they can be found. This means if a guessed letter
            # appears more than once in the word it will show up as many times as that in the answer meaning you don't
            # have to guess the same letter more than once! Thank you Otis for the feedback!
            while guess in word:
                guessindex = word.index(guess)  # finds index of letter guessed in word
                answer.pop(guessindex)  # removes the element at the index
                answer.insert(guessindex, guess)  # adds the correct guessed letter to the correct index
                word.pop(guessindex)  # repeat of the above
                word.insert(guessindex, '-')  # as above

            display = ''.join(answer)  # looks better formatted as a string
            print(display.upper())

    print('\nWell done! You got it!', display.upper(), 'was the word.')
    wp = 'https://www.onelook.com/?w=' + display  # opens up a web page with a definition of the word.
    webbrowser.open(wp)
    hangman()


hangman()
