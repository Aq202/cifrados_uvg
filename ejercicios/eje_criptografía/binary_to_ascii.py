"""
Autor: Diego Morales Aquino

Este código fue realizado con apoyo del modelo de IA ChatGPT 3

Link de la conversación:
https://chatgpt.com/share/679873c5-4e70-8009-a464-f913298554d0

"""


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

if __name__ == "__main__":

    binary_str = input("Ingresar cadena binaria: ")
    text = binary_to_text(binary_str)
    print(f"Texto resultante: {text}")

