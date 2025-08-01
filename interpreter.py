# interpreter.py

from data import lettersLower, lettersUpper, numbersRegular, numbersNegative, specialCharacters

def char_to_code(char):
    if char in lettersUpper:
        return lettersUpper[char]
    elif char in lettersLower:
        return lettersLower[char]
    elif char in numbersRegular:
        return numbersRegular[char]
    elif char in numbersNegative:
        return numbersNegative[char]
    elif char in specialCharacters:
        return specialCharacters[char]
    else:
        return "<UNK>"  # unknown char

def interpret_input(user_input):
    codes = []
    for ch in user_input:
        code = char_to_code(ch)
        codes.append(code)
    return codes

def main():
    print("Custom Word Interpreter")
    while True:
        user_text = input("Input text (or 'exit' to quit): ")
        print("Id Values{ # = letters, $ = numbers (Only support for 1 digit values like 1 or -2), @ = special characters}")
        if user_text.lower() == 'exit':
            print("Peace out ✌️")
            break

        codes = interpret_input(user_text)
        print("Codes:", codes)

if __name__ == "__main__":
    main()
