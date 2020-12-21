import sqlite3
import tkinter

db = sqlite3.connect('music.sqlite')

# ====== Main Window ======
mainWindow = tkinter.Tk()
mainWindow.title('Jukebox')
mainWindow.geometry('1024x768')

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# ====== Labels ======
tkinter.Label(mainWindow, text='Artist').grid(column=0, row=0)
tkinter.Label(mainWindow, text='Albums').grid(column=1, row=0)
tkinter.Label(mainWindow, text='Songs').grid(column=2, row=0)

# ====== Artist ======
artistList = tkinter.Listbox(mainWindow)
artistListVariable = tkinter.Variable(mainWindow)
artistList.grid(row=1, column=0, rowspan=2, columnspan=1, sticky='nsew', padx=30)

for row in db.execute('SELECT artists.name FROM artists ORDER BY artists.name')
    artistList.insert(tkinter.END, row[0])

# ====== Albums ======
albumList = tkinter.Listbox(mainWindow)
albumListVariable = tkinter.Variable(mainWindow)
albumList.grid(row=1, column=1, rowspan=2, columnspan=1, sticky='nsew', padx=30)

# ====== Songs ======
songList = tkinter.Listbox(mainWindow)
songListVariable = tkinter.Variable(mainWindow)
songList.grid(row=1, column=2, rowspan=2, columnspan=1, sticky='nsew', padx=30)



mainWindow.mainloop()
albumListVariable.set()
db.close()