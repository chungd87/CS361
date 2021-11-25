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
import time
import subprocess
import json

header = ['playerName', 'characterName', 'gender', 'race', 'class', 'alignment', 'level,', 'exp',
          'expAdd', 'curHp', 'totHp', 'str', 'dex', 'con', 'int', 'wis', 'chr', 'bio', 'equip', 'skill', 'imgDirectory']

def main():
    pass

def create_character(root):
    """
    Reset all fields and set photo to default photo.
    """
    msgBox = tk.messagebox.askquestion("Create New Character", "Are you sure you want to create a new character? This will erase all existing data fields.")
    if msgBox == "yes":
        root.levelText.configure(state = "normal")
        root.expText.configure(state = "normal")
        clear_all_fields(root)
        root.levelText.configure(state = "readonly")
        root.expText.configure(state = "readonly")

        #Reset character photo to default.
        change_image(root, "new.jpg")
        root.image_path = "new.jpg"

def load_character(root):
    """
    Import fields from a .csv file.
    """
    root.levelText.configure(state="normal")
    root.expText.configure(state="normal")

    #Put 2nd row of .csv, which contains the field data, into list rowsfile.
    rowsfile = []
    characterFileInfo = filedialog.askopenfilename(initialdir = "/", title = "Select a Character File", filetypes = (("CSV", "*.csv"), ))
    with open(characterFileInfo, 'r') as inputFile:
        fileContent = csv.reader(inputFile, delimiter = ',', skipinitialspace = True)
        for rows in fileContent:
            rowsfile.append(rows)

        characterData = rowsfile[1]

    clear_all_fields(root)

    #Put data from rowsfile into proper fields in UI.
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

    root.levelText.configure(state="readonly")
    root.expText.configure(state="readonly")

    #Set photo and image path.
    change_image(root, characterData[j])

def generate_name(root):
    """
    Using microservice, generates a random first and last name into the Character Name field.
    """
    msgBox = tk.messagebox.askquestion("Generate Name", "Are you sure you want to generate a new name? Current name will be lost.")
    if msgBox == "yes":
        #Run DNDGenerator microservice as subprocess to generate a random first and last name.
        subprocess.run(["python3", "./DnDGenerator/generator.py", "-n"])
        time.sleep(0.025)  # Wait for file generation.
        with open("response.json", "r") as generatedFile:
            firstName = json.load(generatedFile)
        subprocess.run(["python3", "./DnDGenerator/generator.py", "-n"])
        time.sleep(0.025)  # Wait for file generation.
        with open("response.json", "r") as generatedFile:
            lastName = json.load(generatedFile)

        #Combine first and last name, put in Character Name field.
        randomName = str(firstName + " " + lastName)
        root.characterNameText.delete(0, "end")
        root.characterNameText.insert(0, randomName)

def generate_attr(root):
    """
    Using microservice, generates random attributes and inserts them in attribute fields accordingly.
    """
    msgBox = tk.messagebox.askquestion("Generate Attributes", "Are you sure you want to generate random attributes? Current attributes will be lost.")
    if msgBox == "yes":
        #Run DNDGenerator microservice as subprocess to generate random attributes.
        subprocess.run(["python3", "./DnDGenerator/generator.py", "-s"])
        time.sleep(0.05)  # Wait for file generation.
        with open("response.json", "r") as generatedFile:
            randomStats = json.load(generatedFile)

        #Clear proper fields and place attributes into proper fields.
        root.strText.delete(0, "end")
        root.strText.insert(0, randomStats["strength"])
        root.dexText.delete(0, "end")
        root.dexText.insert(0, randomStats["dexterity"])
        root.conText.delete(0, "end")
        root.conText.insert(0, randomStats["constitution"])
        root.intText.delete(0, "end")
        root.intText.insert(0, randomStats["intelligence"])
        root.wisText.delete(0, "end")
        root.wisText.insert(0, randomStats["wisdom"])
        root.chrText.delete(0, "end")
        root.chrText.insert(0, randomStats["charisma"])

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

    #Store current image path to the list.
    updatedRow.append(root.image_path)

    print(updatedRow)

    #Output the file.
    fileName = filedialog.asksaveasfilename(initialdir="/", title="Save Character File", filetypes=(("CSV", "*.csv"),))
    with open(f"{fileName}.csv", 'w', newline='', encoding='utf-8') as outputFile:
        csvWriter = csv.writer(outputFile, delimiter = ",", lineterminator='\n')
        csvWriter.writerow(header)
        csvWriter.writerow(updatedRow)

def open_character_image(root):
    """
    Load character image from file and then into UI.
    """
    try:
        imageFileInfo = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select a Photo", filetypes = (("Images", "*.jpg"), ("All Files", "*.*") ))
        change_image(root, imageFileInfo)
        root.image_path = imageFileInfo
    except:
        pass

def update_exp(root):
    """
    Adds added experience points to total experience points, and checks for level update.
    """
    try:
        currentExp = root.expText.get()
        addedExp = root.expAddText.get()
        totalExp = (int(currentExp) + int(addedExp))

        root.levelText.configure(state="normal")
        root.expText.configure(state="normal")
        root.expText.delete(0, "end")
        root.expText.insert(0, totalExp)
        update_level(root, totalExp)
        root.levelText.configure(state="readonly")
        root.expText.configure(state="readonly")

        root.expAddText.delete(0, "end")
        root.expAddText.insert(0, "")

    except:
        pass

def adjustPoint(root, attribute, adjustment):
    """
    Enables usage of + and - buttons to increment and decrement attribute points.
    """
    #attributeDictionary for which button on the UI is clicked for each attribute.
    attributeDictionary = {
        "str": root.strText,
        "dex": root.dexText,
        "con": root.conText,
        "int": root.intText,
        "wis": root.wisText,
        "chr": root.chrText
    }
    attributeValue = attributeDictionary[attribute].get()

    #Increment or reset field to 0 if there is anything other than an int in the field currently.
    if adjustment == "+":
        try:
            attributeValue = int(attributeValue) + 1
            attributeDictionary[attribute].delete(0, "end")
            attributeDictionary[attribute].insert(0, attributeValue)
        except:
            attributeValue = 0
            attributeDictionary[attribute].delete(0, "end")
            attributeDictionary[attribute].insert(0, attributeValue)

    #Decrement or reset field to 0 if there is anything other than an int in the field currently.
    if adjustment == "-":
        try:
            attributeValue = int(attributeValue) - 1
            attributeDictionary[attribute].delete(0, "end")
            attributeDictionary[attribute].insert(0, attributeValue)
        except:
            attributeValue = 0
            attributeDictionary[attribute].delete(0, "end")
            attributeDictionary[attribute].insert(0, attributeValue)


def change_image(root, imgDirectory):
    """
    Helper function for loading an image into UI.
    """
    characterPicture = ImageTk.PhotoImage(Image.open(imgDirectory))
    root.pictureFrame.configure(image=characterPicture)
    root.pictureFrame.image = characterPicture

def clear_all_fields(root):
    """
    Helper function for emptying all fields in the DDCharacterSheet UI.
    """
    for field in root.entryFields:
        field.delete(0, "end")
    for field in root.textFields:
        field.delete(1.0, "end")

def reset_exp(root):
    """
    Helper function for resetting experience and level fields.
    """
    root.levelText.configure(state="normal")
    root.expText.configure(state="normal")
    root.expText.delete(0, "end")
    root.expText.insert(0, 0)
    root.expAddText.delete(0, "end")
    root.expAddText.insert(0, "")
    root.levelText.delete(0, "end")
    root.levelText.insert(0, 1)
    root.levelText.configure(state="readonly")
    root.expText.configure(state="readonly")

def level_number(root, number):
    """
    Helper function for changing the number in character's level field.
    """
    root.levelText.delete(0, "end")
    root.levelText.insert(0, number)

def update_level(root, totalExp):
    """
    Update level field according to level breakpoints.
    """
    levelBreakpointsDictionary = {
        0 : 1,
        300 : 2,
        900 : 3,
        2700 : 4,
        6500 : 5,
        14000 : 6,
        23000 : 7,
        34000 : 8,
        48000 : 9,
        64000 : 10,
        85000 : 11,
        100000 : 12,
        120000 : 13,
        140000 : 14,
        165000 : 15,
        195000 : 16,
        225000 : 17,
        265000 : 18,
        305000 : 19,
        355000 : 20
    }

    for experience in levelBreakpointsDictionary:
        if totalExp >= experience:
            level_number(root, levelBreakpointsDictionary[experience])

if __name__ == "__main__":
    main()