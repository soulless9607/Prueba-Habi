# At the top of the file
EMPTY_BLOCK_MARKER = 'X'
BLOCK_SEPARATOR = ' '

from typing import Tuple, List, Union

def ordenar_bloques(number_sequence: Tuple[int, ...]) -> str:
    if not isinstance(number_sequence, tuple):
        raise TypeError("El Input debe ser una tupla")
    if not all(isinstance(x, int) for x in number_sequence):
        raise ValueError("Todos los elementos deben ser enteros")

    bloque_actual = []
    bloques_ordenados = []

    for numero in number_sequence:
        # Si el número es un cero, significa que hemos terminado un bloque.
        if numero == 0:
            # Ordenamos el bloque actual
            bloque_actual.sort()
            
            if not bloque_actual:
                bloques_ordenados.append(EMPTY_BLOCK_MARKER)
            else:
                # Convertimos cada número a string y los unimos
                bloques_ordenados.append("".join(map(str, bloque_actual)))
            
            # Reiniciamos el bloque actual para el próximo ciclo
            bloque_actual = []
        else:
            # Si el número no es cero, lo añadimos al bloque actual
            bloque_actual.append(numero)
    
    bloque_actual.sort()
    if not bloque_actual:
        bloques_ordenados.append(EMPTY_BLOCK_MARKER)
    else:
        bloques_ordenados.append("".join(map(str, bloque_actual)))

    return BLOCK_SEPARATOR.join(bloques_ordenados)

if __name__ == '__main__':
    test_cases = [
        (1,3,2,0,7,8,1,3,0,6,7,1),
        (2,1,0,0,3,4),
        (0,5,2,0,0,8,9,0)
    ]
    
    for test_case in test_cases:
        print(f"Input: {test_case}")
        print(f"Output: {ordenar_bloques(test_case)}\n")