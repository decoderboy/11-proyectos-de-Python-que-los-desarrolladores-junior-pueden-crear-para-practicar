import random
import os
import os.path
from lyrics_extractor import SongLyrics


def par_impar():
    numero = int(input("Ingresa un número: "))
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")


def mad_libs():
    adjetivo = str(input("Adjetivo: "))
    verbo = str(input("Verbo (-ANDO/IENDO): "))
    sustantivo = str(input("Sustantivo: "))
    sustantivo_plural = str(input("Sustantivo (Plural): "))
    exclamacion = str(input("Exclamacion: "))
    adjetivo_dos = str(input("Adjetivo: "))
    adverbio = str(input("Adverbio: "))
    verbo = str(input("Verbo: "))
    parte_del_cuerpo = str(input("Parte del cuerpo: "))
    color = str(input("Color: "))
    numero = int(input("Numero: "))
    color_plural = str(input("Color (plural): "))
    comida = str(input("Comida: "))
    adjetivo_tres = str(input("Adjetivo: "))
    print(
        '--------------------------------------------------------------------'
        f'Un dia {adjetivo} de primavera, estaba {verbo} en mi\njardin y plant'
        f'aba muchas semillas de {sustantivo} y de verduras en la\ntierra. Me '
        'estiro para agarrar mas semillas y me daba cuenta de que eran\ndorad'
        f'as y tenian la forma de {sustantivo_plural} "{exclamacion}!" yo\n'
        'grite. Estas semillas deben ser magicas. Las sembre en un rincon\n'
        f'{adjetivo_dos} de mi jardin. No podia esperar a ver como crecerian.'
        f'\nEl proximo dia, yo fui {adverbio} para {verbo} mis plantas. No me'
        f' lo podia creer lo que veia mi {parte_del_cuerpo}! Las semillas\n'
        f'magicas han brotado en una planta gigante y {color} Tenia\n{numero}'
        f' flores {color_plural} que olian como {comida}.\nPodia oir musica '
        f'{adjetivo_tres} que venia de las hojas. Justo cuando\nestuve a punto'
        'de tocar la planta, me desperte. ¡Todo ha sido un sueño!.'
        '--------------------------------------------------------------------')


def contador_palabras():
    oracion = str(input("¿En qué estás pensando?\nEntrada: "))
    print("Salida: ¡Muy bien, tu me has mostrado tu pensamiento en "+str(
        len(oracion.split()))+" palabras!")


def biografia():
    nombre = str(input("- Nombre: "))
    fecha = str(input("- Fecha de nacimiento: "))
    direccion = str(input("- Dirección: "))
    metas = str(input("- Metas personales: "))
    print("")


def acronimo():
    string = str(input("Entrada -> "))
    words = string.split(' ')
    character = ''
    for word in words:
        character += word[0]
    print("Salida: "+str(character))


def piedra_papel_tijera_lagarto_spock():
    game = {1: 'piedra', 2: 'papel', 3: 'tijeras', 4: 'lagarto', 5: 'spock'}
    resultado = {
        ('piedra', 'papel'): False,
        ('piedra', 'tijeras'): True,
        ('papel', 'piedra'): True,
        ('papel', 'tijeras'): False,
        ('tijeras', 'piedra'): False,
        ('tijeras', 'papel'): True,
        ('piedra', 'lagarto'): True,
        ('lagarto', 'piedra'): False,
        ('lagarto', 'spock'): True,
        ('spock', 'lagarto'): False,
        ('spock', 'tijeras'): True,
        ('tijeras', 'spock'): False,
        ('tijeras', 'lagarto'): True,
        ('lagarto', 'tijeras'): False,
        ('lagarto', 'papel'): True,
        ('papel', 'lagarto'): False,
        ('papel', 'spock'): True,
        ('spock', 'papel'): False,
        ('spock', 'piedra'): True,
        ('piedra', 'spock'): False
    }
    status = {'player': 0, 'pc': 0}
    partida = 1
    jugadas = 0
    while partida != 0:
        pc = random.randint(1, 5)
        for key, value in game.items():
            print(key, value)

        player = int(input("Ingresa una opcion: "))
        print("_____________________________________")
        if game[player] == game[pc]:
            print("Computer Choise: ", game[pc], "\nPlayer Choise:", game[
                player])
            print("---> Tie <---")
        elif(resultado[(game[player], game[pc])]):
            print("Computer Choise: ", game[pc], "\nPlayer Choise:", game[
                player])
            print("---> Win <---")
            status['player'] += 1
        else:
            print("Computer Choise: ", game[pc], "\nPlayer Choise:", game[
                player])
            print("---> Lose <---")
            status['pc'] += 1
        print("_____________________________________")
        jugadas += 1
        if jugadas >= 2:
            if status['player'] >= 2:
                partida = 0
                print("Player es el ganador!")
                print("_____________________________________")
            elif status['pc'] > status['player']:
                partida = 0
                print("Computer es el ganador!")
                print("_____________________________________")
            else:
                print("_____________________________________")
    print("")


def adivina_el_numero_oculto():
    number = random.randrange(1, 50)
    guess = int(input("Guess a number between 1 and 50: "))
    while guess != number:
        if guess < number:
            print("You need to guess higher. Try again")
            guess = int(input("\nGuess a number between 1 and 50: "))
        else:
            print("You need to guess lower. Try again")
            guess = int(input("\nGuess a number between 1 and 50: "))
    print("You guessed the number correctly!\n")


def palindromo():
    characterlist = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""]
    for t in range(0, 5):
        texto = input("Ingresa la palabra a evaluar:")
        if len(texto.split()) == 0:
            if (texto == texto[::-1]):
                print("-> Es palindromo")
            else:
                print("-> No es palindromo")
        else:
            for c in characterlist:
                if str(c) in texto:
                    texto = texto.replace(str(c), "")
            if (texto == texto[::-1]):
                print("-> Es palindromo")
            else:
                print("-> No es palindromo")


def calculador_de_propinas():
    print("Mensaje inicial: ¿Cuál es la factura total de hoy, por favor?")
    m = float(input("Entrada: "))
    a = f"Salida: La propina aplicando el 18% is ${m * 0.18}, que contabiliza"
    "un total de $"
    m = m * 1.18
    print(a, round(m, 2))


def extractor_de_informacion_del_correo_electronico():
    email = str(input("Entrada: ").strip())
    user = email[:email.index("@")]
    domain = email[email.index("@")+1:]
    print(
        f'Salida: Hola {user}, estoy viendo que tu email está registrado con'
        f'{domain}. ¡Eso es genial!.')


def generador_de_letras():
    apikey = "AIzaSyCNp8sTJqu_Fe1d4NDNFwjBGAynmr05UOM"
    id_de_buscador = "2c93e09249739e7c0"
    extract_lyrics = SongLyrics(apikey, id_de_buscador)
    song = str(input("Ingresa el nombre de la cancion: "))
    lyrics = extract_lyrics.get_lyrics(song)
    name = lyrics['title']
    name = str(name) + '.txt'
    directorio = "LETRAS"
    try:
        os.stat(directorio)
    except:
        os.mkdir(directorio)
    directorio = r"LETRAS\\"+str(name)
    archivo = open(directorio, 'w')
    archivo.write(lyrics['lyrics'])
    archivo.close()
    print(lyrics['title'])
    print(lyrics['lyrics'])
    print("")


def main():
    x = 1
    while x != 0:
        print(
            "\n--- MENU DE OPCIONES ---\n[1]  Par o impar\n[2]  Mad Libs\n[3]"
            "  Contador de palabras\n[4]  Información de la Biografía\n[5]  ¿C"
            "ual es el acrónimo?\n[6]  Piedra, Papel, Tijera, Lagarto, Spock\n"
            "[7]  Adivina el número oculto\n[8]  ¿Es palindromo?\n[9]  Calcula"
            "dor de propinas\n[10] Extractor de información del correo electro"
            "nico\n[11] Generador de letras")
        opcion = str(input("--> "))
        if opcion == "1":
            par_impar()
        elif opcion == "2":
            mad_libs()
        elif opcion == "3":
            contador_palabras()
        elif opcion == "4":
            biografia()
        elif opcion == "5":
            acronimo()
        elif opcion == "6":
            piedra_papel_tijera_lagarto_spock()
        elif opcion == "7":
            adivina_el_numero_oculto()
        elif opcion == "8":
            palindromo()
        elif opcion == "9":
            calculador_de_propinas()
        elif opcion == "10":
            extractor_de_informacion_del_correo_electronico()
        elif opcion == "11":
            generador_de_letras()
        elif opcion == "0":
            x = 0
        else:
            print("Error!, ingresa una opcion valida!\n")

if __name__ == "__main__":
    main()

'# Author: Ivan Reyes'
