import random
from datetime import datetime

mensajes = [
    "Señor, Tú eres digno de toda gloria y honra 🙌",
    "Gracias Dios por tu amor infinito.",
    "Eres mi refugio y mi fortaleza.",
    "Mi vida está en tus manos, Señor.",
    "Tu gracia es suficiente para mí.",
    "Gracias por nunca soltarme.",
    "Eres mi paz en medio de todo.",
    "Te alabo porque eres bueno todo el tiempo.",
    "Mi corazón te pertenece, Señor ❤️",
    "Confío en tus planes perfectos."    
    "Salmos 23:1 - El Señor es mi pastor; nada me faltará.",
    "Filipenses 4:13 - Todo lo puedo en Aquel que me fortalece.",
    "Jeremías 29:11 - Porque yo sé los planes que tengo para ustedes.",

]

def mostrar_menu():
    print("\n✨ Devocional 1Diario ✨")
    print("1. Leer un versiculo o mensaje inspirador")
    print("2. Escribir una oración")
    print("3. Salir")

def ver_mensaje():
    mensaje = random.choice(mensajes)
    print("\n🙏 Palabra para Dios:")
    print(mensaje)

def guardar_oracion():
    oracion = input("\nEscribe tu oración: ")

    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    with open("mi_diario_con_dios.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"\nFecha: {fecha}\n")
        archivo.write(f"Oración: {oracion}\n")
        archivo.write("-" * 30 + "\n")

    print("\n✅ Tu oración fue guardada en mi_diario_con_dios.txt")

while True:
    mostrar_menu()
    opcion = input("\nElige una opción: ")

    if opcion == "1":
        ver_mensaje()
    elif opcion == "2":
        guardar_oracion()
    elif opcion == "3":
        print("\nDios te bendiga 🙏✨")
        break
    else:
        print("\nOpción no válida. Intenta otra vez.")