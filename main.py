import tkinter as tk
from tkinter import filedialog

# Create window
root = tk.Tk()
root.title("My Smart Notepad")
root.geometry("800x600")
icon = tk.PhotoImage(file="notepad.ico")
root.iconphoto(True, icon)

# Create Text Area
text_area = tk.Text(root, undo=True, font=("Consolas", 18), padx=10, pady=10)
text_area.pack(fill="both", expand=True)

# -------- Functions --------
def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file = filedialog.askopenfilename()
    if file:
        try:
            with open(file, "r") as f:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, f.read())
        except:
            print("Error opening file")

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    if file:
        with open(file, "w") as f:
            f.write(text_area.get(1.0, tk.END))

def exit_app():
    root.quit()

# Edit Functions
def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

# -------- Menu Bar --------
menu_bar = tk.Menu(root)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

menu_bar.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)

menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Attach menu
root.config(menu=menu_bar)

# Keyboard Shortcuts
root.bind("<Control-n>", lambda event: new_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())

# Run app
root.mainloop()