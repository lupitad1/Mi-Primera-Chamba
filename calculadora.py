opcion=1
#En un ciclo while  realiza operaciones hasta que el usuario escriba 0
while opcion!=0:
    num1=int(input("Ingresa el primer numero"))
    num2=int(input("Ingresa el segundo numero"))
    print("Ingresa 1. Sumar")
    print("Ingresa 2. Restar")
    print("Ingresa 3. Multiplicar")
    print("Ingresa 4. Dividir")
    op=int(input("¿Que operacion  quieres hacer con esos numeros?"))
    if(op==1):
        res=num1+num2
        print("La suma de los numeros es:", res)
    elif(op==2):
        res=num1-num2
        print("La resta de los numeros es:", res)
    elif(op==3):
        res=num1*num2
        print("La multiplicacion de estos numeros es:", res)
    elif(op==4):
        res=num1/num2
        print("La division de los numeros es:",res)
    else:
        print("No valido")
    opcion=int(input("Deseas Continuar, sino preciona 0. para salir"))