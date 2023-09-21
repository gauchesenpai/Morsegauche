MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += char
    return morse_code

def morse_to_text(morse_code):
    reverse_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        if code in reverse_dict:
            text += reverse_dict[code]
        else:
            text += code
    return text

def main():
    print("Morse Script - Desenvolvido por Gauche-Senpai")
    print("Selecione o que deseja fazer:")
    print("1. Texto para Código Morse")
    print("2. Código Morse para Texto")
    choice = input("Digite o número da opção: ")

    if choice == '1':
        text = input("Digite o texto para converter em Código Morse: ")
        morse_code = text_to_morse(text)
        print("Código Morse:", morse_code)
    elif choice == '2':
        morse_code = input("Digite o Código Morse para converter em texto: ")
        text = morse_to_text(morse_code)
        print("Texto:", text)
        with open('morse_traduzido.txt', 'w') as f:
            f.write(text)
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
