import random
import string
import pytesseract
from pytesseract import image_to_string
from PIL import Image
from languages import Text, Binary, MorseCode, ASCII, Hexadecimal, Base64

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class Translator:
    """
    This class is used to translate messages between different languages
    like Binary, MorseCode, ASCII, Hexadecimal, and Base64.
    """
    def __init__(self):
        self.languages = {
            'Text': Text(),
            'Binary': Binary(),
            'Morse Code': MorseCode(),
            'ASCII': ASCII(),
            'Hexadecimal': Hexadecimal(),
            'Base64': Base64(),
        }

    def translate(self, input_text, input_lang, output_lang):
        if input_lang == 'Text':
            code = self.languages[output_lang].from_text(input_text)
        elif output_lang == 'Text':
            code = self.languages[input_lang].to_text(input_text)
        else:
            # Convert to text first, then to the output language
            text = self.languages[input_lang].to_text(input_text)
            code = self.languages[output_lang].from_text(text)
        return code


class PracticeMode:
    """
    This class is used to facilitate practicing translations between the different
    languages supported by the TransCrypt module.
    """
    def __init__(self):
        self.translator = Translator()
        self.languages = ['Binary', 'Morse Code', 'ASCII', 'Hexadecimal', 'Base64']

    def generate(self, length, target_language):
        self.text = ''.join(random.choices(string.ascii_lowercase + ' ', k=length))
        self.code = self.translator.translate(self.text, 'Text', target_language)
        return self.code

    def check(self, user_translation, target_language):
        correct_translation = self.translator.translate(self.code, target_language, 'Text')
        return user_translation.strip() == correct_translation, correct_translation


class ImageToText:
    def __init__(self):
        pass

    def to_string(self, image_path):
        try:
            img = Image.open(image_path)
            text = image_to_string(img)
            return text
        except Exception as e:
            print(f"An error occurred: {e}")
            return ""