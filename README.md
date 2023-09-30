# aarsla-FPCS.4

# TransCrypt

TransCrypt is a multilingual translator GUI application that translates texts between different languages such as Binary, Morse Code, ASCII, Hexadecimal, and Base64. It's implemented in Python and uses Tkinter for GUI. Moreover, TransCrypt includes a practice mode for translations and an image to text converter utilizing Tesseract OCR.

## Installation

To run TransCrypt, you need to have Python (version 3.6 or later) installed on your computer. Install the following packages with pip:

```sh
pip install pytesseract
pip install pillow
```

Please make sure that Tesseract-OCR is installed on your system. You can download it from here: https://github.com/UB-Mannheim/tesseract/wiki. After installing, specify the Tesseract path in the TransCrypt.py file as shown below:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```
Change the path according to your Tesseract installation.
(If you are using linux deleting this line will just work fine)

## Files

TransCrypt project consists of the following Python files:

1. `gui.py`: This is the main GUI file which contains all the GUI related code. It includes different pages for each feature of the application: the Translator page, the Practice Mode page, and the Image to Text page.

2. `TransCrypt.py`: This file contains the main logic of the application. It includes classes for translation (Translator), practice mode (PracticeMode), and image to text conversion (ImageToText).

3. `languages.py`: This file includes the definitions of the languages used in the application. Each language class includes methods to convert text to that language and vice versa.

## Usage

To run the application, execute `gui.py`:

```sh
python gui.py
```

### Translator

The translator is the main feature of the application. To use it, follow these steps:

1. Select the input and output languages from the drop-down menus.
2. Enter the text you want to translate in the input box.
3. The translated text will automatically appear in the output box.
4. If you want to translate in the other direction, click the 'Switch' button.
5. To translate a text file, click 'Select File To Translate' and choose a file. The content of the file will be automatically translated.
6. To save the output, click 'Save Output' and choose a location to save the file.

### Practice Mode

Practice mode allows you to practice translations. Here is how to use it:

1. Select the language you want to practice from the drop-down menu.
2. Enter the length of the source text.
3. Click 'New Text' to generate a random text. Try to translate it to the selected language.
4. Enter your translation in the input box and click 'Check' to check if it's correct.

### Image to Text

This feature allows you to convert text in images to plain text:

1. Click 'Open Image File' and select an image file. The text in the image will be extracted and displayed in the output box.
2. To save the output, click 'Save Output' and choose a location to save the file.
