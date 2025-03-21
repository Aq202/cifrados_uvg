import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


key = b'0123456789abcdef' # llave
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8080))
server.listen(1)
print(f"Listening on port 8080")

while True:
    conn, addr = server.accept()
    print(f"Connection from {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received: {data.hex()}")

        # Descifrar el mensaje AES CBC
        iv = data[:16]  # Extraer el IV
        mensaje_cifrado = data[16:]  # Extraer el mensaje cifrado

        # Descifrar el mensaje
        cipher = AES.new(key, AES.MODE_CBC, iv)
        mensaje_descifrado = unpad(cipher.decrypt(mensaje_cifrado), AES.block_size)


        print(f"Mensaje descifrado: {mensaje_descifrado.decode()}")
        
    conn.close()