import csv

def read_file_to_dict(filename):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    bufferd = dict()
    
    try:
        with open(filename, mode='r') as file:
            csv_reader = csv.reader(file,delimiter=";")

            for row in csv_reader:

                for i in row:
                    if (i == ''):
                        continue
                    buffer = i.split(':')

                    if (buffer[0] in bufferd):
                        bufferd[buffer[0]].append(float(buffer[1]))
                    else:
                        bufferd[buffer[0]] = [float(buffer[1])]
        return bufferd
        
    except FileNotFoundError:
        raise FileNotFoundError


def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    for i in data:
        print(f'{i}: ventas totales ${sum(data[i])}0, promedio ${sum(data[i])/len(data[i])}0')
