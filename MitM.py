from scapy.all import rdpcap, ICMP, Raw
from termcolor import colored
from langdetect import detect
import re

def extract_icmp_data(pcap_file):
    packets = rdpcap(pcap_file)
    data = ''

    for packet in packets:
        if ICMP in packet and packet[ICMP].type == 8:  # ICMP Echo Request
            if packet.haslayer(Raw):
                data += packet[Raw].load.decode('latin1')  # Decodificar cada byte

    return data

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ''

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char

    return decrypted_text

def es_espanol(decrypted_text):
    try:
        return detect(decrypted_text) == 'es'
    except:
        return False

def brute_force_caesar(text):
    probable_message = None
    for shift in range(26):
        decrypted_text = caesar_cipher_decrypt(text, shift)
        if es_espanol(decrypted_text):
            probable_message = decrypted_text
            print(colored(f"Shift {shift}: {decrypted_text}", 'green'))
        else:
            print(f"Shift {shift}: {decrypted_text}")

    return probable_message

# Ejemplo de uso
pcap_file = 'Trafico de paquetes ICMP.pcapng'  # Reemplaza con el nombre de tu archivo .pcapng
icmp_data = extract_icmp_data(pcap_file)
print(f"ICMP datos extraidos: {icmp_data}")

print("\nIntentando descifrar el cifrado César por fuerza bruta:")
brute_force_caesar(icmp_data)
