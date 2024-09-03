from scapy.all import *
import time

def send_icmp_data(destination_ip, data, interval=0.1):
    packet_id = 12345  # ID fijo para todos los paquetes
    seq_number = 1  # Número de secuencia inicial

    for char in data:
        # Crear paquete ICMP con el carácter en el campo de datos
        packet = IP(dst=destination_ip)/ICMP(id=packet_id, seq=seq_number)/Raw(load=char)
        
        # Enviar el paquete
        send(packet, verbose=0)
        
        print(f"Sent 1 packets.")
        
        # Incrementar el número de secuencia para el siguiente paquete
        seq_number += 1
        packet_id += 1
        
        # Esperar antes de enviar el siguiente paquete para mantener el timestamp coherente
        time.sleep(interval)

# Ejemplo de uso
data = input("Introduce el texto cifrado:") # Datos a enviar

destination_ip = "192.168.31.188"  # IP de destino
  
send_icmp_data(destination_ip, data)