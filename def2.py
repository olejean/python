def privetstvie(name, *args):
    ''' Напечатать приветствие'''
    print("privet", name, *args)



test = privetstvie('olejean', 12)
print(test)