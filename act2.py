cont1=0
cont2=0
gastos=0
x=1
n=int(input("Cuentos empleados tiene la empresa:"))
while x<=n:
    sueldo=float(input("Ingrese el sueldo del empleado:"))
    if sueldo<=300:
        cont1=cont1+1
    else:
        cont2=cont2+1
    gastos=gastos+sueldo
    x=x+1
print("Cantidad de empleados con sueldos entre 100 y 300")
print(cont1)
print("Cantidad de empleados con sueldos mayores a 300")
print(cont2)
print("Los gatos de la empresa en sueldos")
print(gastos)


