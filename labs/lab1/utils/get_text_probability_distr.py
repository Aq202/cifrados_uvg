def get_text_probability_distr(text, alphabet="abcdefghijklmnñopqrstuvwxyz"):
    text = text.lower()

    # Contar frecuencia de cada letra en el texto
    probability = {}
    for letter in alphabet:
        probability[letter] = text.count(letter)

    # Calcular probabilidad
    total = sum(probability.values())
    for letter in probability:
        probability[letter] /= total
    return probability