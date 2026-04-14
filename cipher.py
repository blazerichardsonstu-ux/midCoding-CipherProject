def shift_letter(letter, shift):
    if not letter.isalpha():
        return letter
    
    if letter.isupper():
        start = ord('A')
    else:
        start = ord('a')

    letter_position = ord(letter) - start
    new_position = (letter_position + shift) % 26

    return chr(start + new_position)


def encode_message(message, shift):
    encoded_message = ""

    for letter in message:
        encoded_message += shift_letter(letter, shift)

    return encoded_message
def decode_message(message, shift):
    return encode_message(message, -shift)


def ask_for_shift():
    try:
        return int(input("Enter the shift amount: "))
    except ValueError:
        print("Please enter a whole number for the shift.")
        return None


def encode_file(input_file, output_file, shift):
    try:
        with open(input_file, 'r') as input_handle:
            original_text = input_handle.read()
        encoded_text = encode_message(original_text, shift)
        with open(output_file, 'w') as output_handle:
            output_handle.write(encoded_text)

        print(f"File '{input_file}' was encoded and saved as '{output_file}'.")
    except FileNotFoundError:
        print(f"File '{input_file}' was not found.")
    except IOError as error:
        print(f"There was a problem while working with the file: {error}")


def decode_file(input_file, output_file, shift):
    try:
        with open(input_file, 'r') as input_handle:
            encoded_text = input_handle.read()
        decoded_text = decode_message(encoded_text, shift)
        with open(output_file, 'w') as output_handle:
            output_handle.write(decoded_text)

        print(f"File '{input_file}' was decoded and saved as '{output_file}'.")
    except FileNotFoundError:
        print(f"File '{input_file}' was not found.")
    except IOError as error:
        print(f"There was a problem working with the file: {error}")


def handle_message_choice(choice):
    if choice == 'decode':
        message = input("Enter a message to decode: ")
    else:
        message = input("Enter a message to encode: ")

    shift = ask_for_shift()
    if shift is None:
        return

    print(f"Original: {message}")

    if choice == 'decode':
        print(f"Decoded: {decode_message(message, shift)}")
    else:
        print(f"Encoded: {encode_message(message, shift)}")


def handle_file_choice(action):
    input_file = input("Enter the input file name: ").strip()
    output_file = input("Enter the output file name: ").strip()
    shift = ask_for_shift()

    if shift is None:
        return

    if action == 'encode':
        encode_file(input_file, output_file, shift)
    else:
        decode_file(input_file, output_file, shift)


def main():
    print("What would you like to do?")
    print("  1. encode a message")
    print("  2. decode a message")
    print("  3. encode a file")
    print("  4. decode a file")

    choice = input("Enter 1, 2, 3, or 4: ").strip()

    if choice == '1':
        handle_message_choice('encode')
    elif choice == '2':
        handle_message_choice('decode')
    elif choice == '3':
        handle_file_choice('encode')
    elif choice == '4':
        handle_file_choice('decode')
    else:
        print("Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main() 
    #bulldog
