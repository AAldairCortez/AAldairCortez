def presentacion():
    print("Programa para obtener total de compra.")
    print("*******************************")


def carga_suma():
    valor1=int(input("Ingrese el precio del producto: "))
    valor2=int(input("Ingrese la cantidad del producto: "))
    suma=valor1*valor2
    print("Su total a pagar es:",suma)


def finalizacion():
    print("*******************************")    
    print("Gracias por utilizar este programa")


presentacion()
carga_suma()
finalizacion()