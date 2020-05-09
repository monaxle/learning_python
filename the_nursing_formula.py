def the_nursing_formula():
    ''' the ‘nursing formula': volume to administer  = dose required (what you want) * volume of solution (what you got)
     / solution strength (what is in it)’'''

    # inputs block
    medication = str(input('Name of medication: '))

    while True:
        try:
            dose_required = int(input('Amount prescribed (mg): '))
            break
        except ValueError:
            print('Numbers only!')
            continue

    while True:
        try:
            vol_solution = int(input('Volume of solution (ml): '))
            break
        except ValueError:
            print('Numbers only!')
        continue

    while True:
        try:
            dose_available = int(input('Solution strength (mg/ml?): '))
            break
        except ValueError:
            print('Numbers only!')
        continue

    # the nursing formula calculation
    vol_to_administer = dose_required * vol_solution / dose_available

    # confirmation of inputs
    print(f'\n{medication} {dose_required}mg is prescribed. You have {medication} {dose_available}mg/{vol_solution}ml.')

    # output block
    tnf = '\n- THE NURSING FORMULA - '
    print(tnf)
    print('-' * len(tnf))
    form = f'Volume to administer = {dose_required}mg (what you want) x {vol_solution}ml (what you got) / {dose_available}mg (what\'s in it)'
    print(form)

    print(
        f'\nVolume to administer = {vol_to_administer}ml')


the_nursing_formula()