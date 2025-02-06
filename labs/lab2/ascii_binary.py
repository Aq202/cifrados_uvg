"""
Autor: Diego Morales Aquino

Este código fue realizado con apoyo del modelo de IA ChatGPT O4

Link de la conversación:
https://chatgpt.com/share/67986815-0098-8009-8080-3a6374653a88
https://chatgpt.com/share/679873c5-4e70-8009-a464-f913298554d0

"""

def decimal_to_binary(decimal_number):
    """
    Convierte un número decimal en su representación binaria utilizando un proceso paso a paso.

    Args:
        decimal_number (int): Número decimal a convertir.

    Returns:
        str: Representación binaria del número decimal.
    """
    binary_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number //= 2
    return binary_number if binary_number else "0"

def text_to_binary(text):
    """
    Convierte un texto en su representación binaria concatenada.

    Args:
        text (str): Texto a convertir.

    Returns:
        str: Representación binaria concatenada del texto.
    """
    binary_result = ""
    for char in text:
        ascii_value = ord(char)  # Obtener el valor ASCII del carácter
        binary_value = decimal_to_binary(ascii_value)  # Convertir a binario
        binary_result += binary_value.zfill(8)  # Asegurar 8 bits por carácter
    return binary_result

def binary_to_decimal(bin_str):
    """
    Convierte una cadena binaria a un número decimal.
    """
    decimal = 0
    for i in range(len(bin_str)):
        if bin_str[-(i+1)] == '1':  # Tomar cada bit, desde el último (derecha)
            decimal += 2**i
    return decimal

def binary_to_text(bin_str):
    """
    Convierte cadena binaria a su representación en texto mediante código ascii
    """
    text_result = ""
    
    # Asegurar que la longitud de la cadena binaria sea un múltiplo de 8
    while len(bin_str) % 8 != 0:
        bin_str = '0' + bin_str  # Rellenars con ceros

    # Dividir la cadena binaria en bloques de 8 bits
    for i in range(0, len(bin_str), 8):
        block = bin_str[i:i+8]
        decimal_value = binary_to_decimal(block)
        text_result += chr(decimal_value)

    return text_result
