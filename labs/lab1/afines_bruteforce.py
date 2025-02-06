import os
from utils.metric import eval_distr
from utils.get_text_probability_distr import get_text_probability_distr
from utils.sp_frequencies import sp_frequencies
from utils.clean_text import clean_text
from afines_cypher import extended_gcd, afines_decypher

def afines_bruteforce(text, text_to_find = None, alphabet="abcdefghijklmnñopqrstuvwxyz"):
   
    # Limpiar texto
    text = clean_text(text, alphabet)
    m = len(alphabet)

    results = []
    for a in range(1, 16):

        # Validar que a y m sean coprimos
        g, x, y = extended_gcd(a, m)
        if g != 1:
            continue

        for b in range(1, 16):
            decyphered_text = afines_decypher(text, a, b, alphabet)
            decypher_prob_distr = get_text_probability_distr(decyphered_text, alphabet)
            # calcular metrica
            metric = eval_distr(decypher_prob_distr)
            
            results.append((a, b, metric, decyphered_text))

    results = sorted(results, key=lambda x: x[2], reverse=True)
    return results

if __name__ == "__main__":
    current_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_path, "cypher_texts/afines.txt")
    
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
        results = afines_bruteforce(text)

        for result in results:
            a, b, metric, decyphered_text = result
            print(f"a: {a}, b: {b}, Métrica: {metric}, Texto descifrado: {decyphered_text}\n")
