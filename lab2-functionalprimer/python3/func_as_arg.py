def listFunc(a,b):
    return [i for i in range(a, b)] #Create list of ints from 1 to 5, Haskell equivalent [1..5]

def applicatorFunc(inpFunc,a,b ,s):
    if s=='s':
        return sum(inpFunc(a,b))
    else:
        return sum(inpFunc(a,b))/(b-a)




print(applicatorFunc(listFunc,1, 5 , 's'))

