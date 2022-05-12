def main():
    #Adicionar/agregar contenido a un archivo de texto plano:
    print('Adicionar /agregar contenido a un archivo de texto plano:')

    nombre_archivo = 'paises.txt'

    with open(nombre_archivo, 'a+', encoding='utf-8') as f: 
        f.write('\n')
        f.write('Egipto')
        f.write('\n')
        f.write('Japon')
        f.write('\n')
        f.write('Bolivia')

    print('El programa ha finalizado.')


if __name__ == "__main__":
    main()