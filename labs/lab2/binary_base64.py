"""
Autor: Diego Morales Aquino

Este código fue realizado con apoyo del modelo de IA ChatGPT 3

Link de la conversación:
https://chatgpt.com/share/679873c5-4e70-8009-a464-f913298554d0
https://chatgpt.com/share/67986f47-f18c-8009-b959-c4eba887a336

"""

from ascii_binary import binary_to_decimal
from ascii_binary import decimal_to_binary

def binary_to_base64(bin_str):
    """
    Convierte una cadena binaria a un texto en base 64.
    """
    # Tabla de caracteres Base64
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    # Rellenar para que longitud sea un múltiplo de 6
    zeros_added = 0
    while len(bin_str) % 6 != 0:
        bin_str = bin_str + '0'
        zeros_added += 1
    
    # Dividir la cadena binaria en bloques de 6 bits
    base64_result = ""
    for i in range(0, len(bin_str), 6):
        block = bin_str[i:i+6]  # Cada bloque de 6 bits
        decimal_value = binary_to_decimal(block)
        base64_result += base64_chars[decimal_value]  # Obtener char correspondiente

    return base64_result + '=' * int(zeros_added / 2)

def base64_to_binary(base64_str):
    # El conjunto de caracteres Base64
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    binary_result = ""
    
    for char in base64_str:

        if char == "=":
            # Ignorar padding
            continue

        # Validar que el char exista en representación base64
        index = base64_chars.find(char)
        
        if index == -1:
            raise ValueError(f"Carácter no válido encontrado en la cadena: {char}")
        
        # Convertimos el índice a una representación binaria de 6 bits
        binary_chunk = decimal_to_binary(index).zfill(6)
        
        # Añadimos el fragmento binario al resultado final
        binary_result += binary_chunk
    
    # Eliminar padding
    num_paddings = base64_str.count("=")
    if num_paddings > 0:
        binary_result = binary_result[0:-2*num_paddings]

    return binary_result