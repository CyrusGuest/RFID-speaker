import spotipy
import threading
from playsound import playsound
from tkinter import *
from tkinter import ttk
from spotipy.oauth2 import SpotifyOAuth

scope = "streaming"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope, client_id='3993b982d9df4af19743bbdbaef21b52', client_secret='e524990dac2244bf80912ca4d5a39927', redirect_uri='http://google.com/'))
songsNameDictionary = {
    "0005634691": "Jack Johnson - Upside Down",
    "0015442236": "Hozier - From Eden"
}

songsSpotifyIDDictionary = {
    '0005634691': "spotify:track:6shRGWCtBUOPFLFTTqXZIC",
    '0015442236': "spotify:track:5aRZk9oWIYUB5alrTs8TTV"
}


def playSong(*args):
    threading.Thread(target=playsound, args=('beep.mp3',), daemon=True).start()
    songID = songsSpotifyIDDictionary[cardID.get()]
    cardID.set('')
    uris = [songID]
    sp.start_playback(
        uris=uris)


root = Tk()
root.title("RFID Reader")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

currentSong = StringVar()
cardID = StringVar()
cardID_entry = ttk.Entry(mainframe, width=7, textvariable=cardID)
cardID_entry.grid(column=2, row=1, sticky=(W, E), columnspan=3)

ttk.Label(mainframe, text="Card ID: ").grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text="Play song", command=playSong).grid(
    column=1, row=2, columnspan=4)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", playSong)

root.mainloop()
