from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb

from PIL import Image, ImageTk
import os


def open_file():
    global file
    file = fd.askopenfilename(defaultextension='.txt', filetypes=[('All Files', '*.*'), ("Text File", "*.txt*")])

    if file != '':
        root.title(f"{os.path.basename(file)}")
        text_area.delete(1.0, END)
        with open(file, "r") as file_:
            text_area.insert(1.0, file_.read())
            file_.close()
    else:
        file = None


def new_file():
    root.title("Untitled - Editor")
    text_area.delete(1.0, END)


def save_file():
    global file
    if not file:
        file = fd.asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt',
                                    filetypes=[("Text File", "*.txt*"), ("Word Document", '*,docx*'), ("PDF", "*.pdf*")])
    with open(file,'w') as f:
        f.write(text_area.get(1.0, END))
    root.title(f"{os.path.basename(file)} - Editor")


def save_as_file():
    file = fd.asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt',
                                filetypes=[("Text File", "*.txt*"), ("Word Document", '*,docx*'), ("PDF", "*.pdf*")])
    with open(file,'w') as f:
        f.write(text_area.get(1.0, END))
    root.title(f"{os.path.basename(file)} - Editor")


def exit_application():
    root.destroy()


def copy_text():
    text_area.event_generate("<<Copy>>")


def cut_text():
    text_area.event_generate("<<Cut>>")


def paste_text():
    text_area.event_generate("<<Paste>>")


def select_all():
    text_area.event_generate("<<Control-KeyPress-A>>")


def about_us():
    mb.showinfo("About us", "This is just another text editor, but this is better than all others")


def about_commands():
    commands = """
Under the File Menu:
-> 'New' clears the entire Text Area
-> 'Open' clears text and opens another file
-> 'Save' saves your current file 
-> 'Save As' saves your data to new file

Under the Edit Menu:
-> 'Copy' copies the selected text to your clipboard
-> 'Cut' cuts the selected text and removes it from the text area 
-> 'Paste' pastes the copied/cut text
-> 'Select All' selects the entire text
"""
    mb.showinfo(title="All commands", message=commands)


# Initializing the window
root = Tk()
root.title("Untitled - Editor")
root.geometry('800x500')
root.resizable(1, 1)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

file = ''


# Top menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Text area to write
text_area = Text(root, font=("Times New Roman", 12))
text_area.grid(sticky=NSEW)

# Right Side scroll bar
scroller = Scrollbar(text_area, orient=VERTICAL)
scroller.pack(side=RIGHT, fill=Y)
scroller.config(command=text_area.yview)
text_area.config(yscrollcommand=scroller.set)

# File option on menu bar
file_menu = Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Close File", command=exit_application)
menu_bar.add_cascade(label="File", menu=file_menu)


# Edit option on menu bar
edit_menu = Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')
edit_menu.add_command(label='Copy', command=copy_text)
edit_menu.add_command(label='Cut', command=cut_text)
edit_menu.add_command(label='Paste', command=paste_text)
edit_menu.add_separator()
edit_menu.add_command(label='Select All', command=select_all)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Help option on menu bar
help_menu = Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')
help_menu.add_command(label='About Text Editor', command=about_us)
help_menu.add_command(label='About Commands', command=about_commands)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)
root.update()
root.mainloop()
