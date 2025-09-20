import pandas as pd

datos = {
    "Frutas": ["manzana", "Peras","Bananas","Naranja"],
    "Precio": [2.5,3.0,1.8,2.2],
    "Cantidad": [100,150,200,80],
    "Mes": ["Enero", "Enero", "Febrero", "Febrero"]
    
}

#Filas Mes Enero
print(Frutas[Frutas["Mes"]=="Enero"])
print("*"*100)

#Columnas producto y cantidad vendida
print(Frutas[["Producto","Cantidad Vendida"]])
print("*"*100)

#Columna Precio Modificada en un 10%

Frutas["Precio"]=Frutas["Precio"]*1.10
print(Frutas)
print("*"*100)

#Nueva Columna Ingreso

Frutas["Ingreso"]=Frutas["Precio"]*Frutas["Cantidad Vendida"]
print(Frutas)
print("*"*100)
