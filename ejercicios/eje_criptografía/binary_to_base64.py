"""
Autor: Diego Morales Aquino

Este código fue realizado con apoyo del modelo de IA ChatGPT 3

Link de la conversación:
https://chatgpt.com/share/679873c5-4e70-8009-a464-f913298554d0

"""

from binary_to_ascii import binary_to_decimal

def binary_to_base64(bin_str):
    """
    Convierte una cadena binaria a un texto en base 64 sin usar librerías de base64.
    """
    # Tabla de caracteres Base64
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    # Rellenar para que longitud sea un múltiplo de 6 (rellenar con ceros si es necesario)
    while len(bin_str) % 6 != 0:
        bin_str = '0' + bin_str
    
    # Dividir la cadena binaria en bloques de 6 bits
    base64_result = ""
    for i in range(0, len(bin_str), 6):
        block = bin_str[i:i+6]  # Cada bloque de 6 bits
        decimal_value = binary_to_decimal(block)
        base64_result += base64_chars[decimal_value]  # Obtener char correspondiente

    return base64_result

if __name__ == "__main__":
    binary_text = input("Ingresar cadena binaria a convertir a base64: ")
    base64 = binary_to_base64(binary_text)
    print("Base 64:", base64)
