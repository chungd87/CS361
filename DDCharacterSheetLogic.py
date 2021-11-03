#Author: Danny Chung
#Date: 10/20/2021
#Description: Dungeons and Dragons Character Sheet class. Logic behind interface.

from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import tkinter as tk
import os

def main():
    pass

def create_character(root):
    msgBox = tk.messagebox.askquestion("Create New Character", "Are you sure you want to create a new character? This will reset current existing data.")
    if msgBox == "yes":
        print("hi")

def load_character(root):
    characterFileInfo = filedialog.askopenfile(initialdir = "/", title = "Select a Character File", filetypes = (("CSV", "*.csv"), ))
    print("hi")

def generate_name(root):
    msgBox = tk.messagebox.askquestion("Generate Name", "Are you sure you want to generate a new name? Current name will be lost.")
    if msgBox == "yes":
        print("hi")

def generate_attr(root):
    msgBox = tk.messagebox.askquestion("Generate Attributes", "Are you sure you want to generate random attributes? Current attributes will be lost.")
    if msgBox == "yes":
        print("hi")

def save_character(root):
    fileName = filedialog.asksaveasfile(initialdir = "/", title = "Save Character File", filetypes = (("CSV", "*.csv"), ))

def open_character_image(root):
    imageFileInfo = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select a Photo", filetypes = (("Images", "*.jpg"), ("All Files", "*.*") ))
    characterPicture = ImageTk.PhotoImage(Image.open(imageFileInfo))
    root.pictureFrame.configure(image = characterPicture)
    root.pictureFrame.image = characterPicture

if __name__ == "__main__":
    main()