"""
Autor: Diego Andrés Morales Aquino
"""

import random
import string
from ascii_to_binary import text_to_binary
from binary_to_ascii import binary_to_text
from xor import xor_binary_strings

def generate_dynamic_key(n):
    """
    Genera un texto aleatorio de longitud n compuesto por números y letras.
    """
    if n <= 0:
        raise ValueError("La longitud debe ser un entero positivo.")

    caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits
    texto_random = ''.join(random.choices(caracteres, k=n))
    return texto_random

def fixed_key_cypher(key, text):
    """
    Cifra un texto a partir de una llave, aplicándoles XOR.
    """
    complete_key = key
    text_bin = text_to_binary(text)

    if len(key) < len(text):
        # Repetir la llave hasta que sea del tamaño del texto
        i = 0
        while len(complete_key) < len(text):
            complete_key += key[i]
            i = i + 1 if i < len(key) - 1 else  0 # Seleccionar siguiente char de key
        
        complete_key_bin = text_to_binary(complete_key)
        
    elif len(key) != len(text):
        # Llenar con ceros el texto hasta que alcance tamaño de llave (en binario)
        complete_key_bin = text_to_binary(complete_key)
        text_bin = text_bin.zfill(len(complete_key_bin))

    cypher_bin = xor_binary_strings(text_bin, complete_key_bin)
    return binary_to_text(cypher_bin)

def dynamic_key_cypher(key_size, text):
    """
    Cifra un texto con una llave de tamaño key_size aleatoria.
    """
    key = generate_dynamic_key(key_size)
    return fixed_key_cypher(key, text), key


def decypher(key, text):
    """
    Descifra un texto mediante la llave original.
    """

    complete_key = key

    if len(key) < len(text):
        # Repetir la llave hasta que sea del tamaño del texto
        i = 0
        while len(complete_key) < len(text):
            complete_key += key[i]
            i = i + 1 if i < len(key) - 1 else  0 # Seleccionar siguiente char de key
        
    complete_key_bin = text_to_binary(complete_key)
    text_bin = text_to_binary(text)
    decypher_text_bin = xor_binary_strings(text_bin, complete_key_bin)
    return binary_to_text(decypher_text_bin)


if __name__ == "__main__":
    # Llave estática
    key = "hola"
    text = "Este es un mensaje cifrado!"
    cypher_result = fixed_key_cypher(key, text)
    print("Mensaje cifrado: ", cypher_result)
    print("Mensaje decifrado: ", decypher(key, cypher_result))

    # Llave dinámica
    cypher_result, key = dynamic_key_cypher(15, text)
    print("Mensaje cifrado: ", cypher_result)
    print("Mensaje decifrado: ", decypher(key, cypher_result))

