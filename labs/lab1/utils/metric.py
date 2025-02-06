"""
Autor: Diego Morales Aquino

Realizado con la ayuda del modelo GPT-3.5
Link de la conversación: https://chatgpt.com/share/67a410f8-5ad4-8009-b750-294ad5a847ba
"""
import numpy as np
from scipy.spatial.distance import jensenshannon
from utils.sp_frequencies import sp_frequencies

def normalize_distribution(dist):
    total = sum(dist.values())
    return {k: v / total for k, v in dist.items()}

def eval_distr(dist):
    """Calcula la distancia de Jensen-Shannon entre una distribución y la distribución teórica."""
    dist = normalize_distribution(dist)
    dist_theo = normalize_distribution(sp_frequencies)

    keys = set(dist.keys()).union(dist_theo.keys())
    p = np.array([dist.get(k, 0) for k in keys])
    q = np.array([dist_theo.get(k, 0) for k in keys])

    return jensenshannon(p, q)  # Distancia de JS (0 = idénticas, >0 = diferentes)

