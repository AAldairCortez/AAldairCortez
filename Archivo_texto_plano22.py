def main():
    #Creacion de un archivo de texto plano:

    nombre_archivo = 'paises.txt'

    with open(nombre_archivo, 'w', encoding='utf-8') as f: 
        f.write('Colombia')
        f.write('\n')
        f.write('Ecuador')
        f.write('\n')
        f.write('Argentina')
        f.write('\n')
        f.write('Alemania')
        f.write('\n')
        f.write('Peru')
        f.write('\n')
        f.write('Italia')
        f.write('\n')
        f.write('Rusia')
        f.write('\n')


if __name__ =="__main__":
    main()

    