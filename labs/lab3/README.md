# Laboratorio #3
Diego Andrés Morales Aquino <br>
21762

## 📦 Dependencias Principales

Las principales dependencias del proyecto incluyen:

- Matplotlib
- Numpy
- PIL
- PyCryptodome
- tracemalloc
- sockets

## 🚀 Instalación y Ejecución

1. Clona este repositorio e instala las dependencias:

    ```bash
    git clone https://github.com/Aq202/cifrados_uvg.git
    cd cifrados_uvg/labs/lab3
    ```
2. Ejecuta el notebook IPYNB siguiendo el orden de las celdas.


## Parte 1: Rompiendo ECB en Imágenes: 
Compara el cifrado AES en modo ECB y CBC con imágenes, analizando los patrones y su seguridad.

Las imágenes tux.ppm y snoopy.ppm se deben encontrar en el mismo directorio del notebook. 

[Solución completa](lab3.ipynb)

## Parte 2: Capturando Cifrado en Red con Wireshark
Envia mensajes cifrados con AES-CBC y analiza el tráfico con Wireshark para evaluar su seguridad.

Los scripts de cliente y servidor deben ejecutarse en equipos distintos. Asegurarse que las reglas de entrada y salida del firewall habiliten el tráfico de paquetes en el puerto 8080.

[Respuestas a preguntas y análisis](lab3.ipynb)<br>
[Cliente de socket](parte2/socket_client.py)<br>
[Servidor de socket](parte2/socket_server.py)<br>
[Captura de datos de wireshark](parte2/captura-wireshark.pcap)<br>

## Parte 3: Implementando ChaCha20: 
Implementa el cifrado ChaCha20 y compara su rendimiento con AES.

Únicamente es necesario ejecutar la sección correspondiente en el notebook siguiendo el orden de las celdas.

[Solución completa](lab3.ipynb)

## Parte 4: Simulación de un Ransomware
Simula un ataque de ransomware usando cifrado AES y reflexiona sobre medidas de seguridad y manejo de claves.

Al ejecutar los scripts llevan a cabo la tarea de cifrar/descifrar todo el contenido de la carpeta en la que se encuentran.

[Respuestas a pregunta y análisis](lab3.ipynb)<br>
[Script para cifrar](parte4/cypher_randsomware.py)<br>
[Script para descifrar](parte4/decypher_randsomware.py)<br>