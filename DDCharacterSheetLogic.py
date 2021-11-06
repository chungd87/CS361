#Author: Danny Chung
#Date: 10/20/2021
#Description: Dungeons and Dragons Character Sheet class. Logic behind interface.

from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import tkinter as tk
import os
import csv

header = ['playerName', 'characterName', 'gender', 'race', 'class', 'alignment', 'level,', 'exp',
          'expAdd', 'curHp', 'totHp', 'str', 'dex', 'con', 'int', 'wis', 'chr', 'bio', 'equip', 'skill']

def main():
    pass

def create_character(root):
    """
    Reset all fields and set photo to default photo.
    """
    msgBox = tk.messagebox.askquestion("Create New Character", "Are you sure you want to create a new character? This will erase all existing data fields.")
    if msgBox == "yes":

        clear_all_fields(root)

        #Reset character photo to default.
        characterPicture = ImageTk.PhotoImage(Image.open("new.jpg"))
        root.pictureFrame.configure(image = characterPicture)
        root.pictureFrame.image = characterPicture

def load_character(root):
    """
    Import fields from a .csv file.
    """
    #Put 2nd row of .csv, which contains the field data, into list rowsfile.
    rowsfile = []
    characterFileInfo = filedialog.askopenfilename(initialdir = "/", title = "Select a Character File", filetypes = (("CSV", "*.csv"), ))
    with open(characterFileInfo, 'r') as inputFile:
        fileContent = csv.reader(inputFile, delimiter = ',', skipinitialspace = True)
        for rows in fileContent:
            rowsfile.append(rows)

        characterData = rowsfile[1]

    clear_all_fields(root)

    #Put data from rowsfile into proper fields.
    j = 0
    for field in root.entryFields:
        field.insert(0, characterData[j])
        j+=1
    for field in root.textFields:
        if "\\n" in characterData[j]:
            print(characterData[j])
            newData = characterData[j].replace("\\n", "\n")
            print(newData)
            field.insert(1.0, newData)
            j+=1
            continue
        else:
            field.insert(1.0, characterData[j])
            j+=1

def generate_name(root):
    msgBox = tk.messagebox.askquestion("Generate Name", "Are you sure you want to generate a new name? Current name will be lost.")
    if msgBox == "yes":
        print("hi")

def generate_attr(root):
    msgBox = tk.messagebox.askquestion("Generate Attributes", "Are you sure you want to generate random attributes? Current attributes will be lost.")
    if msgBox == "yes":
        print("hi")

def save_character(root):
    """
    Output all fields to a .csv file.
    """
    row = []
    updatedRow = []

    #Put fields into a list.
    for field in root.entryFields:
        row.append(field.get())
    for field in root.textFields:
        row.append(field.get(1.0,"end"))

    #Transform if needed to preserve \n new line without causing problems to .csv format.
    for data in row:
        if "\n" in data:
            newData = data.replace("\n", "\\n")
            updatedRow.append(newData)
            continue
        updatedRow.append(data)

    #Output the file.
    fileName = filedialog.asksaveasfilename(initialdir="/", title="Save Character File", filetypes=(("CSV", "*.csv"),))
    with open(f"{fileName}.csv", 'w', newline='', encoding='utf-8') as outputFile:
        csvWriter = csv.writer(outputFile, delimiter = ",", lineterminator='\n')
        csvWriter.writerow(header)
        csvWriter.writerow(updatedRow)

def open_character_image(root):
    """
    Load character image into UI.
    """
    try:
        imageFileInfo = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select a Photo", filetypes = (("Images", "*.jpg"), ("All Files", "*.*") ))
        characterPicture = ImageTk.PhotoImage(Image.open(imageFileInfo))
        root.pictureFrame.configure(image = characterPicture)
        root.pictureFrame.image = characterPicture
    except:
        pass

def clear_all_fields(root):
    """
    Empty all fields in the DDCharacterSheet UI.
    """
    for field in root.entryFields:
        field.delete(0, "end")
    for field in root.textFields:
        field.delete(1.0, "end")

if __name__ == "__main__":
    main()