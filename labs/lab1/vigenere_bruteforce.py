import os
from utils.metric import eval_distr
from utils.clean_text import clean_text
from itertools import product
from vigenere_cypher import vigenere_decypher
from utils.get_text_probability_distr import get_text_probability_distr
from tqdm import tqdm


def generate_keys(alphabet, size):
    return [''.join(c) for c in product(alphabet, repeat=size)]

def vigenere_bruteforce(text, key_start ="", key_max_len = 6, alphabet="abcdefghijklmnñopqrstuvwxyz"):
   
    # Limpiar texto
    text = clean_text(text, alphabet)

    # Validar key_start
    if len(key_start) > 0:
        key_start = key_start.lower()
        if not all(char in alphabet for char in key_start):
            raise Exception(f"La clave contiene chars que no están en el alfabeto")
    
    results = []
    # Iterar en los posibles tamaños de clave
    for key_len in range(1, key_max_len + 1):

        # Saltar inicio de clave que ya se tiene
        if key_len <= len(key_start):
            continue

        # Generar todas las posibles claves de tamaño key_len
        keys = generate_keys(alphabet, key_len - len(key_start))
        for key in tqdm(keys):
            complete_key = key_start + key

            # Descifrar texto y calcular probab
            decyphered_text = vigenere_decypher(text, complete_key, alphabet)
            decypher_prob_distr = get_text_probability_distr(decyphered_text, alphabet)

            # Evaluar métrica
            metric = eval_distr(decypher_prob_distr)
            results.append((complete_key, metric, decyphered_text))

        
    return sorted(results, key=lambda x: x[1], reverse=False)


            
if __name__ == "__main__":
    current_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_path, "cypher_texts/vigenere.txt")
    
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
        results = vigenere_bruteforce(text, key_start="pa")

        for result in results[0:20]:
            key, metric, decyphered_text = result
            print(f"Key: {key}, Métrica: {metric}, Texto descifrado: {decyphered_text}\n")
