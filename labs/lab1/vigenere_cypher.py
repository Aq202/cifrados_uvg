"""
Autor: Diego Morales Aquino
"""
def vigenere_cypher(text, key, alphabet="abcdefghijklmnñopqrstuvwxyz"):

    key = key.lower()

    N = len(key)
    M = len(alphabet)
    cypher_text = ""
    for i, char in enumerate(text):
        
        lower_char = char.lower()
        if lower_char == " ":
            cypher_text += char
        elif lower_char in alphabet:
            # Aplicar formula (xi + (ki mod N)) mod M
            xi = alphabet.index(lower_char)
            ki = alphabet.index(key[i % N])
            index = (xi + (ki % N)) % M

            new_char = alphabet[index] 
            cypher_text += new_char.upper() if char.isupper() else new_char # Mantener case

    return cypher_text

def vigenere_decypher(text, key, alphabet="abcdefghijklmnñopqrstuvwxyz"):
    
    key = key.lower()

    N = len(key)
    M = len(alphabet)
    decypher_text = ""
    for i, char in enumerate(text):
        
        lower_char = char.lower()
        if lower_char == " ":
            decypher_text += char
        elif lower_char in alphabet:
            # Aplicar formula (xi - (ki mod N)) mod M
            xi = alphabet.index(lower_char)
            ki = alphabet.index(key[i % N])
            index = (xi - (ki % N)) % M
            
            new_char = alphabet[index]
            decypher_text += new_char.upper() if char.isupper() else new_char # Mantener case

    return decypher_text
if __name__ == "__main__":
    text = "WHAT A NICE DAY today"
    key = "cRypTO"
    cypher_text = vigenere_cypher(text, key)
    print("Texto cifrado: ", cypher_text)
    print("Texto decifrado: ", vigenere_decypher(cypher_text, key))
    