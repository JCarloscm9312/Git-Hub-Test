def maxx(a,b):
    if a > b:
        print(a)
    else:
        print(b)

def maxx3(a,b,c):
    if (a>b) and (a>c):
        print(a)
    elif (b>a) and (b>c):
        print(b)
    else:
        print(c)
def lenlist(*lista):
    x = 0
    for i in lista:
        x +=1
    print("Tamaño de la lista = {}".format(x))


def inversa(cad):
    dac = ""
    for i in cad:
        dac =  i + dac
    print(dac)

def es_palindromo(cad):
    print(cad)
    dac = str(inversa(cad))
    print(type(dac))
    print(type(cad))
    if cad == dac:
        print("Es palindromo")
    else:
        print("no es palindromo")

def histo(*lista):
    for i in lista:

        print("*" * i)
       
#s = 0
#for i in range(1001):

    
 #   if (i%3 == 0) or (i%5 == 0):
#        s += i
#print(s)

"""
fin = 0
cuenta = 1
lista = []
while fin <= 1000000:
    if (cuenta%3 ==0) or ("9" in str(cuenta)):
        x = ":("
    else:
        lista.append(cuenta)
    cuenta +=1
    fin = len(lista)

print(lista[1000000])    
"""

for x in range(2, 94931):
    for y in range(2, 94931):
        n1 = int(str(x) + str(y))
        n2 = int(str(y) + str(x))
        if n1 + n2 == 94932:
            print("X: {}   Y: {}".format(x, y))
        
