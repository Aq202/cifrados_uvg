import os
from utils.metric import eval_distr
from caesar_cypher import caesar_decypher
from utils.get_text_probability_distr import get_text_probability_distr
from utils.sp_frequencies import sp_frequencies
from utils.clean_text import clean_text

def caesar_bruteforce(text, alphabet="abcdefghijklmnñopqrstuvwxyz"):
    """Descifra un texto cifrado con el cifrado César con un desplazamiento dado."""
    
    # Limpiar texto
    text = clean_text(text, alphabet)

    
    results = []
    # Ir probando que cada letra sea la más probable en español
    for shift in range(len(alphabet)):
        decyphered_text = caesar_decypher(text, shift, alphabet)
        decypher_prob_distr = get_text_probability_distr(decyphered_text, alphabet)
        # calcular metrica
        metric = eval_distr(decypher_prob_distr)
        
        results.append((shift, metric, decyphered_text))

    return sorted(results, key=lambda x: x[1], reverse=False)

if __name__ == "__main__":
    current_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_path, "cypher_texts/ceasar.txt")
    
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
        results = caesar_bruteforce(text)
        for shift, metric, decyphered_text in results:
            print(f"Shift: {shift}, Métrica: {metric}, Texto descifrado: {decyphered_text}\n")
