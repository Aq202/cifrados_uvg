"""
Autor: Diego Morales Aquino
"""
from base64_to_binary import base64_to_binary
from binary_to_ascii import binary_to_text

def base64_to_text(base64_str):

    binary_str = base64_to_binary(base64_str)
    print(binary_str)
    # Eliminar padding
    num_paddings = base64_str.count("=")
    if num_paddings > 0:
        binary_str = binary_str[0:-2*num_paddings]
    
    # Convertir cada byte a texto (ascii)
    text = ""
    for i in range(0, len(binary_str), 8):
        text += binary_to_text(binary_str[i: i + 8])

    return text

if __name__ == "__main__":
    base64_text = input("Ingresar cadena en base64: ")
    text_plain = base64_to_text(base64_text)
    print(text_plain)