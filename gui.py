import random
import string
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from TransCrypt import Translator, PracticeMode, ImageToText
from tkinter import messagebox

class TranslatorPage(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        for i in range(3):
            self.columnconfigure(i, weight=1)
        self.rowconfigure(1, weight=1)
        # Create instances of Text, Binary, MorseCode, ASCII, Hexadecimal, Base64
        self.languages = ['Text', 'Binary', 'Morse Code', 'ASCII', 'Hexadecimal', 'Base64']
        self.translator = Translator()

        # Create the drop-down menus for language selection
        self.input_lang = tk.StringVar()
        self.output_lang = tk.StringVar()
        self.input_menu = ttk.Combobox(self, textvariable=self.input_lang, values=self.languages)
        self.output_menu = ttk.Combobox(self, textvariable=self.output_lang, values=self.languages)
        self.input_menu.current(0)  # default value
        self.output_menu.current(1)  # default value

        # Create the text boxes for input and output
        self.input_box = tk.Text(self, height=10, width=50)
        self.output_box = tk.Text(self, height=10, width=50)
        self.output_box['state'] = tk.DISABLED  # Initialize as disabled

        self.input_box.bind('<KeyRelease>', self.handle_input)
        self.input_menu.bind('<<ComboboxSelected>>', self.translate)
        self.output_menu.bind('<<ComboboxSelected>>', self.translate)

        # Create the 'Switch' button
        switch_button = tk.Button(self, text="Switch", command=self.switch)

        # Grid layout
        self.input_menu.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')
        switch_button.grid(row=0, column=1, sticky='nsew')
        self.output_menu.grid(row=0, column=2, padx=10, pady=5, sticky='nsew')

        self.input_box.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        self.output_box.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')

        # 'Select File' button
        select_file_button = tk.Button(self, text="Select File To Translate", command=self.open_file)
        select_file_button.grid(row=3, column=0, padx=10, pady=5, sticky='nsew')

        # 'Save File' button
        save_file_button = tk.Button(self, text="Save Output", command=self.save_file)
        save_file_button.grid(row=3, column=2, sticky='nsew')

    def translate(self, event = None):
        input_text = self.input_box.get("1.0", 'end-1c')  # Get text from input_box
        in_lang = self.input_lang.get()
        out_lang = self.output_lang.get()
        if in_lang == out_lang:
            messagebox.showinfo("Error", "Input and Output language cannot be the same.")
            return

        output_text = self.translator.translate(input_text, in_lang, out_lang)
        self.output_box['state'] = tk.NORMAL    # Temporarily enable the widget
        self.output_box.delete("1.0", tk.END)  # Clear output_box
        self.output_box.insert(tk.END, output_text)  # Insert the translated text
        self.output_box['state'] = tk.DISABLED # Disable the widget again

    def switch(self):
        output_text = self.output_box.get("1.0", 'end-1c')
        self.input_box.delete("1.0", tk.END)
        self.input_box.insert(tk.END, output_text)
        temp = self.input_lang.get()
        self.input_lang.set(self.output_lang.get())
        self.output_lang.set(temp)
        self.translate()  # Translate after switching languages

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
        with open(file_path, 'r') as file:
            input_text = file.read()
        self.input_box.delete("1.0", tk.END)  # Clear input_box
        self.input_box.insert(tk.END, input_text)  # Insert the file content
        self.translate()

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[('Text Files', '*.txt')])
        output_text = self.output_box.get("1.0", 'end-1c')  # Get text from output_box
        with open(file_path, 'w') as file:
            file.write(output_text)

    def validate_input(self, language, input_text):
        if language == 'Text':
            # All input is valid for text
            return True
        elif language == 'Binary':
            # Check if all characters are 0 or 1
            return all(char in '01 ' for char in input_text)
        elif language == 'Morse Code':
            # Check if all characters are dots, dashes, spaces or slash (representing space between words)
            return all(char in '.-/ ' for char in input_text)
        elif language == 'ASCII':
            # Check if all characters are either a space or a digit (ASCII representation is in decimal)
            return all(char.isspace() or char.isdigit() for char in input_text)
        elif language == 'Hexadecimal':
            # Check if all characters are hexadecimal digits
            return all(char in '0123456789abcdefABCDEF ' for char in input_text)
        elif language == 'Base64':
            # Base64 characters are alphanumeric and also include '+' and '/'
            # Check that the length of the string (without padding '=') is a multiple of 4
            return all(char.isalnum() or char in '+/ ' for char in input_text.rstrip('=') ) and len(input_text.rstrip('=')) % 4 == 0
        else:
            #implement a exception for characters/languages that are not implemented
            return null
    
    def handle_input(self, event=None):
        # Get the current language
        current_language = self.input_lang.get()

        # Get the current input
        input_text = self.input_box.get("1.0", 'end-1c')

        # Check if the input is valid
        if not self.validate_input(current_language, input_text):
            # If not, delete the last character
            self.input_box.delete('end-2c')
        else:
            self.translate()

        



class PracticePage(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        # Instantiate PracticeMode
        self.practice_mode = PracticeMode()

        # Get languages from the translator
        self.languages = self.practice_mode.languages
        self.target_language = tk.StringVar()

        # Create the drop-down menu for language selection
        self.target_lang_menu = ttk.Combobox(self, textvariable=self.target_language, values=self.languages)

        self.target_lang_menu.current(0)  # default value
        self.target_lang_menu.bind('<<ComboboxSelected>>', self.new_text)

        # Create the labels, text boxes, and entry field
        self.prompt_label = tk.Label(self, text="Translate this:")
        self.input_label = tk.Label(self, text="Your translation:")
        self.prompt_box = tk.Text(self, height=10, width=50)
        self.prompt_box['state'] = tk.DISABLED
        self.input_box = tk.Text(self, height=10, width=50)
        self.length_label = tk.Label(self, text="Length of the source text:")
        self.length_entry = tk.Entry(self)

        self.length_entry.bind('<KeyRelease>', self.validate)

        
        
        # Create the buttons
        self.new_text_button = tk.Button(self, text="New Text", command=self.new_text)
        self.check_button = tk.Button(self, text="Check", command=self.check)

        # Grid layout
        self.target_lang_menu.grid(row=1, column=0, padx=10, pady=5, sticky='nsew')
        self.length_label.grid(row=0, column=1, padx=10, pady=5, sticky='nsew')
        self.length_entry.grid(row=1, column=1, padx=10, pady=5, sticky='nsew')
        self.new_text_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')
        
        self.prompt_label.grid(row=3, column=0, padx=10, pady=5, sticky='nsew')
        self.prompt_box.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

        self.input_label.grid(row=5, column=0, padx=10, pady=5, sticky='nsew')
        self.input_box.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')
        self.check_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

        # Configuring column and row weights for resizing
        for i in range(2):
            self.columnconfigure(i, weight=1)
        for i in range(8):
            self.rowconfigure(i, weight=1)

        self.new_text()  # Generate the first text

    def new_text(self, event=None):
        # Generate a new random text
        try:
            length = min(int(self.length_entry.get()), 50)
        except ValueError:  # Handle the case where the user has not entered anything
            length = 1
        self.code = self.practice_mode.generate(length, self.target_language.get())
        self.prompt_box['state'] = tk.NORMAL
        self.prompt_box.delete("1.0", tk.END)
        self.prompt_box.insert(tk.END, self.code)
        self.prompt_box['state'] = tk.DISABLED

    def check(self):
        # Check the user's translation
        user_translation = self.input_box.get("1.0", 'end-1c')
        is_correct, correct_translation = self.practice_mode.check(user_translation, self.target_language.get())
        if is_correct:
            messagebox.showinfo("Result", "Correct!")
            self.new_text()
        else:
            messagebox.showinfo("Result", "Incorrect. The correct translation is:\n" + correct_translation)

    def validate(self, event = None):
        try:
            int(self.length_entry.get())
        except ValueError:
            self.length_entry.delete(len(self.length_entry.get())-1)
        else:
            self.new_text()

class ImagePage(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.image_to_text = ImageToText()

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.output_box = tk.Text(self, height=10, width=50)

        open_file_button = tk.Button(self, text="Open Image File", command=self.open_file)
        save_file_button = tk.Button(self, text="Save Output", command=self.save_file)

        open_file_button.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')
        self.output_box.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        save_file_button.grid(row=2, column=0, padx=10, pady=5, sticky='nsew')

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.png *.jpg *.jpeg')])
        output_text = self.image_to_text.to_string(file_path)
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, output_text)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[('Text Files', '*.txt')])
        output_text = self.output_box.get("1.0", 'end-1c')
        with open(file_path, 'w') as file:
            file.write(output_text)


class HelpPage(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        # Create a Text widget to display the help text
        self.help_text = tk.Text(self, height=10, width=50)

        with open('help.txt', 'r') as f:
            help_content = f.read()
        self.help_text.insert(tk.END, help_content)
        
        # Set the text widget to read-only
        self.help_text.config(state='disabled')

        self.help_text.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        # Configure weights for resizing
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("TransCrypt")

    notebook = ttk.Notebook(root)

    translator_page = TranslatorPage(notebook)
    notebook.add(translator_page, text="Translator")

    practice_page = PracticePage(notebook)
    notebook.add(practice_page, text="Practice Mode")

    image_page = ImagePage(notebook)
    notebook.add(image_page, text="Image to Text")

    # Add the help page
    help_page = HelpPage(notebook)
    notebook.add(help_page, text="Help")

    notebook.pack(expand=1, fill='both')

    root.mainloop()

