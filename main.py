from tkinter import *
from tkinter import messagebox as mb

import requests
import json

def extract_lyrics():
    global artist, song
    artist_name = str(artist.get())
    song_name = str(song.get()).lower()
    link = 'https://api.lyrics.ovh/v1/'+artist_name.replace(' ', '%20')+'/'+song_name.replace(' ', '%20')
    req = requests.get(link)
    json_data = json.loads(req.content)
    try:
        lyrics = json_data["lyrics"]
        exec("print(lyrics)")
        mb.showinfo('Lyrics printed', f"The lyrics to the song you wanted have been ectracted, and have been printed on your command terminal.")
    except:
        mb.showerror('No such song found', 'recheck the name of the artist and the song, and if it is correct, we apologise because we do not have that song available with us.')

root = Tk()
root.title("Python song extractor")
root.geometry("600x200")
root.config(bg="CadetBlue")
root.resizable(0, 0)

Label(root, text="Python Song Extractor", font=("Comic Sans MS",16, "bold" ), bg="CadetBlue").pack(side=TOP, fill=X)

Label(root, text="Enter Artist Name: ", font=("Times New Roman", 14, "bold"), bg="CadetBlue").place(x=20, y=50)
artist = StringVar()
Entry(root, width=40, textvariable=artist, font=("TImes New Roman", 14)).place(x=200, y=50)

Label(root, text="Enter the Song Name:  ", font=("Times New Roman", 14, "bold"), bg="CadetBlue").place(x=20, y=100)
song = StringVar()
Entry(root, width=40, textvariable=song, font=("Times New Roman", 14), bg="CadetBlue").place(x=200, y=100)

Button(root, text="Extract Song Lyrics", font=("Georgia", 14), command=extract_lyrics, width=15).place(x=220, y=150)

root.update()
root.mainloop()

