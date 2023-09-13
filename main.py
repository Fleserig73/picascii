"""
picascii
Fleserig73
"""
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from PIL import Image, ImageOps

root = ctk.CTk()
root.title("picascii")
root.geometry("800x400")
root.iconphoto(False, tk.PhotoImage(file="picascii.png"))
root.resizable(False, False)
size=124
path_i=""

def slider_event(value):
    global size
    size = int(value)
    l_size.configure(text=size)

def change_image(e):
    global path_i
    path = filedialog.askopenfilename(title='Open a file',initialdir='/',filetypes=(("PNG", "*.png"), ("jpeg", "*.jpeg"), ("jpeg", "*.jpeg")))
    if path:
        path_i = path
        my_image = ctk.CTkImage(dark_image=Image.open(path_i), size=(300, 340))
        l_image.configure(image=my_image)

def change_size(e):
    global size
    dialog = ctk.CTkInputDialog(text="Type in a custom size (width):", title="Change size")
    number_pick = dialog.get_input()
    if number_pick is not None and number_pick.isnumeric():
        size = int(number_pick)
        l_size.configure(text=size)

def create():
    global size, path_i
    if path_i != "":
        path = filedialog.asksaveasfile(initialfile="picascii", defaultextension=".txt")
        if path is not None:
            path = path.name
            new_x = int(size)
            chars = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
            interval = len(chars)/256
            image = Image.open(path_i)
            x, y = image.size
            image = image.resize((new_x, int(y * (new_x/x))))
            image = ImageOps.grayscale(image)
            text_file = open(path, "w")
            x, y = image.size
            for i in range(y):
                for j in range(x):
                    color = image.getpixel((j, i))
                    print(color)
                    text_file.write(chars[int(color*interval)])
                text_file.write("\n")

l_image = ctk.CTkLabel(root, font=ctk.CTkFont(size=169), text="+", width=340, height=340, fg_color="#333333", corner_radius=25)
l_image.place(x=30, y=30)

frame = ctk.CTkFrame(master=root)
frame.place(x=400, y=145)

l_size = ctk.CTkLabel(frame, text=size, fg_color="transparent")
l_size.pack()

size_slider = ctk.CTkSlider(frame, from_=1, to=250, command=slider_event, width=350)
size_slider.pack()

crte_btn = ctk.CTkButton(frame, text="create", command=create)
crte_btn.pack(pady=20)

l_size.bind("<Button-1>", change_size)
l_image.bind("<Button-1>", change_image)



root.mainloop()