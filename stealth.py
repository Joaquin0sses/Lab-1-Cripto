from scapy.all import *
import time

# Función para enviar caracteres cifrados en paquetes ICMP
def enviar_datos_icmp(destino, texto_cifrado):
    for char in texto_cifrado:
        paquete = IP(dst=destino)/ICMP()/Raw(load=char)
        send(paquete)
        time.sleep(1)  # Espera para no enviar todos los paquetes demasiado rápido

# Mostrar un ping real previo al envío de datos
def ping_real(destino):
    ping_result = sr1(IP(dst=destino)/ICMP(), timeout=1)
    print("Ping real previo:")
    ping_result.show()

# Mostrar un ping real posterior al envío de datos
def ping_real_post(destino):
    ping_result = sr1(IP(dst=destino)/ICMP(), timeout=1)
    print("Ping real posterior:")
    ping_result.show()

# Ejemplo de uso
destino = "172.17.0.1"  # Puedes cambiar esto por la IP de destino
texto = input("Introduce el texto cifrado:")

# Cifrado del texto
texto_cifrado =texto
print(f"Texto cifrado: {texto_cifrado}")

# Ping real previo
ping_real(destino)

# Envío de datos cifrados en ICMP
enviar_datos_icmp(destino, texto_cifrado)

# Ping real posterior
ping_real_post(destino)
