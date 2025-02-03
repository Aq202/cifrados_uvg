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
            cypher_text += alphabet[index]

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
            decypher_text += alphabet[index]

    return decypher_text
if __name__ == "__main__":
    text = "ATACAR AL AMANECER"
    cypher_text = caesar_cypher(text)
    print("Texto cifrado: ", cypher_text)
    print("Texto decifrado: ", caesar_decypher(cypher_text))
    