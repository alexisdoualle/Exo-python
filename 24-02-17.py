import math as m

def approxFacto(x):
    n = ((x/m.e)**x) * m.sqrt(2*m.pi*x) #formule de Stirling
    print("factorielle de {} =          {:e}".format(x,m.factorial(x)))
    n *= (1+1/(12*x)) #amélioration
    print("avec Stirling*(1+1/12n) =    {:e} \n".format(n))
    return n

def syr(x):
        while x<1:
            print("le nombre entré n'est pas supérieur à 0")
            x = int(input("entrez un entier supérieur à 0"))
        while x != 1:
            if x%2 == 0:
                x = int(x/2)
            else:
                x = 3*x +1
            print("x = {}".format(x))
