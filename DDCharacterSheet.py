import tkinter as tk
from tkinter import *
from tkinter.tix import *
from tkinter import tix
from tkinter import ttk
from PIL import ImageTk, Image
import os
import DDCharacterSheetLogic

#Row 0
characterPicture = ImageTk.PhotoImage(Image.open("new.jpg"))
pictureFrame = tk.Label(root, image = characterPicture)
pictureFrame.grid(column = 2, row = 0, sticky = "NSEW")

newCharacter = tk.Button(root, command = lambda: DDCharacterSheetLogic.create_character(self), text = "Create New Character", padx = 10, pady=3)
newCharacter.grid(column = 0, row = 0, sticky = "NSEW")
tip1 = Balloon(root)
tip1.bind_widget(newCharacter, balloonmsg = "Clear all current fields.")
loadCharacter = tk.Button(root, command = lambda: DDCharacterSheetLogic.load_character(self), text = "Load a Character", padx = 10, pady=3)
loadCharacter.grid(column = 1, row = 0, sticky = "NSEW")
tip2 = Balloon(root)
tip2.bind_widget(loadCharacter, balloonmsg = "Load a .csv character file, replacing all fields.")

selectPhoto = tk.Button(root, command = lambda: DDCharacterSheetLogic.open_character_image(self), text ="Select a Character Photo", padx = 10, pady = 3)
selectPhoto.grid(column = 2, row = 0, sticky = "S")
tip7 = Balloon(root)
tip7.bind_widget(selectPhoto, balloonmsg = "Select a character photo from a .jpeg file. Recommended size of 200x200px.")

#Row 1 ==============SEPARATOR==============
separator = ttk.Separator(root, orient = "horizontal")
separator.grid(column = 0 , row = 1, columnspan = 3, sticky = "EW")
blankSpace = tk.Label(text = "")
blankSpace.grid(column = 0, row = 1, sticky = "W")

#Row 2
playerNameLabel = tk.Label(text = "Player Name:")
playerNameLabel.grid(column = 0, row = 2, sticky = "E")
playerNameText = tk.Entry()
playerNameText.insert(0, "Player Name")
playerNameText.grid(column=1, row = 2, sticky = "W", padx = 5)

#Row 3
characterNameLabel = tk.Label(text = "Character Name:")
characterNameLabel.grid(column = 0, row = 3, sticky = "E")
characterNameText = tk.Entry()
characterNameText.insert(0, "Character Name")
characterNameText.grid(column=1, row = 3, sticky = "W", padx = 5)
generateName = tk.Button(root, command = lambda: DDCharacterSheetLogic.generate_name(root), text = "Generate a Random Name", padx = 10, pady = 0)
generateName.grid(column = 1, row = 3, sticky = "E")
tip3 = Balloon(root)
tip3.bind_widget(generateName, balloonmsg = "Randomly generate a character name. Replaces current character name.")

#Row 4
genderLabel = tk.Label(text = "Gender:")
genderLabel.grid(column = 0, row = 4, sticky = "E")
genderText = tk.Entry()
genderText.insert(0, "Gender")
genderText.grid(column=1, row = 4, sticky = "W", padx = 5)

#Row 5
raceLabel = tk.Label(text = "Race:")
raceLabel.grid(column = 0, row = 5, sticky = "E")
raceText = tk.Entry()
raceText.insert(0, "Race")
raceText.grid(column=1, row = 5, sticky = "W", padx = 5)

#Row 6
classLabel = tk.Label(text = "Class:")
classLabel.grid(column = 0, row = 6, sticky = "E")
classText = tk.Entry()
classText.insert(0, "Class")
classText.grid(column=1, row = 6, sticky = "W", padx = 5)

#Row 7
alignmentLabel = tk.Label(text = "Alignment:")
alignmentLabel.grid(column = 0, row = 7, sticky = "E")
alignmentText = tk.Entry()
alignmentText.insert(0, "Alignment")
alignmentText.grid(column=1, row = 7, sticky = "W" , padx = 5)

#Row 8
biographyFrame = tk.Frame(root, width = 500, height = 100)
biographyFrame.grid(column = 1, columnspan = 2, row = 8, sticky = "W")
biographyFrame.grid_propagate(False)
biographyLabel = tk.Label(text = "Biography:")
biographyLabel.grid(column = 0, row = 8, sticky = "NE")
biographyText = tk.Text(biographyFrame)
biographyText.insert("1.0", "Biographical text.")
biographyText.grid(column = 1, columnspan = 2, row = 8, sticky = "WEN", padx = 5)

#Row 9 ==============SEPARATOR==============
separator2 = ttk.Separator(root, orient = "horizontal")
separator2.grid(column = 0 , row = 9, columnspan = 3, sticky = "EW")
blankSpace2 = tk.Label(text = "")
blankSpace2.grid(column = 0, row = 9, sticky = "W", pady = 5)

#Row 10
levelLabel = tk.Label(text = "Level:")
levelLabel.grid(column = 0, row = 10, sticky = "E")
levelText = tk.Entry()
levelText.insert(0, "Level")
levelText.grid(column=1, row = 10, sticky = "W", padx = 5)

#Row 11
expLabel = tk.Label(text = "Total Experience Points:")
expLabel.grid(column = 0, row = 11, sticky = "E")
expText = tk.Entry()
expText.insert(0, "Total Points")
expText.grid(column=1, row = 11, sticky = "W", padx=5, pady = 8)

#Row 12
expAddLabel = tk.Label(text = "+")
expAddLabel.grid(column=1, row = 12, sticky = "W", padx=5)

#Row 13
expTextAdd = tk.Entry()
expTextAdd.insert(0, "Points to be Added")
expTextAdd.grid(column=1, row = 13, sticky = "W", padx=5)
addExpButton = tk.Button(root, text = "Add to Total Experience Points", padx = 10)
addExpButton.grid(column = 1, row = 13, sticky = "E")
tip4 = Balloon(root)
tip4.bind_widget(addExpButton, balloonmsg = "Click to add number in this field to Total Experience Points.")

#Row 14
curHpLabel = tk.Label(text = "Current Hit Points:")
curHpLabel.grid(column = 0, row = 14, sticky = "E")
curHpText = tk.Entry()
curHpText.insert(0, "Current HP")
curHpText.grid(column=1, row = 14, sticky = "W", padx = 5, pady = 8)

totHpLabel = tk.Label(text = "Total Hit Points:")
totHpLabel.grid(column = 1, row = 14, sticky = "E")
totHpText = tk.Entry()
totHpText.insert(0, "Total HP")
totHpText.grid(column=2, row = 14, sticky = "W", padx = 5, pady = 8)

#Row 15
separator3 = ttk.Separator(root, orient = "horizontal")
separator3.grid(column = 0 , row = 15, columnspan = 2, sticky = "EW")
blankSpace2 = tk.Label(text = "")
blankSpace2.grid(column = 0, row = 15, sticky = "W", pady = 5)

attrLabel = tk.Label(text = "Attributes", font = "Calibri 11 underline")
attrLabel.grid(column = 0, row = 15, sticky = "E")
generateAttr = tk.Button(root, command = lambda: DDCharacterSheetLogic.generate_attr(root), text = "Generate Random Attributes", padx = 10, pady = 0)
generateAttr.grid(column = 1, row = 15, sticky = "W")
tip5 = Balloon(root)
tip5.bind_widget(generateAttr, balloonmsg = "Generate random attributes. Replaces all current attributes.")

#Row 16 to 21
strLabel = tk.Label(text = "Strength:")
strLabel.grid(column = 0, row = 16, sticky = "E")
strText = tk.Entry()
strText.insert(0, "Str")
strText.grid(column=1, row = 16, sticky = "W")

dexLabel = tk.Label(text = "Dexterity:")
dexLabel.grid(column = 0, row = 17, sticky = "E")
dexText = tk.Entry()
dexText.insert(0, "Dex")
dexText.grid(column=1, row = 17, sticky = "W")

conLabel = tk.Label(text = "Constitution:")
conLabel.grid(column = 0, row = 18, sticky = "E")
conText = tk.Entry()
conText.insert(0, "Con")
conText.grid(column=1, row = 18, sticky = "W")

intLabel = tk.Label(text = "Intelligence:")
intLabel.grid(column = 0, row = 19, sticky = "E")
intText = tk.Entry()
intText.insert(0, "Int")
intText.grid(column=1, row = 19, sticky = "W")

wisLabel = tk.Label(text = "Wisdom:")
wisLabel.grid(column = 0, row = 20, sticky = "E")
wisText = tk.Entry()
wisText.insert(0, "Wis")
wisText.grid(column=1, row = 20, sticky = "W")

chrLabel = tk.Label(text = "Charisma:")
chrLabel.grid(column = 0, row = 21, sticky = "E")
chrText = tk.Entry()
chrText.insert(0, "Chr")
chrText.grid(column=1, row = 21, sticky = "W")

#Row 22
separator4 = ttk.Separator(root, orient = "horizontal")
separator4.grid(column = 0 , row = 22, columnspan = 1, sticky = "EW")
blankSpace2 = tk.Label(text = "")
blankSpace2.grid(column = 0, row = 22, sticky = "W", pady = 2)

#Row 23
equipmentLabel = tk.Label(text = " Equipment:")
equipmentLabel.grid(column = 0, row = 23, sticky = "W")

skillLabel = tk.Label(text = "Attacks, Spells, and Skills:")
skillLabel.grid(column = 1, row = 23, sticky = "W")

#Row 24
equipmentFrame = tk.Frame(root, width = 300, height = 200, pady = 5)
equipmentFrame.grid(column = 0, row = 24, sticky = "W")
equipmentFrame.grid_propagate(False)
equipmentText = tk.Text(equipmentFrame)
equipmentText.insert("1.0", "Equipment")
equipmentText.grid(column = 0, row = 24, sticky = "W", padx = 5, pady = 5)

skillFrame = tk.Frame(root, width = 300, height = 200, pady = 5)
skillFrame.grid(column = 1, row = 24, sticky = "W")
skillFrame.grid_propagate(False)
skillText = tk.Text(skillFrame)
skillText.insert("1.0", "Attacks, Spells, Skills")
skillText.grid(column = 1, row = 24, sticky = "W", padx = 5, pady = 5)

saveCharacter = tk.Button(root, command = lambda: DDCharacterSheetLogic.save_character(root), text = "Save Character", padx = 10, pady=3)
saveCharacter.grid(column = 2, row = 24, sticky = "NSEW", padx= 5, pady = 5)
tip6 = Balloon(root)
tip6.bind_widget(saveCharacter, balloonmsg = "Save current fields to a .csv file.")
