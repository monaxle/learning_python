#calculate total cost of meal with three var: meal cost, tip rate (%) and tax rate (%).

def meal_cost(mealCost,tipPercent,taxPercent):
    mealCost = float(mealCost)
    tipPercent = float(tipPercent)
    taxPercent = float(taxPercent)

    tip = (mealCost) * tipPercent / 100
    tax = mealCost * taxPercent / 100
    totalCost = mealCost + tip + tax
    ans = round(totalCost,2) #round to two decimal places
    return f'The cost of the meal including the tip and tax is: £{ans}'


print(meal_cost(input('How much was the meal: '),input('How much do you tip (percent): '),input('What\'s the tax rate (percent): ')))
