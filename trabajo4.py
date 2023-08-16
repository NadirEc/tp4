#1)Escriba una función que muestre todos los números primos entre 1 y un número n que es
#ingresado por parámetro.

"""def esprimo(numero):
    for k in range(2,numero-1):
        if numero%k==0:
            return False
        return True
    
def mostrarprimoshasta(n):
    for i in range(2,n):
        if esprimo(i):
            print(i,end=" ")
mostrarprimoshasta(1)  """

#2) Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta
#que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje
#avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del
#programa de acuerdo a estos criterios:
#• Use un test condicional en el ciclo while para detener la ejecución.
#• Use un test condicional dentro del ciclo para decidir si continuar la ejecución. 

"""def hacer_sandwich():
    condimento = input("Ingrese un condimento para el sándwich : ")
    
    while condimento != 'salir':
        print(f"Se ha agregado {condimento} al sándwich.")
        condimento = input("Ingrese otro condimento (o 'salir' para terminar): ")

    print("El sándwich está listo.")

hacer_sandwich()"""


"""def hacer_sandwich():
    condimento = input("Ingrese un condimento para el sándwich:")
    
    while True:
        if condimento == 'salir':
            break
        
        print(f"Se ha agregado {condimento} al sándwich.")
        condimento = input("Ingrese otro condimento:")

    print("El sándwich está listo.")"""

#3) A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un
#tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje
#describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez
#usando argumentos por posición. Llámela una segunda vez usando argumentos por clave.
#B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por
#defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los
#valores por defecto, y la segunda con valores diferentes. 

"""def hacer_remera(tamaño, mensaje):
    print("La remera es de tamaño", tamaño)
    print("Mensaje impreso en la remera:", mensaje)

hacer_remera("M", "toma tu remera")

hacer_remera(tamaño="S", mensaje="accion")"""



#B)
"""def hacer_remera(tamaño="L", mensaje="Me gusta Python"):
    print("La remera es de tamaño", tamaño)
    print("Mensaje en la remera:", mensaje)

hacer_remera()

hacer_remera(tamaño="XL", mensaje="holaa")"""

#4) Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros 
#de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo 
#número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …).

def fibonacci(n):
    if n == 0:
        return 

    if n == 1:
        return 









