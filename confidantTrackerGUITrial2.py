import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# confident screen
def openConfidantScreen():
    profilesOnScreen("morganaPor.png", 0, 0, command = openMorganaWindow)
    profilesOnScreen("ryujiPor.png", 0, 1, command = openRyujiWindow)
    profilesOnScreen("annPor.png", 0, 2, command = openAnnWindow)
    profilesOnScreen("yusukePor.png", 0, 3, command = openYusukeWindow)
    profilesOnScreen("makotoPor.png", 0, 4, command = openMakotoWindow)
    
    profilesOnScreen("futabaPor.png", 1, 0, command = openFutabaWindow)
    profilesOnScreen("haruPor.png", 1, 1, command = openHaruWindow)
    profilesOnScreen("akechiPor.png", 1, 2, command = openAkechiWindow)
    profilesOnScreen("yoshizawaPor.png", 1, 3, command = openYoshizawaWindow)
    

def profilesOnScreen(CharPortrait, row, column, command):
    Charimage = Image.open(CharPortrait)
    CharPor_resized = Charimage.resize((100, 100))  # Set the desired size here
    CharPor = ImageTk.PhotoImage(CharPor_resized)

    CharacterPortrait = Button(image=CharPor, command=command)
    CharacterPortrait.image = CharPor
    CharacterPortrait.grid(row=row,
                            column=column,
                            columnspan = 1,
                            rowspan = 1,
                            sticky="n",
                            ipadx=0,
                            )
    
def openingPersonaHolderWindow(screenTitle, name, codename, arcana, location, sq_image_path, rec_image_path):
    # create the window
    characterWindow = Toplevel(confidantWindow)
    # name the window
    characterWindow.title=(screenTitle)
    # size of new window
    characterWindow.geometry("500x400")
    # change color of window
    characterWindow.config(bg="#FF0505")
    
    
    # the square portraits
    character_sq_Image = Image.open(sq_image_path)
    resize_sq = character_sq_Image.resize((250, 200))
    sq = ImageTk.PhotoImage(resize_sq)
    
    characterSquare = tk.Label(characterWindow, image=sq)
    characterSquare.Image = sq
    characterSquare.pack(anchor = "ne")
    
    # the rec image
    character_rt_Image = Image.open(rec_image_path)
    resize_rt = character_rt_Image.resize((500, 200))
    rt = ImageTk.PhotoImage(resize_rt)
    
    characterRectangle = tk.Label(characterWindow, image=rt)
    characterRectangle.Image = rt
    characterRectangle.pack(side="bottom")
    
    # canvas for label
    canvas = Frame(width=250, height=200, bg="#FF0505" )
    
    # Info label
    characterInfo = Label(characterWindow, text=f"Name: {name}\nCodename: {codename}\nArcana: {arcana}\nLocation: {location}", font=("Arial", 18), fg="black",bg="#FF0505")
    characterInfo.place(x=20,y=30)
    
    # back button
    backButton = Button(characterWindow, text="Back", fg="black", command = characterWindow.destroy)
    backButton.place(x=75,y=150)
 

# opening confidant windows
def openMorganaWindow():
    openingPersonaHolderWindow("Morgana Info", "Morgana", "Mona", "Magican", "With MC", "morgana.png", "morganaRec.png")
def openRyujiWindow():
    openingPersonaHolderWindow("Ryuji Info", "Ryuji", "Skull", "Chariot", "Shujin", "ryuji.png", "ryujiRec.png")
def openAnnWindow():
    openingPersonaHolderWindow("Ann Info", "Ann", "Panther", "Lovers", "Underground Mall", "ann.png", "annRec.png")
def openYusukeWindow():
    openingPersonaHolderWindow("Yusuke Info", "Yusuke", "Fox", "Emperor", "Underground walkway", "yusuke.png", "yusukeRec.png")
def openMakotoWindow():
    openingPersonaHolderWindow("Makoto Info", "Makoto", "Persona", "Priestess", "Shujin", "makoto.png", "makotoRec.png")
### second row ###
def openFutabaWindow():
    openingPersonaHolderWindow("Futaba Info", "Futaba", "Orcle", "Hermet", "Lablanc", "futaba.png", "futabaRec.png")
def openHaruWindow():
    openingPersonaHolderWindow("Haru Info", "Haru", "Noir", "Empress", "Shujin Rooftop", "haru.png", "haruRec.png")
def openAkechiWindow():
    openingPersonaHolderWindow("Akechi Info", "Akechi", "Crow", "Justice", "Shinjuku", "akechi.png", "akechiRec.png")
def openYoshizawaWindow():
    openingPersonaHolderWindow("Yoshizawa Info", "Yoshizawa", "Violet", "Faith", "Shujin", "yoshizawa.png", "yoshizawaRec.png")

    
# main program
confidantWindow = tk.Tk()
confidantWindow.title("Confidant Tracker")
confidantWindow.geometry("650x600")  


confidantWindow.rowconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)
confidantWindow.columnconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)

openConfidantScreen()


 

confidantWindow.mainloop()
    
    
    
    