# Laboratorio #3
Diego Andrés Morales Aquino <br>
21762

## Parte 1: Rompiendo ECB en Imágenes: 
Compara el cifrado AES en modo ECB y CBC con imágenes, analizando los patrones y su seguridad.

[Solución completa](lab3.ipynb)

## Parte 2: Capturando Cifrado en Red con Wireshark
Envia mensajes cifrados con AES-CBC y analiza el tráfico con Wireshark para evaluar su seguridad.

[Respuestas a preguntas y análisis](lab3.ipynb)<br>
[Cliente de socket](parte2/socket_client.py)<br>
[Servidor de socket](parte2/socket_server.py)<br>
[Captura de datos de wireshark](parte2/captura-wireshark.pcap)<br>

## Parte 3: Implementando ChaCha20: 
Implementa el cifrado ChaCha20 y compara su rendimiento con AES.

[Solución completa](lab3.ipynb)

## Parte 4: Simulación de un Ransomware
Simula un ataque de ransomware usando cifrado AES y reflexiona sobre medidas de seguridad y manejo de claves.

Al ejecutar los scripts llevan a cabo la tarea de cifrar/descifrar todo el contenido de la carpeta en la que se encuentran.

[Respuestas a pregunta y análisis](lab3.ipynb)<br>
[Script para cifrar](parte4/cypher_randsomware.py)<br>
[Script para descifrar](parte4/decypher_randsomware.py)<br>