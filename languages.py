import base64

class Language:
    """
    Base class for all languages. All other language classes should inherit
    from this class and implement required methods.
    """
    def to_text(self, code):
        raise NotImplementedError

    def from_text(self, text):
        raise NotImplementedError


class Text(Language):
    """
    Represents plain text. It's the default language class used for
    direct text input and output.
    """
    def to_text(self, code):
        return code

    def from_text(self, text):
        return text

class Binary(Language):
    """
    Represents the binary language. This class is used to translate text
    to and from binary format.
    """
    def to_text(self, code):
        binary_chars = code.split(' ')
        text = ''.join(chr(int(binary, 2)) for binary in binary_chars)
        #
        return text

    def from_text(self, text):
        binary = ' '.join(format(ord(char), '08b') for char in text)
        return binary

class MorseCode(Language):
    """
    Represents the Morse code language. This class is used to translate
    text to and from Morse code format.
    """
    def __init__(self):
        self.char_to_morse = {
            'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
            'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
            'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
            's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
            'y': '-.--', 'z': '--..', 
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', 
            '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', 
            ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', 
            '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
        }
        self.morse_to_char = {v: k for k, v in self.char_to_morse.items()}

    def to_text(self, code):
        morse_chars = code.split(' ')
        text = ''.join(self.morse_to_char.get(morse, ' ') for morse in morse_chars)
        return text

    def from_text(self, text):
        text = text.lower()  # Morse code doesn't distinguish between upper and lower case
        morse = ' '.join(self.char_to_morse.get(char, '/') for char in text)
        return morse
        
class ASCII(Language):
    """
    Represents ASCII language. This class is used to translate text
    to and from ASCII format.
    """
    def to_text(self, code):
        ascii_chars = code.split(' ')
        text = ''.join(chr(int(ascii)) for ascii in ascii_chars)
        return text

    def from_text(self, text):
        ascii = ' '.join(str(ord(char)) for char in text)
        return ascii


class Hexadecimal(Language):
    """
    Represents the hexadecimal language. This class is used to translate
    text to and from hexadecimal format.
    """
    def to_text(self, code):
        hex_chars = code.split(' ')
        text = ''.join(chr(int(hex, 16)) for hex in hex_chars)
        return text

    def from_text(self, text):
        hexa = ' '.join(hex(ord(char))[2:] for char in text)
        return hexa


class Base64(Language):
    """
    Represents the Base64 language. This class is used to translate text
    to and from Base64 format.
    """
    def to_text(self, code):
        return base64.b64decode(code).decode('utf-8')

    def from_text(self, text):
        return base64.b64encode(text.encode('utf-8')).decode('utf-8')




