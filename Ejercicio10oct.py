
# Numero= int(input("Ingrese un número entero:"))
# if Numero>=10 and Numero<=20:
#     print(True)
# else:
#     print(False)
    
    
    
# #Ejercicio 2
# Numero= int(input("Ingrese un número entero:"))
# if Numero %2==0:
#     print("Par")
# else:
#     print("Impar")

#Ejercicio 3
# cadena1 = str(input("Ingrese la primera cadena:"))
# cadena2 = str(input("Ingrese la segunda cadena:"))
# if cadena1 == cadena2:
#     print(True)
# else:
#     print(False)


# Ejercicio 4
# TamanoDelTornillo = float(input("Ingrese el tamaño del tornillo en centímetros"))
# if TamanoDelTornillo >= 3 and TamanoDelTornillo <= 5:
#     print("es mediano")
# elif TamanoDelTornillo >= 5 and TamanoDelTornillo <= 6.5:
#     print("es grande")
# elif TamanoDelTornillo >= 6.5  and TamanoDelTornillo <= 8.5:
#     print("es muy grande")
# elif TamanoDelTornillo >= 8.5:
#     print("es gigante")


#Ejercicio 5
# Lado1 = float(input("Ingrese la longitud del lado 1: "))
# Lado2 = float(input("Ingrese la longitud del lado 2: "))
# Lado3 = float(input("Ingrese la longitud del lado 3: "))

# if Lado1 == Lado2 == Lado3:
#     print("Este es un triángulo equilatero")
# elif Lado1 == Lado2 or Lado2 == Lado3:
#     print("Este es un triángulo isósceles")
# else:
#     print("Este triángulo es escaleno")



#Ejercicio 6

# x=int(input("Ingrese la cantidad de empleados: "))

# conteo1=0
# conteo2=0
# gasto=0

# for i in range (1,x+1):
#     while True:
#         sueldo=int(input(f"Ingrese el sueldo del empleado: "))
#         gasto+=sueldo
#         if sueldo>= 100 and sueldo <=300:
#             conteo1+=1
#             break
#         elif sueldo >= 301 and sueldo >=500:
#             conteo2+=1
#         break
# print(f"Empleados que cobran entre $100 y $300: {conteo1}")
# print(f"Empleados que cobran más de $300: {conteo2}")
# print(f"Gasto total en sueldos: {conteo1*300+conteo2*500}")

