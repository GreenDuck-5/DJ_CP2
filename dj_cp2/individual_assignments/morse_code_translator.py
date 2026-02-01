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

#morse to english
morse_to_english = {value: key for key, value in alphabet.items()}

#introduce the user
#ask how to translate - morse to english or english to morse
print("Welcome to the Morse Code Translator!")

def main():
    choice = input("Choose translation type:\n1 - English to Morse\n2 - Morse to English\nEnter 1 or 2: ")

#ask for the message if english
    while True:
        if choice == "1":
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

    #ask for message if morse

        elif choice == "2":
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

        else:
            print("Invalid choice. Try again.")
            continue

#ask user whether to quit or translate another message
        again = input("Translate another message? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            exit()

main()