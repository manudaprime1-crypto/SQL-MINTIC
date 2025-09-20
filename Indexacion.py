import pandas as pd
Empleados=pd.DataFrame({
    "Id=Empleados":[101,102,103,104,105,106,107],
    "Nombre":["James Rodriguez", "Lionel Messi", "Cristiano Ronaldo", "Falcao Garcia", "Earling Halaand", "Kevin De Bruyne", "Dibu Martinez"],
    "Edad": [34,38,40,39,26,35,33],
    "Equipo":["León mx", "Inter Miami", "Al Nassr", "Millonarios", "Manchester City", "Fiorentina", "Aston Villa"],
    "Posición":["Volante","Delantero","Delantero","Delantero","Delantero", "Volante Creador", "Arquero"],
    "Años de Contrato":['2025', '2024', '2022', '2024', '2021', '2025','2022'],
    "Salario": [10.000,400.000,800.000,10.000,21.000,15.000,20.000]
})


print(Empleados)
print("*"*100)
print("Indexación Por Nombres:")
print("Registro 2:")
print(Empleados.iloc[1])
print("*"*100)
print("Registro 1:")
print(Empleados.loc[0])
print("*"*100)
print("Registro 1:")
print(Empleados.loc[:,["Nombre","Edad"]])
print("*"*100)
print("Empleados a pensionarse:")
print(Empleados[Empleados["Edad"]>=50])
print("*"*100)
print("Imprime 3 registros:")
print(Empleados.loc[0:2])
print("*"*100)
print("Imprime Rangos:")
print(Empleados.iloc[0:2,0:3])
print("*"*100)
print("Nueva Columna de Comisión:")
Empleados["Comision"]=Empleados["Salario"]*0.08
Empleados["Salario Total"]=Empleados["Salario"]+Empleados["Comision"]
Empleados.loc[Empleados["Salario"]<=35000,"Salario"]+=2500
print(Empleados)
print(Empleados[["Nombre", "Salario","Comision","Salario Total"]])
print("*"*100)
Empleados["Perfil"]=Empleados["Equipo"]+"-"+Empleados["Posición"]
print(Empleados)
print("*"*100)
Empleados=Empleados.drop(columns=["Perfil"])
print(Empleados)
Empleados=Empleados.rename(columns={"Id_Empleados":"Id"})
print(Empleados)
