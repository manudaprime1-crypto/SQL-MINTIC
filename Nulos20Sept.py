import pandas as pd
Datos=({
    "Id=Empleados":[101,102,103,104,105,106,107],
    "Nombre":["James Rodriguez", "Lionel Messi", None, "Falcao Garcia", "Earling Halaand", "Kevin De Bruyne", "Dibu Martinez"],
    "Edad": [34,38,None,39,26,35,33],
    "Equipo":["León mx", "Inter Miami", "AlNassr", None, "Manchester City", "Fiorentina", "Aston Villa"],
    "Posición":["Volante","Delantero","Delantero","Delantero",None, "Volante Creador", "Arquero"],
    "Años de Contrato":['2025', '2024', '2022', '2024', '2021', '2025',None],
    "Salario": [None,400.000,800.000,10.000,21.000,15.000,20.000]
})

df=pd.DataFrame(Datos)
print("*"*100)

#Identificar Valores Nulos
print("Cantidad De nulos En cada Columna")
print(df.isnull().sum())
print("*"*100)

#Mostrar la información de nuestro dataframe con valores nulos
print("DataFrame con información:")
print(df.info())
print("*"*100)

print("Elimina filas de los valores nulos:")
print(df.dropna(how="all", inplace=True))
print("*"*100)

print("Reemplazar valores nulos con valor específico:")
df["Edad"]=df["Edad"].fillna(0)
print(df[["Nombre","Edad"]].head())
print("*"*100)


print("Reemplazar valores nulos con valor de la media:")
df["Edad"]=df["Edad"].fillna(df["Edad"].median())
print(df[["Nombre","Edad"]].head)
print("*"*100)

print("Reemplazar valores nulos con valor promedio:")
df["Salario"]=df["Salario"].fillna(df["Salario"].mean())
print(df[["Nombre","Salario"]].head())
print("*"*100)

print("Reemplazar valores nulos con valor de a moda:")
df["Salario"]=df["Salario"].fillna(df["Salario"].mode())
print(df[["Nombre","Salario"]].head())
print("*"*100)
