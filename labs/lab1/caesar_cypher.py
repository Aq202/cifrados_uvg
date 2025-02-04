"""
Autor: Diego Morales Aquino
"""
def caesar_cypher(text, shift=3, alphabet="abcdefghijklmnñopqrstuvwxyz"):

    cypher_text = ""
    for char in text:
        
        lower_char = char.lower()
        if lower_char == " ":
            cypher_text += char
        elif lower_char in alphabet:
            # realizar corrimiento hacia la derecha
            index = (alphabet.index(lower_char) + shift) % len(alphabet)
            new_char = alphabet[index]
            cypher_text += new_char.upper() if char.isupper() else new_char # Mantener case

    return cypher_text

def caesar_decypher(text, shift=3, alphabet="abcdefghijklmnñopqrstuvwxyz"):

    decypher_text = ""
    for char in text:
        
        lower_char = char.lower()
        if lower_char == " ":
            decypher_text += char
        elif lower_char in alphabet:
            # realizar corrimiento hacia la derecha
            index = (alphabet.index(lower_char) - shift) % len(alphabet)
            new_char = alphabet[index]
            decypher_text += new_char.upper() if char.isupper() else new_char # Mantener case

    return decypher_text
if __name__ == "__main__":
    text = "Atacar al amanecer"
    cypher_text = caesar_cypher(text)
    print("Texto cifrado: ", cypher_text)
    print("Texto decifrado: ", caesar_decypher(cypher_text))
    