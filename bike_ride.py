def hows_the_x(traffic, weather, fitness, bike, company):
    '''A simple rating scale which takes five variables and returns the average accompanied by a contrived summary.
    May easily be adapted to suit your fancy.'''

    traffic = int(traffic)
    weather = int(weather)
    fitness = int(fitness)
    bike = int(bike)
    company = int(company)

    t = traffic + weather + fitness + bike + company
    t = int(t / .5)
    ts = str(t)

    if t <= 0:
        return '\nThat\'s a ' + ts + ' % bike ride. You\'re lucky to still be alive! Go and have a lie down.'
    elif t > 0 and t <= 10:
        return '\nThat\'s a ' + ts + ' % bike ride. Blimy \'O\' Reily! Things can only get better.'
    elif t > 10 and t <= 20:
        return '\nThat\'s a ' + ts + ' % bike ride. Told you things would get better'
    elif t > 20 and t <= 30:
        return '\nThat\'s a ' + ts + ' % bike ride. The toughest part is getting started.'
    elif t > 30 and t <= 40:
        return '\nThat\'s a ' + ts + ' % bike ride. Well done for having a go.'
    elif t > 40 and t <= 50:
        return '\nThat\'s a ' + ts + ' % bike ride. Nearly half way to enjoying yourself! Keep at it.'
    elif t > 50 and t <= 60:
        return '\nThat\'s a ' + ts + ' % bike ride. More good than bad.'
    elif t > 60 and t <= 70:
        return '\nThat\'s a ' + ts + ' % bike ride. Don\'t take it for granted. Keep up the good work.'
    elif t > 70 and t <= 80:
        return '\nThat\'s a ' + ts + ' % bike ride. Lot\'s of positive gains being felt.'
    elif t > 80 and t <= 90:
        return '\nThat\'s a ' + ts + ' % bike ride. Why did you stop?'
    elif t > 90 and t <= 100:
        return '\nThat\'s a ' + ts + ' % bike ride. You crushed it peloton!.'
    else:
        return '\nThat\'s a ' + ts + ' % bike ride. You must be tripping!'


print('How was your bike ride? Rate the following five aspects of your ride. 0 (the worst) 10 (the best).')


print(hows_the_x(input('\nTraffic: '), input('\nWeather: '), input('\nFitness: '),
                 input('\nBike: '),
                 input('\nCompany: ')))
