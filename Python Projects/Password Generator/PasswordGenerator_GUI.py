import tkinter as tk
import random
import string
from PIL import Image, ImageTk  # Import the required modules from Pillow

class GuiPasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        self.length_label = tk.Label(master, text="Enter password length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(master)
        self.length_entry.pack()

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(master, text="")
        self.password_label.pack()

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_label.config(text="Generated Password: " + password)
        except ValueError as e:
            self.password_label.config(text="Error: " + str(e))


if __name__ == "__main__":
    root = tk.Tk()
    
    # Window Icon
    window_icon = ImageTk.PhotoImage(file="images/password.png")
    root.iconphoto(False, window_icon)
    gui_password_generator = GuiPasswordGenerator(root)
    
    root.mainloop()
