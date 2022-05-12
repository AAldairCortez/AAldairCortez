suma=0
x=1
n=int(input("Escribe cuantas personas quieres medir: "))
while x<=n:
    altura=float(input("Escribe la altura: "))
    suma=suma+altura
    x=x+1
promedio=suma/n
print("Altura promedio")
print(promedio)