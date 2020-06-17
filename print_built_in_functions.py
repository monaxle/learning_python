'''

11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
'''

def get_some_info():
    ui = (input('Type the name of the function you want to find out more about: '))
    hds = (input("Type 'ds' for the doc string or 'h' for the help info: "))
    if hds == 'ds':
       print(eval(ui + ".__doc__"))  #check out the eval() function!
    elif hds == 'h':
       return help(ui)

get_some_info()


#s = input('\nType the name of the function you want to find out more about: ')
#if s in dir(__builtins__):
#    print(eval(s+".__doc__"))
