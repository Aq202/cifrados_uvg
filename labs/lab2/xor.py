"""
Autor: Diego Morales Aquino

Este código fue realizado con apoyo del modelo de IA ChatGPT 3

Link de la conversación:
https://chatgpt.com/share/67996c41-f2d8-8009-999e-4d0abc700a9f

"""
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
