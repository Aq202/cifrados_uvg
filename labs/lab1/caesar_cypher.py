"""
Autor: Diego Morales Aquino
"""
from clean_text import clean_text

def caesar_cypher(text, shift=3, alphabet="abcdefghijklmnñopqrstuvwxyz"):

    cypher_text = ""
    text = clean_text(text, alphabet)
    for char in text:
        
        # realizar corrimiento hacia la derecha
        index = (alphabet.index(char) + shift) % len(alphabet)
        new_char = alphabet[index]
        cypher_text += new_char

    return cypher_text

def caesar_decypher(text, shift=3, alphabet="abcdefghijklmnñopqrstuvwxyz"):

    decypher_text = ""
    text = clean_text(text, alphabet)
    for char in text:
        
        # realizar corrimiento hacia la derecha
        index = (alphabet.index(char) - shift) % len(alphabet)
        new_char = alphabet[index]
        decypher_text += new_char

    return decypher_text
if __name__ == "__main__":
    text = "Atacar al amanecer"
    cypher_text = caesar_cypher(text)
    print("Texto cifrado: ", cypher_text)
    print("Texto decifrado: ", caesar_decypher(cypher_text))
    