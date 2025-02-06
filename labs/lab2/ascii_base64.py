"""
Autor: Diego Morales Aquino
"""
from binary_base64 import base64_to_binary, binary_to_base64
from ascii_binary import binary_to_text, text_to_binary

def base64_to_text(base64_str):

    binary_str = base64_to_binary(base64_str)
    
    # Convertir cada byte a texto (ascii)
    text = ""
    for i in range(0, len(binary_str), 8):
        text += binary_to_text(binary_str[i: i + 8])

    return text

def text_to_base64(text):
    
    text_bin = text_to_binary(text)
    text_base64 = binary_to_base64(text_bin)
    return text_base64