def presentacion():
    print("Calculador de sueldo")
    print("*******************************")

def carga_suma():
    valor1=int(input("Ingrese la cantidad de horas trabajadas:"))
    valor2=36.92
    suma=valor1*valor2
    print("Tu total a cobrar es de:",suma)

#Jornada laboral max 8 horas
#Dias laborales Lunes Viernes 
#Mes laboral de 30 dias 
#El valor por hora lo defini segun lo que encontre en internet

presentacion()
carga_suma()
