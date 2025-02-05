"""
Autor: Diego Morales Aquino

Este código fue realizado con apoyo del modelo de IA ChatGPT 3

Link de la conversación:
https://chatgpt.com/share/67a18e05-8640-8009-be4a-241f8e105f73
"""
from clean_text import clean_text

def afines_cypher(text, a, b, alphabet="abcdefghijklmnñopqrstuvwxyz"):

    cypher_text = ""
    text = clean_text(text, alphabet)
    for char in text:
        
        # Aplicar cifrado ax +b (mod m)
        index = (a * alphabet.index(char) + b) % len(alphabet)
        new_char = alphabet[index]
        cypher_text += new_char

    return cypher_text

# Función para calcular el inverso de a módulo m
def mod_inverse(a, m):
    # Algoritmo extendido de Euclides
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception(f"No tiene inverso modular, {a} y {m} no son coprimos")
    return x % m

# Algoritmo extendido de Euclides para calcular el GCD y los coeficientes
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

# Función para descifrar el texto usando el cifrado afín
def afines_decypher(text, a, b, alphabet="abcdefghijklmnñopqrstuvwxyz"):
    m = len(alphabet)
    a_inv = mod_inverse(a, m)  # Calcula el inverso de a módulo m
    
    decypher_text = ""
    text = clean_text(text, alphabet)
    for char in text:
        index_y = alphabet.index(char)  # Índice del carácter cifrado
        # Aplica la fórmula para descifrar: a_inv * (y - b) mod m
        index_x = (a_inv * (index_y - b)) % m
        new_char = alphabet[index_x]
        decypher_text += new_char

    return decypher_text

if __name__ == "__main__":
    text = "Atacar al AMANECER"
    a = 2
    b = 8
    cypher_text = afines_cypher(text, a, b)
    print("Texto cifrado: ", cypher_text)
    print("Texto decifrado: ", afines_decypher(cypher_text, a, b))
    