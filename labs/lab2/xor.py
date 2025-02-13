"""
Autor: Diego Morales Aquino

Este código fue realizado con apoyo del modelo de IA ChatGPT 3

Link de la conversación:
https://chatgpt.com/share/67996c41-f2d8-8009-999e-4d0abc700a9f

"""
from ascii_binary import text_to_binary

def xor_binary_strings(bin1, bin2):
    # Ambas cadenas con la misma long
    max_length = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_length)
    bin2 = bin2.zfill(max_length)

    # Realizar la operación XOR bit a bit
    xor_result = []
    for b1, b2 in zip(bin1, bin2):
        if b1 == '1' and b2 == '0' or b1 == '0' and b2 == '1':
            xor_result.append('1')
        else:
            xor_result.append('0')

    # Convertir a string
    return ''.join(xor_result)

def xor_ascii_strings(text1, text2):
    """
    Realiza la operación XOR entre dos strings de texto ASCII.
    Convierte cada texto a binario y realiza la operación XOR bit a bit.
    @return: El resultado de la operación XOR en binario.
    """
    # Convertir texto a binario
    bin_text1 = text_to_binary(text1)
    bin_text2 = text_to_binary(text2)
    return xor_binary_strings(bin_text1, bin_text2)