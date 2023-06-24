import tkinter as tk
import tkinter.font as tkFont

def process_text():
    text = entry_text.get()
    
    if encode_var.get():
        utf8_encoded = text.encode('utf-8')
        iso_encoded = utf8_encoded.decode('ISO-8859-1', errors='ignore')
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, iso_encoded)
    else:
        utf8_decoded = text.encode('ISO-8859-1', errors='ignore')
        original_text = utf8_decoded.decode('utf-8', errors='ignore')
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, original_text)

def copy_text():
    text_content = result_text.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(text_content)
    root.update()

def remove_placeholder(event, widget_type):
    if widget_type == "entry":
        if entry_widget.get() == placeholder_text_entry and entry_widget.cget("fg") == placeholder_color:
            entry_widget.delete(0, "end")
            entry_widget.config(fg="black")
    elif widget_type == "result":
        if result_text.get("1.0", "end-1c") == placeholder_text_result and result_text.cget("fg") == placeholder_color:
            result_text.delete("1.0", "end")
            result_text.config(fg="black")

def add_placeholder(event, widget_type):
    if widget_type == "entry":
        if entry_widget.get() == "":
            entry_widget.insert(0, placeholder_text_entry)
            entry_widget.config(fg=placeholder_color)
    elif widget_type == "result":
        if result_text.get("1.0", "end-1c") == "":
            result_text.insert("1.0", placeholder_text_result)
            result_text.config(fg=placeholder_color)

root = tk.Tk()
root.title("Mojibake Encrypter")

cool_font = tkFont.Font(size=12, family="Arial")

placeholder_text_entry = "Enter text to encode/decode..."
placeholder_text_result = "Processed text:"
placeholder_color = "gray"

entry_text = tk.StringVar()
entry_widget = tk.Entry(root, textvariable=entry_text)
entry_widget.place(x=20, y=20, width=260, height=25)
entry_widget.insert(0, placeholder_text_entry)
entry_widget.config(fg=placeholder_color)
entry_widget_remove = lambda event: remove_placeholder(event, "entry")
entry_widget_add = lambda event: add_placeholder(event, "entry")
entry_widget.bind("<FocusIn>", entry_widget_remove)
entry_widget.bind("<FocusOut>", entry_widget_add)

result_text = tk.Text(root, wrap=tk.WORD)
result_text.place(x=25, y=140, width=250, height=200)
result_text.insert("1.0", placeholder_text_result)
result_text.config(fg=placeholder_color)
result_text_remove = lambda event: remove_placeholder(event, "result")
result_text_add = lambda event: add_placeholder(event, "result")
result_text.bind("<FocusIn>", result_text_remove)
result_text.bind("<FocusOut>", result_text_add)

encode_var = tk.BooleanVar()
encode_var.set(True)

encode_radio = tk.Radiobutton(root, text="Encode", variable=encode_var, value=True)
encode_radio.place(x=50, y=60)

decode_radio = tk.Radiobutton(root, text="Decode", variable=encode_var, value=False)
decode_radio.place(x=180, y=60)

process_button = tk.Button(root, text="Process Text", command=process_text)
process_button.place(x=85, y=95, width=140, height=35)
process_button.config(padx=15, pady=15, font=cool_font, bg="plum")

copy_button = tk.Button(root, text="Copy to clipboard", command=copy_text)
copy_button.place(x=85, y=355, width=140, height=35)
copy_button.config(padx=15, pady=15, bg="plum", font=cool_font)

root.geometry("300x410")
root.configure(bg="slate gray")
root.resizable(width=False, height=False)

root.mainloop()
