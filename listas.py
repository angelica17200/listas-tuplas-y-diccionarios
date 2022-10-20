## Ejercicio practico "Lista"


def capturar ():
    global Lista 
    Lista =[]
    print  ("cuantos elementos va a tener la lista?")
    n=input()
    n=int(n)
    for i in range (0,n):
        print ("Ingresa el Elemento del indice ", i )
        elemento =input()
        Lista.insert(i,elemento)
#Definiendo la funcion de mostrar
def mostrar():
    print (Lista)
#DeFINIENDO LA FUNCION DE AGREGAR 
def agregar():
    print ("Ingresar el Elemento que desea Agregar ")
    elemento=input()
    print ("Ingrese el indice donde desea Agregarlo:")
    indice= input()
    indice=int(indice)
    Logintud=len(Lista)
    Longitud=int(Longitud)
    if (indice>Longitud or indice<0):
        print

capturar()
mostrar()



