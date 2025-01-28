"""
Autor: Diego Morales Aquino

Este código fue realizado con apoyo del modelo de IA ChatGPT O4

Link de la conversación:
https://chatgpt.com/share/67986815-0098-8009-8080-3a6374653a88

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

# Ejemplo de uso
if __name__ == "__main__":
    text = input("Ingresar un texto a transformar a binario: ")
    print(f"Texto: {text}")
    print(f"Binario: {text_to_binary(text)}")
