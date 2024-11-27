opcion=1
print("Hola Bienvenida Al Programa")
while opcion!=0:
    print("Ingresa 1. Area Triangulo")
    print("Ingresa 2. Area Rectangulo")
    print("Ingresa 3. Area Circulo")
    print("Ingresa 4. Convertir temperatura °F a °C")
    print("Ingresa 5. Convertir temperatura °C a °F")
    print("Ingresa 0. Salir del programa")
    op=int(input("¿Que actividad quieres realizar?"))
    if(op==1):
        base=int(input("Ingresa la base del triangulo"))
        altura=int(input("Ingresa la altura del triangulo"))
        res=base*altura/2
        print("El area de el triangulo es", res)
    elif(op==2):
        base=int(input("Ingresa la base del rectangulo"))
        altura=int(input("Ingresa la altura del rectangulo"))
        res=base*altura
        print("El area del rectangulo es", res)
    elif(op==3):
        radio=int(input("cual es el radio del circulo"))
        res=3.14*radio*radio
        print("El ara del circulo es", res)
    elif(op==4):
        f=int(input("¿que grado fahrenheit quieres covertir a grados Centigrados?"))
        res=(f-32)*5/9
        print("Tus grados centigrados serian", res)
    elif(op==5):
        c=int(input("¿Cuantois grados centigrados quieres covbertir a fahrenheit?"))
        res=c*9/5+32
        print("Los grados fahrenheit serian",res)
    else:
        print("No valido")
    opcion=int(input("Deseas continuar, sino preciona 0. para salir"))
        
        