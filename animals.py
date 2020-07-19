def list_animals(animals):
    list = ''
    x=0
    for i in animals:
        list += str(x+1) + '. ' + animals[x] + '\n'
        x+=1
    return list
