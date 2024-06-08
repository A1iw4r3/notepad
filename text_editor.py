from tkinter import *
from tkinter import filedialog, font
from tkinter.messagebox import askyesno

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.filename = None
        self.bold_on = False
        self.italic_on = False
        self.underline_on = False
        self.font_size = 12
        self.master.title("Text Editor")
        self.master.geometry("800x600")
        self.text_area = Text(self.master, font=("Arial", self.font_size))
        self.text_area.pack(expand=YES, fill=BOTH)
        self.menu_bar = Menu(self.master)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_editor)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.font_menu = Menu(self.edit_menu, tearoff=0)
        self.font_size_menu = Menu(self.font_menu, tearoff=0)
        self.font_size_menu.add_command(label="8", command=lambda:self.set_font_size(8))
        self.font_size_menu.add_command(label="10", command=lambda:self.set_font_size(10))
        self.font_size_menu.add_command(label="12", command=lambda:self.set_font_size(12))
        self.font_size_menu.add_command(label="14", command=lambda:self.set_font_size(14))
        self.font_size_menu.add_command(label="16", command=lambda:self.set_font_size(16))
        self.font_size_menu.add_command(label="18", command=lambda:self.set_font_size(18))
        self.font_size_menu.add_command(label="20", command=lambda:self.set_font_size(20))
        self.font_size_menu.add_command(label="22", command=lambda:self.set_font_size(22))
        self.font_size_menu.add_command(label="24", command=lambda:self.set_font_size(24))
        self.font_size_menu.add_command(label="26", command=lambda:self.set_font_size(26))
        self.font_size_menu.add_command(label="28", command=lambda:self.set_font_size(28))
        self.font_size_menu.add_command(label="30", command=lambda:self.set_font_size(30))
        self.font_menu.add_cascade(label="Font Size", menu=self.font_size_menu)
        self.font_menu.add_command(label="Bold", command=self.toggle_bold)
        self.font_menu.add_command(label="Italic", command=self.toggle_italic)
        self.font_menu.add_command(label="Underline", command=self.toggle_underline)
        self.edit_menu.add_cascade(label="Font", menu=self.font_menu)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.master.config(menu=self.menu_bar)
        self.status_bar = Label(self.master, text="Ready        ", bd=1, relief=SUNKEN, anchor=W)
        self.status_bar.pack(side=BOTTOM, fill=X)
    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
        if self.filename:
            self.text_area.delete(1.0, END)
            with open(self.filename, "r") as f:
                self.text_area.insert(1.0, f.read())

    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.text_area.get(1.0, END))
            self.status_bar.config(text="File saved.")
        else:
            self.save_file_as()

    def save_file_as(self):
        self.filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.text_area.get(1.0, END))
            self.status_bar.config(text="File saved.")

    def exit_editor(self):
        if askyesno("Quit", "Are you sure you want to quit?"):
            self.master.destroy()

    def set_font_size(self, size):
        self.font_size = size
        self.text_area.config(font=("Arial", self.font_size))

    def toggle_bold(self):
        self.bold_on = not self.bold_on
        self.update_font()

    def toggle_italic(self):
        self.italic_on = not self.italic_on
        self.update_font()

    def toggle_underline(self):
        current_tags = self.text_area.tag_names("sel.first")
        if current_tags and "underline" in current_tags:
            self.text_area.tag_remove("underline", "sel.first", "sel.last")
        else:
            self.text_area.tag_add("underline", "sel.first", "sel.last")


    def update_font(self):
        font_weight = "normal"
        font_style = "roman"
        if self.bold_on:
            font_weight = "bold"
        if self.italic_on:
            font_style = "italic"
        if self.underline_on:
            font_style += " underline"
        self.text_area.tag_configure("tag-name", font=("Arial", self.font_size, font_style, font_weight))
        self.text_area.tag_add("tag-name", "sel.first", "sel.last")
        
root = Tk()
text_editor = TextEditor(root)
root.mainloop()