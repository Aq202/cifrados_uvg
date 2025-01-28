"""
Autor: Diego Morales Aquino

Este código fue realizado con apoyo del modelo de IA ChatGPT 3

Link de la conversación:
https://chatgpt.com/share/67986f47-f18c-8009-b959-c4eba887a336

"""

from ascii_to_binary import decimal_to_binary

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

if __name__ == "__main__":
    base64_text = input("Ingresar texto base64 a convertir a binario: ")
    binary_representation = base64_to_binary(base64_text)
    print("Binario: ",binary_representation)
