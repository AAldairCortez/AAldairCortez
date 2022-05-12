def main():
    # Introduccion a la Manipulacion de Archivos de Texto
    print('Introduccion a la Manipulacion de Archivos de Texto')

    print()

    #Apertura de un archivo de texto
    print('Apertura de un archivo con un manejador de contexto:')

    nombre_archivo = 'Lenguaje.txt'

    with open(nombre_archivo, 'r') as f:
        for l in f.readlines():
            print(l, end='')

if __name__ == "__main__":
    main()





