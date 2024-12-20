# -*- coding: utf-8 -*-

# Diccionario para convertir números del 1 al 9 en superíndices python3 agregar_superindices.py
superindice_map = {
    '0': '⁰',
    '1': '¹',
    '2': '²',
    '3': '³',
    '4': '⁴',
    '5': '⁵',
    '6': '⁶',
    '7': '⁷',
    '8': '⁸',
    '9': '⁹'
}

def numero_a_superindice(numero):
    """Convierte un número entero a su representación en superíndices."""
    return ''.join(superindice_map[d] for d in str(numero))

def agregar_superindices(entrada, salida):
    """Agrega superíndices secuenciales al inicio de cada línea."""
    with open(entrada, 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    with open(salida, 'w', encoding='utf-8') as f:
        for i, linea in enumerate(lineas, start=1):
            # if i > 1000:
            #     break
            superindice = numero_a_superindice(i)
            f.write(f"{superindice} {linea}")

    print(f"El archivo ha sido procesado y guardado en '{salida}'.")

# Ejemplo de uso
entrada = 'entrada.txt'  # Cambia por el nombre de tu archivo de entrada
salida = 'salida.txt'    # Cambia por el nombre del archivo de salida
agregar_superindices(entrada, salida)
