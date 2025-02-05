"""
Autor: Diego Morales Aquino
"""
from clean_text import clean_text

def vigenere_cypher(text, key, alphabet="abcdefghijklmnñopqrstuvwxyz"):

    key = clean_text(key, alphabet)
    text = clean_text(text, alphabet)

    N = len(key)
    M = len(alphabet)
    cypher_text = ""
    for i, char in enumerate(text):
        
        # Aplicar formula (xi + (ki)) mod M
        xi = alphabet.index(char)
        ki = alphabet.index(key[i % N])
        index = (xi + ki) % M

        new_char = alphabet[index] 
        cypher_text += new_char # Mantener case

    return cypher_text

def vigenere_decypher(text, key, alphabet="abcdefghijklmnñopqrstuvwxyz"):
    
    key = clean_text(key, alphabet)
    text = clean_text(text, alphabet)

    N = len(key)
    M = len(alphabet)
    decypher_text = ""
    for i, char in enumerate(text):
        
        # Aplicar formula (xi - (ki)) mod M
        xi = alphabet.index(char)
        ki = alphabet.index(key[i % N])
        index = (xi - ki) % M
        
        new_char = alphabet[index]
        decypher_text += new_char # Mantener case

    return decypher_text

if __name__ == "__main__":
    text = "WHAT A NICE DAY today"
    key = "cRypTO"
    cypher_text = vigenere_cypher(text, key)
    print("Texto cifrado: ", cypher_text)
    print("Texto decifrado: ", vigenere_decypher(cypher_text, key))
    