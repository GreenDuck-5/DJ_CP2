#DJ, 1st, Simple Morse Code Translator

#dictionary with the alphabet to the morse code translation

alphabet = {
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--..",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"-----"
}
morse_to_english = {value: key for key, value in alphabet.items()}

def morse_to_english_func(morse_to_english):
    message = input("Enter Morse code (use / between words): ")
    translated = []

    #loop through message and translate each letter

    words = message.split(" / ")
    for word in words:
        letters = word.split()
        for letter in letters:
            if letter in morse_to_english:
                translated.append(morse_to_english[letter])
        translated.append(" ")

    #print message

    print("English:")
    print("".join(translated).strip())

def english_to_morse():
    message = input("Enter an English message: ").lower()
    translated = []

    #loop through message and translate each letter
    for char in message:
        if char == " ":
            translated.append("/")
        elif char in alphabet:
            translated.append(alphabet[char])

    #print message

    print("Morse Code:")
    print(" ".join(translated))

#introduce the user
#ask how to translate - morse to english or english to morse
print("Welcome to the Morse Code Translator!")

def main():
    choice = input("Choose translation type:\n1 - English to Morse\n2 - Morse to English\n3 - Exit\nEnter 1 or 2 or 3: ")

    while True:
        if choice == "1":
            english_to_morse()

        elif choice == "2":
            morse_to_english_func(morse_to_english)

        elif choice == "3":
            print("Goodbye!")
            exit()

        else:
            print("Invalid choice. Try again.")
            continue

#ask user whether to quit or translate another message
        again = input("Translate another message? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            exit()
        main()

main()