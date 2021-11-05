#Author: Danny Chung
#Date: 10/20/2021
#Description: Dungeons and Dragons Character Sheet class, Main User Interface

import tkinter as tk
from tkinter import *
from tkinter.tix import *
from tkinter import tix
from tkinter import ttk
from PIL import ImageTk, Image
import os
import DDCharacterSheetLogic

class DDCharacterSheet:
    """
    Sets up user interface for Dungeons and Dragons Character Sheet.
    """
    def __init__(self, master):

        #Row 0
        self.characterPicture = ImageTk.PhotoImage(Image.open("new.jpg"))
        self.pictureFrame = tk.Label(root, image = self.characterPicture)
        self.pictureFrame.grid(column = 2, row = 0, sticky = "NSEW")

        self.newCharacter = tk.Button(root, command = lambda: DDCharacterSheetLogic.create_character(self), text = "Create New Character", padx = 10, pady=3)
        self.newCharacter.grid(column = 0, row = 0, sticky = "NSEW")
        tip1 = Balloon(root)
        tip1.bind_widget(self.newCharacter, balloonmsg = "Clear all current fields.")
        self.loadCharacter = tk.Button(root, command = lambda: DDCharacterSheetLogic.load_character(self), text = "Load a Character", padx = 10, pady=3)
        self.loadCharacter.grid(column = 1, row = 0, sticky = "NSEW")
        tip2 = Balloon(root)
        tip2.bind_widget(self.loadCharacter, balloonmsg = "Load a .csv character file, replacing all fields.")

        self.selectPhoto = tk.Button(root, command = lambda: DDCharacterSheetLogic.open_character_image(self), text ="Select a Character Photo", padx = 10, pady = 3)
        self.selectPhoto.grid(column = 2, row = 0, sticky = "S")
        tip7 = Balloon(root)
        tip7.bind_widget(self.selectPhoto, balloonmsg = "Select a character photo from a .jpeg file. Recommended size of 100x100px.")

        #Row 1 ==============SEPARATOR==============
        self.separator = ttk.Separator(root, orient = "horizontal")
        self.separator.grid(column = 0 , row = 1, columnspan = 3, sticky = "EW")
        self.blankSpace = tk.Label(text = "")
        self.blankSpace.grid(column = 0, row = 1, sticky = "W")

        #Row 2
        self.playerNameLabel = tk.Label(text = "Player Name:")
        self.playerNameLabel.grid(column = 0, row = 2, sticky = "E")
        self.playerNameText = tk.Entry()
        self.playerNameText.insert(0, "Player Name")
        self.playerNameText.grid(column=1, row = 2, sticky = "W", padx = 5)

        #Row 3
        self.characterNameLabel = tk.Label(text = "Character Name:")
        self.characterNameLabel.grid(column = 0, row = 3, sticky = "E")
        self.characterNameText = tk.Entry()
        self.characterNameText.insert(0, "Character Name")
        self.characterNameText.grid(column=1, row = 3, sticky = "W", padx = 5)
        self.generateName = tk.Button(root, command = lambda: DDCharacterSheetLogic.generate_name(self), text = "Generate a Random Name", padx = 10, pady = 0)
        self.generateName.grid(column = 1, row = 3, sticky = "E")
        tip3 = Balloon(root)
        tip3.bind_widget(self.generateName, balloonmsg = "Randomly generate a character name. Replaces current character name.")

        #Row 4
        self.genderLabel = tk.Label(text = "Gender:")
        self.genderLabel.grid(column = 0, row = 4, sticky = "E")
        self.genderText = tk.Entry()
        self.genderText.insert(0, "Gender")
        self.genderText.grid(column=1, row = 4, sticky = "W", padx = 5)

        #Row 5
        self.raceLabel = tk.Label(text = "Race:")
        self.raceLabel.grid(column = 0, row = 5, sticky = "E")
        self.raceText = tk.Entry()
        self.raceText.insert(0, "Race")
        self.raceText.grid(column=1, row = 5, sticky = "W", padx = 5)

        #Row 6
        self.classLabel = tk.Label(text = "Class:")
        self.classLabel.grid(column = 0, row = 6, sticky = "E")
        self.classText = tk.Entry()
        self.classText.insert(0, "Class")
        self.classText.grid(column=1, row = 6, sticky = "W", padx = 5)

        #Row 7
        self.alignmentLabel = tk.Label(text = "Alignment:")
        self.alignmentLabel.grid(column = 0, row = 7, sticky = "E")
        self.alignmentText = tk.Entry()
        self.alignmentText.insert(0, "Alignment")
        self.alignmentText.grid(column=1, row = 7, sticky = "W" , padx = 5)

        #Row 8
        self.biographyFrame = tk.Frame(root, width = 500, height = 100)
        self.biographyFrame.grid(column = 1, columnspan = 2, row = 8, sticky = "W")
        self.biographyFrame.grid_propagate(False)
        self.biographyLabel = tk.Label(text = "Biography:")
        self.biographyLabel.grid(column = 0, row = 8, sticky = "NE")
        self.biographyText = tk.Text(self.biographyFrame)
        self.biographyText.insert("1.0", "Biographical text.")
        self.biographyText.grid(column = 1, columnspan = 2, row = 8, sticky = "WEN", padx = 5)

        #Row 9 ==============SEPARATOR==============
        self.separator2 = ttk.Separator(root, orient = "horizontal")
        self.separator2.grid(column = 0 , row = 9, columnspan = 3, sticky = "EW")
        self.blankSpace2 = tk.Label(text = "")
        self.blankSpace2.grid(column = 0, row = 9, sticky = "W", pady = 5)

        #Row 10
        self.levelLabel = tk.Label(text = "Level:")
        self.levelLabel.grid(column = 0, row = 10, sticky = "E")
        self.levelText = tk.Entry()
        self.levelText.insert(0, "Level")
        self.levelText.grid(column=1, row = 10, sticky = "W", padx = 5)

        #Row 11
        self.expLabel = tk.Label(text = "Total Experience Points:")
        self.expLabel.grid(column = 0, row = 11, sticky = "E")
        self.expText = tk.Entry()
        self.expText.insert(0, "Total Points")
        self.expText.grid(column=1, row = 11, sticky = "W", padx=5, pady = 8)

        #Row 12
        self.expAddLabel = tk.Label(text = "+")
        self.expAddLabel.grid(column=1, row = 12, sticky = "W", padx=5)

        #Row 13
        self.expAddText = tk.Entry()
        self.expAddText.insert(0, "Points to be Added")
        self.expAddText.grid(column=1, row = 13, sticky = "W", padx=5)
        self.addExpButton = tk.Button(root, text = "Add to Total Experience Points", padx = 10)
        self.addExpButton.grid(column = 1, row = 13, sticky = "E")
        tip4 = Balloon(root)
        tip4.bind_widget(self.addExpButton, balloonmsg = "Click to add number in this field to Total Experience Points.")

        #Row 14
        self.curHpLabel = tk.Label(text = "Current Hit Points:")
        self.curHpLabel.grid(column = 0, row = 14, sticky = "E")
        self.curHpText = tk.Entry()
        self.curHpText.insert(0, "Current HP")
        self.curHpText.grid(column=1, row = 14, sticky = "W", padx = 5, pady = 8)

        self.totHpLabel = tk.Label(text = "Total Hit Points:")
        self.totHpLabel.grid(column = 1, row = 14, sticky = "E")
        self.totHpText = tk.Entry()
        self.totHpText.insert(0, "Total HP")
        self.totHpText.grid(column=2, row = 14, sticky = "W", padx = 5, pady = 8)

        #Row 15
        self.separator3 = ttk.Separator(root, orient = "horizontal")
        self.separator3.grid(column = 0 , row = 15, columnspan = 2, sticky = "EW")
        self.blankSpace2 = tk.Label(text = "")
        self.blankSpace2.grid(column = 0, row = 15, sticky = "W", pady = 5)

        self.attrLabel = tk.Label(text = "Attributes", font = "Calibri 11 underline")
        self.attrLabel.grid(column = 0, row = 15, sticky = "E")
        self.generateAttr = tk.Button(root, command = lambda: DDCharacterSheetLogic.generate_attr(self), text = "Generate Random Attributes", padx = 10, pady = 0)
        self.generateAttr.grid(column = 1, row = 15, sticky = "W")
        tip5 = Balloon(root)
        tip5.bind_widget(self.generateAttr, balloonmsg = "Generate random attributes. Replaces all current attributes.")

        #Row 16 to 21
        self.strLabel = tk.Label(text = "Strength:")
        self.strLabel.grid(column = 0, row = 16, sticky = "E")
        self.strText = tk.Entry()
        self.strText.insert(0, "Str")
        self.strText.grid(column=1, row = 16, sticky = "W")

        self.dexLabel = tk.Label(text = "Dexterity:")
        self.dexLabel.grid(column = 0, row = 17, sticky = "E")
        self.dexText = tk.Entry()
        self.dexText.insert(0, "Dex")
        self.dexText.grid(column=1, row = 17, sticky = "W")

        self.conLabel = tk.Label(text = "Constitution:")
        self.conLabel.grid(column = 0, row = 18, sticky = "E")
        self.conText = tk.Entry()
        self.conText.insert(0, "Con")
        self.conText.grid(column=1, row = 18, sticky = "W")

        self.intLabel = tk.Label(text = "Intelligence:")
        self.intLabel.grid(column = 0, row = 19, sticky = "E")
        self.intText = tk.Entry()
        self.intText.insert(0, "Int")
        self.intText.grid(column=1, row = 19, sticky = "W")

        self.wisLabel = tk.Label(text = "Wisdom:")
        self.wisLabel.grid(column = 0, row = 20, sticky = "E")
        self.wisText = tk.Entry()
        self.wisText.insert(0, "Wis")
        self.wisText.grid(column=1, row = 20, sticky = "W")

        self.chrLabel = tk.Label(text = "Charisma:")
        self.chrLabel.grid(column = 0, row = 21, sticky = "E")
        self.chrText = tk.Entry()
        self.chrText.insert(0, "Chr")
        self.chrText.grid(column=1, row = 21, sticky = "W")

        #Row 22
        self.separator4 = ttk.Separator(root, orient = "horizontal")
        self.separator4.grid(column = 0 , row = 22, columnspan = 1, sticky = "EW")
        self.blankSpace2 = tk.Label(text = "")
        self.blankSpace2.grid(column = 0, row = 22, sticky = "W", pady = 2)

        #Row 23
        self.equipmentLabel = tk.Label(text = " Equipment:")
        self.equipmentLabel.grid(column = 0, row = 23, sticky = "W")

        self.skillLabel = tk.Label(text = "Attacks, Spells, and Skills:")
        self.skillLabel.grid(column = 1, row = 23, sticky = "W")

        #Row 24
        self.equipmentFrame = tk.Frame(root, width = 300, height = 200, pady = 5)
        self.equipmentFrame.grid(column = 0, row = 24, sticky = "W")
        self.equipmentFrame.grid_propagate(False)
        self.equipmentText = tk.Text(self.equipmentFrame)
        self.equipmentText.insert("1.0", "Equipment")
        self.equipmentText.grid(column = 0, row = 24, sticky = "W", padx = 5, pady = 5)

        self.skillFrame = tk.Frame(root, width = 300, height = 200, pady = 5)
        self.skillFrame.grid(column = 1, row = 24, sticky = "W")
        self.skillFrame.grid_propagate(False)
        self.skillText = tk.Text(self.skillFrame)
        self.skillText.insert("1.0", "Attacks, Spells, Skills")
        self.skillText.grid(column = 1, row = 24, sticky = "W", padx = 5, pady = 5)

        self.saveCharacter = tk.Button(root, command = lambda: DDCharacterSheetLogic.save_character(self), text = "Save Character", padx = 10, pady=3)
        self.saveCharacter.grid(column = 2, row = 24, sticky = "NSEW", padx= 5, pady = 5)
        tip6 = Balloon(root)
        tip6.bind_widget(self.saveCharacter, balloonmsg = "Save current fields to a .csv file.")

        """
        List of fields, used by DDCharacterSheetLogic for iteration.
        """
        self.entryFields = [
            self.playerNameText,
            self.characterNameText,
            self.genderText,
            self.raceText,
            self.classText,
            self.alignmentText,
            self.levelText,
            self.expText,
            self.expAddText,
            self.curHpText,
            self.totHpText,
            self.strText,
            self.dexText,
            self.conText,
            self.intText,
            self.wisText,
            self.chrText,
        ]

        self.textFields = [
            self.biographyText,
            self.equipmentText,
            self.skillText
        ]


#Set root, dimensions, and title for UI window.
root = tix.Tk()
root.geometry("1000x925")
root.title("Dungeons & Dragons Character Sheet")

app = DDCharacterSheet(root)

#Row and Column Configuration
root.rowconfigure(0, weight = 1, minsize = 100)
for col in range(3):
    root.columnconfigure(col, weight = 1, minsize = 100)

root.mainloop()