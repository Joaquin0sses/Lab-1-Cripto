from scapy.all import *
import time
import struct

def get_milliseconds_since_midnight():
    current_time = time.time()
    midnight = time.mktime(time.gmtime()) - time.timezone
    milliseconds_since_midnight = int((current_time - midnight) * 1000)
    return milliseconds_since_midnight

def send_icmp_data(destination_ip, data, interval=0.1):
    packet_id = 12345  # ID fijo para todos los paquetes
    seq_number = 1  # Número de secuencia inicial

    for char in data:
        # Obtener la hora actual en milisegundos desde la medianoche
        timestamp = get_milliseconds_since_midnight()
        
        # Crear los campos de timestamp en formato binario
        timestamp_data = struct.pack("!III", timestamp, 0, timestamp)
        
        # Crear paquete ICMP tipo 13 (Timestamp Request) con el carácter en el campo de datos
        packet = (IP(dst=destination_ip) /
                  ICMP(type=13, id=packet_id, seq=seq_number) /
                  Raw(load=timestamp_data + char.encode('latin1')))
        
        # Enviar el paquete
        send(packet, verbose=0)
        
        print(f"Sent 1 packet with seq {seq_number} and timestamp {timestamp}.")
        
        # Incrementar el número de secuencia para el siguiente paquete
        seq_number += 1
        packet_id += 1
        
        # Esperar antes de enviar el siguiente paquete para mantener el timestamp coherente
        time.sleep(interval)

# Ejemplo de uso
data = input("Introduce el texto cifrado:")  # Datos a enviar
destination_ip = "127.0.0.1"  # IP de destino
  
send_icmp_data(destination_ip, data)
