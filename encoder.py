def encoder():
    '''This function coverts a user entered string to the NATO phonetic alphabet and morse code'''

    import textwrap

    intro = '''
    The NATO phonetic alphabet is the most widely used radiotelephone spelling alphabet. It is officially the 
    International Radiotelephony Spelling Alphabet, and also commonly known as the ICAO phonetic alphabet, with a 
    variation officially known as the ITU phonetic alphabet and figure code. The International Civil Aviation 
    Organization (ICAO) assigned codewords acrophonically to the letters of the English alphabet, so that critical 
    combinations of letters and numbers are most likely to be pronounced and understood by those who exchange voice 
    messages by radio or telephone, regardless of language differences or the quality of the communication channel.
    
    The 26 code words in the NATO phonetic alphabet are assigned to the 26 letters of the English alphabet in 
    alphabetical order as follows: 
    
    Alfa, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliett, Kilo, Lima, Mike, November, Oscar, Papa,
    Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu.
    
    Morse code is a method used in telecommunication to encode text characters as standardized sequences of two 
    different signal durations, called dots and dashes or dits and dahs.[2][3] Morse code is named for Samuel Morse, 
    an inventor of the telegraph.
    
    The International Morse Code encodes the 26 English letters A through Z, some non-English letters, 
    the Arabic numerals and a small set of punctuation and procedural signals (prosigns). There is no distinction 
    between upper and lower case letters. Each Morse code symbol is formed by a sequence of dots and dashes. 
    '''

    textwrap.wrap(intro, width=70)
    intro = textwrap.dedent(intro)
    print(intro)

    text = input('\nText entered here will be converted to the NATO phonetic alphabet and morse code: ')

    phoneticalpha = {'A': 'alpha', 'B': 'bravo', 'C': 'charly', 'D': 'delta', 'E': 'echo', 'F': 'foxtrot', 'G': 'golf',
                     'H': 'hotel', 'I': 'india'
        , 'J': 'juliet', 'K': 'kilo', 'L': 'lima', 'M': 'mike', 'N': 'november', 'O': 'oscar', 'P': 'papa',
                     'Q': 'quebec', 'R': 'romeo',
                     'S': 'sierra', 'T': 'tango', 'U': 'uniform', 'V': 'victor', 'W': 'whisky', 'X': 'xray',
                     'Y': 'yankee', 'Z': 'zulu', ' ': ' '}

    text = text.upper()
    code = []

    for i in text:
        code.append(phoneticalpha[i])
    joinAlla = ' '.join(code)
    pa = joinAlla.title()

    morse = {'A': '•-', 'B': '-•••', 'C': '-•-•', 'D': '-••', 'E': '•', 'F': '••-•', 'G': '--•', 'H': '••••', 'I': '••',
             'J': '•---', 'K': '-•-',
             'L': '•-••', 'M': '--', 'N': '-•', 'O': '---', 'P': '•--•', 'Q': '--•-', 'R': '•-•', 'S': '•••', 'T': '-',
             'U': '••-', 'V': '•••-',
             'W': '•--', 'X': '-••-', 'Y': '-•--', 'Z': '--••', ' ': ' '}

    mc = text.upper()
    code = []

    for i in mc:
        code.append(morse[i])
    joinAllm = ' '.join(code)
    mc = joinAllm

    print(f'\n{text} converted to the NATO phonetic alaphabet is: {pa} \n\n{text} converted to morse code is: {mc}')
    print('\nThank you for using the encoder. We hope you found it of some interest.')


encoder()
