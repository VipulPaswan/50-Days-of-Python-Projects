from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

#        Translator Setup       #

translator = Translator()

# language dictionary
languages = {v: k for k, v in LANGUAGES.items()}
language_list = list(languages.keys())

#        Functions              #

def translate_text():
    try:
        source_lang = comb_source.get()
        dest_lang = comb_dest.get()

        src_code = languages[source_lang]
        dest_code = languages[dest_lang]

        text = source_text.get(1.0, END).strip()

        if text == "":
            messagebox.showwarning("Warning", "Please enter text to translate")
            return

        result = translator.translate(text, src=src_code, dest=dest_code)

        dest_text.delete(1.0, END)
        dest_text.insert(END, result.text)

    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_text():
    source_text.delete(1.0, END)
    dest_text.delete(1.0, END)

def swap_language():
    src = comb_source.get()
    dest = comb_dest.get()

    comb_source.set(dest)
    comb_dest.set(src)

#        Main Window            #

root = Tk()
root.title("AI Language Translator")
root.geometry("600x650")
root.config(bg="#1e1e2f")

#        Title                  #

title = Label(
    root,
    text="Language Translator",
    font=("Helvetica", 28, "bold"),
    bg="#1e1e2f",
    fg="white"
)

title.pack(pady=20)

#        Source Label           #

label_source = Label(
    root,
    text="Source Text",
    font=("Helvetica", 16, "bold"),
    bg="#1e1e2f",
    fg="white"
)

label_source.pack()

#        Source Textbox         #

source_text = Text(
    root,
    height=6,
    width=60,
    font=("Arial", 14),
    wrap=WORD,
    bd=3
)

source_text.pack(pady=10)

#        Language Frame         #

lang_frame = Frame(root, bg="#1e1e2f")
lang_frame.pack(pady=10)

comb_source = ttk.Combobox(
    lang_frame,
    values=language_list,
    width=20
)

comb_source.set("english")
comb_source.grid(row=0, column=0, padx=10)

swap_button = Button(
    lang_frame,
    text="⇄ Swap",
    command=swap_language,
    font=("Arial", 12, "bold"),
    bg="#ff9800",
    fg="white"
)

swap_button.grid(row=0, column=1, padx=10)

comb_dest = ttk.Combobox(
    lang_frame,
    values=language_list,
    width=20
)

comb_dest.set("hindi")
comb_dest.grid(row=0, column=2, padx=10)

#        Buttons                #

button_frame = Frame(root, bg="#1e1e2f")
button_frame.pack(pady=15)

translate_button = Button(
    button_frame,
    text="Translate",
    command=translate_text,
    font=("Arial", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    width=12
)

translate_button.grid(row=0, column=0, padx=10)

clear_button = Button(
    button_frame,
    text="Clear",
    command=clear_text,
    font=("Arial", 14, "bold"),
    bg="#f44336",
    fg="white",
    width=12
)

clear_button.grid(row=0, column=1, padx=10)

#        Destination Label      #

label_dest = Label(
    root,
    text="Translated Text",
    font=("Helvetica", 16, "bold"),
    bg="#1e1e2f",
    fg="white"
)

label_dest.pack(pady=5)

#        Destination Textbox    #

dest_text = Text(
    root,
    height=6,
    width=60,
    font=("Arial", 14),
    wrap=WORD,
    bd=3
)

dest_text.pack(pady=10)

#        Run App                #

root.mainloop()