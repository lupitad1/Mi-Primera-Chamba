#Crear un funcion

#Funcion llamada saludar, va a recibir el nombre 
def saludar(nombre) :
    print("Holaaaa", nombre)
    
nom=input("Ingresa tu nombre")
saludar(nom)

#Funcion llamada sumita, va a recibir 5 numeros

#Va a regresar el valor de la suma
def sumita(n1,n2,n3,n4,n5):
    res_suma=n1+n2+n3+n4+n5
    return res_suma

num1=int(input("Ingresa el primer numero"))
num2=int(input("Ingresa el segunda numero"))
num3=int(input("Ingresa el tercer numero"))
num4=int(input("Ingresa el cuarto numero"))
num5=int(input("Ingresa el quinto numero"))

#Mandar llamar a la funcion/ usarla
print(sumita(num1,num2,num3,num4,num5))

#Crear una funcion llamada area_triangulo
#Que reciba base y altura
##Regresa el resultado del area
def area_triangulo(b,h):
    area=(b*h)/2
    return area
#Usar la funcion
print(area_triangulo(4,5))

#Ejercicios
'''1)Crear una funcion llamada multiplicar que reciba 3 numeros, egresar el resultado'''
def multiplicar(num1,num2,num3):
    res_multiplicacion=(num1*num2*num3)
    return res_multiplicacion

num1=int(input("Ingresa el primer numero"))
num2=int(input("Ingresa el segundo numero"))
num3=int(input("Ingresa el tercero numero"))
print(multiplicar(num1,num2,num3))