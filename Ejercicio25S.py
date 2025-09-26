import pandas as pd

Data={
    "ID":[1,2,3,4,5],
    "Fechas": ["1990-09-02", "1985/12/15", "2000-07-30", "1995-03-25", "1988/11/05"],
    "Nombre":["Ana","Luis","Luis","Carlos","Mary"],
    "Salario en dólares":[1.500,1.200,2.100,2.900,4.700]
}
df=pd.DataFrame(Data)

#Convertir "ID" A ENTERO
df["ID"]=pd.to_numeric(df["ID"], errors="coerce")

#CONVERTIR "Salario en dólares" A FLOAT
df["Salario en dólares"]=pd.to_numeric(df["Salario en dólares"], errors="coerce")
print(f"DataFrame convertido:\n{df}")

#CONVERTIR FECHA A DATATIME
df["Fechas"] = pd.to_datetime(df["Fechas"], dayfirst=True, errors='coerce')
print(f"DataFrame con fechas convertidas:\n{df}")
print("*"*100)



