def cifrar_cesar(texto, corrimiento):
    # Inicializamos el texto cifrado
    texto_cifrado = ""

    # Iteramos sobre cada carácter en el texto
    for char in texto:
        if char.isalpha():  # Solo ciframos letras
            # Determinamos el valor base (A para mayúsculas o a para minúsculas)
            base = ord('A') if char.isupper() else ord('a')

            # Aplicamos el corrimiento y ajustamos el valor para que se mantenga dentro del alfabeto
            nuevo_char = chr((ord(char) - base + corrimiento) % 26 + base)

            # Añadimos el carácter cifrado al texto cifrado
            texto_cifrado += nuevo_char
        else:
            # Si no es una letra, lo añadimos sin modificarlo
            texto_cifrado += char

    return texto_cifrado

# Ejemplo de uso aqui ahora
texto = input("Introduce el texto a cifrar: ")
corrimiento = int(input("Introduce el corrimiento: "))

texto_cifrado = cifrar_cesar(texto, corrimiento)
print("Texto cifrado:", texto_cifrado)

