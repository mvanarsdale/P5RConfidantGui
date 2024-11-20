import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# puts info of the confidant buttons on the window 
def openConfidantScreen():
    # first row of characters
    profilesOnScreen("morganaPor.png", 0, 0, command = openMorganaWindow)
    profilesOnScreen("ryujiPor.png", 0, 1, command = openRyujiWindow)
    profilesOnScreen("annPor.png", 0, 2, command = openAnnWindow)
    profilesOnScreen("yusukePor.png", 0, 3, command = openYusukeWindow)
    profilesOnScreen("makotoPor.png", 0, 4, command = openMakotoWindow)
    # second row of characters 
    profilesOnScreen("futabaPor.png", 1, 0, command = openFutabaWindow)
    profilesOnScreen("haruPor.png", 1, 1, command = openHaruWindow)
    profilesOnScreen("akechiPor.png", 1, 2, command = openAkechiWindow)
    profilesOnScreen("yoshizawaPor.png", 1, 3, command = openYoshizawaWindow)
    profilesOnScreen("MarukiPor.png", 1, 4, command = openMarukiWindow)
    # third row of characters
    profilesOnScreen("igorPor.png", 2, 0, command = openigorWindow)
    profilesOnScreen("twinsPor.png", 2, 1, command = opentwinsWindow)
    profilesOnScreen("SojiroPor.png", 2, 2, command = openSojiroWindow)
    profilesOnScreen("niijima.png", 2, 3, command = openniijimaWindow)
    profilesOnScreen("hangedPor.png", 2, 4, command = openhangedWindow)
    # fourth row of characters
    profilesOnScreen("fortunePor.png", 3, 0, command = openfortuneWindow)
    profilesOnScreen("takemiPor.png", 3, 1, command = opentakemiWindow)
    profilesOnScreen("reporterPor.png", 3, 2, command = openreporterWindow)
    profilesOnScreen("teacherPor.png", 3, 3, command = openteacherWindow)
    profilesOnScreen("hifumiPor.png", 3, 4, command = openhifumiWindow)
    # fifth row of characters
    profilesOnScreen("kidPor.png", 4, 0, command = openkidWindow)
    profilesOnScreen("mishimaPor.png", 4, 1, command = openmishimaWindow)
    profilesOnScreen("yoshidaPor.png", 4, 2, command = openyoshidaWindow)
    
    closeButton = Button(text="Close", bg="black", command=confidantWindow.destroy)
    closeButton.place(x=400,y=550)
    
    ### maybe add a close button at bottom of the gui ##
    
    
# subroutine to put confidant buttons on window 
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

# subroutine for the confidants individual info windows 
def openingPersonaHolderWindow(screenTitle, name, arcana, location, sq_image_path, rec_image_path):
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
    
    # the rectangle image
    character_rt_Image = Image.open(rec_image_path)
    resize_rt = character_rt_Image.resize((500, 200))
    rt = ImageTk.PhotoImage(resize_rt)
    characterRectangle = tk.Label(characterWindow, image=rt)
    characterRectangle.Image = rt
    characterRectangle.pack(side="bottom")
    
#     # canvas for label
#     canvas = Frame(width=250, height=200, bg="#FF0505" )
    
    # Info label
    characterInfo = Label(characterWindow, text=f"Name: {name}\nArcana: {arcana}\nLocation: {location}", font=("Arial", 18), fg="black",bg="#FF0505")
    characterInfo.place(x=20,y=30)
    
    # back button to destory info window and return to confidant screen
    backButton = Button(characterWindow, text="Back", fg="black", command = characterWindow.destroy)
    backButton.place(x=75,y=150)
 

# opening confidant windows
### first row ####
def openMorganaWindow():
    openingPersonaHolderWindow("Morgana Info", "Morgana", "Magican", "With MC", "morgana.png", "morganaRec.png")
def openRyujiWindow():
    openingPersonaHolderWindow("Ryuji Info", "Ryuji", "Chariot", "Shujin", "ryuji.png", "ryujiRec.png")
def openAnnWindow():
    openingPersonaHolderWindow("Ann Info", "Ann", "Lovers", "Underground Mall", "ann.png", "annRec.png")
def openYusukeWindow():
    openingPersonaHolderWindow("Yusuke Info", "Yusuke", "Emperor", "Underground walkway", "yusuke.png", "yusukeRec.png")
def openMakotoWindow():
    openingPersonaHolderWindow("Makoto Info", "Makoto", "Priestess", "Shujin", "makoto.png", "makotoRec.png")

### second row ###
def openFutabaWindow():
    openingPersonaHolderWindow("Futaba Info", "Futaba", "Hermit", "Outside Leblanc", "futaba.png", "futabaRec.png")
def openHaruWindow():
    openingPersonaHolderWindow("Haru Info", "Haru", "Empress", "Shujin Rooftop", "haru.png", "haruRec.png")
def openAkechiWindow():
    openingPersonaHolderWindow("Akechi Info", "Akechi", "Justice", "Penguin Sniper", "akechi.png", "akechiRec.png")
def openYoshizawaWindow():
    openingPersonaHolderWindow("Yoshizawa Info", "Yoshizawa", "Faith", "Shujin", "yoshizawa.png", "yoshizawaRec.png")
def openMarukiWindow():
    openingPersonaHolderWindow("Maruki Info", "Maruki", "Councillor", "Shujin", "maruki.png", "marukiRec.png")

### third row ####
def openigorWindow():
    openingPersonaHolderWindow("Igor Info", "Igor", "Fool", "Velvet Room", "igor.png", "igorRec.png")
def opentwinsWindow():
    openingPersonaHolderWindow("Twins Info", "Caroline and Justine", "Strength", "Velvet Room", "twins.png", "twinsRec.png")
def openSojiroWindow():
    openingPersonaHolderWindow("Sojiro Info", "Sojiro Sakura", "Hermit", "Cafe Leblanc", "sojiro.png", "sojiroRec.png")
def openniijimaWindow():
    openingPersonaHolderWindow("Niijima Info", "Sei Niijima", "Judge", "N/A", "niijimaPor.png", "niijimaRec.png")
def openhangedWindow():
    openingPersonaHolderWindow("Iwai Info", "Iwai", "Hnaged Man", "Airsoft Shop", "iawi.png", "iawiRec.png")
    
### fourth row ####
def openfortuneWindow():
    openingPersonaHolderWindow("Chihya Info", "Chihya", "Fortune", "Shinjuku", "futaba.png", "futabaRec.png")
def opentakemiWindow():
    openingPersonaHolderWindow("Takemi Info", "Takemi", "Death", "Back Alley", "futaba.png", "futabaRec.png")
def openreporterWindow():
    openingPersonaHolderWindow("Ohya Info", "Ohya", "Devil", "Cross Roads", "futaba.png", "futabaRec.png")
def openteacherWindow():
    openingPersonaHolderWindow("Kawakami Info", "Kawakami", "Tempress", "On yellow pay phone", "futaba.png", "futabaRec.png")
def openhifumiWindow():
    openingPersonaHolderWindow("Hifumi Info", "Hifumi", "Star", "Church", "futaba.png", "futabaRec.png")
    
### fifth ####
def openkidWindow():
    openingPersonaHolderWindow("Hifumi Info", "Hifumi", "Tower", "Akihabara Arcade", "futaba.png", "futabaRec.png")
def openmishimaWindow():
    openingPersonaHolderWindow("Mishima Info", "Mishima", "Moon", "Akihabara", "futaba.png", "futabaRec.png")
def openyoshidaWindow():
    openingPersonaHolderWindow("Yoshida Info", "Yoshida", "Sun", "Shibuya Square", "futaba.png", "futabaRec.png")
 
# main program
# create the window 
confidantWindow = tk.Tk()
confidantWindow.title("Confidant Tracker")
confidantWindow.geometry("650x600")
confidantWindow.config(bg="#FF0505")


confidantWindow.rowconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)
confidantWindow.columnconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)


openConfidantScreen()


 

confidantWindow.mainloop()
    
    
    
    