import sqlite3
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

conn = sqlite3.connect('music.sqlite')


class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        # tkinter.Listbox.__init__(self, window, **kwargs)  # Python 2
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        # tkinter.Listbox.grid(self, row=row, column=column, sticky=sticky, rowspan=rowspan,
        #  **kwargs)  # Python 2
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self.config(yscrollcommand=self.scrollbar.set)


class DataListBox(Scrollbox):

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        # Scrollbox.__init__(self, window, **kwargs)  # Python 2
        super().__init__(window, **kwargs)

        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.link_field = None
        self.linked_box = None
        self.link_to_table = None

        self.bind('<<ListboxSelect>>', self.on_select)

        self.sql_select = "SELECT " + self.table + '.' + self.field + ", " + self.table + "._id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + self.table + '.' + ','.join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def link(self, link_to_box, link_field, link_to_table):
        self.linked_box = link_to_box
        link_to_box.link_field = link_field
        self.link_to_table = link_to_table

    def requery(self, link_value=None):
        if link_value and self.link_field:
            sql_link = self.sql_select + ' , ' + self.link_to_table + ' WHERE ' + self.table + \
                       '.' + self.link_field + ' = ' + self.link_to_table + '._id' + ' = ?' + self.sql_sort
            print(sql_link, (link_value,))
            # self.cursor.execute(sql_link, (link_value,))
        else:
            print(self.sql_select + self.sql_sort)      # TODO delete this line
            self.cursor.execute(self.sql_select + self.sql_sort)

        # clear the listbox contents before re-loading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

        if self.linked_box:
            self.linked_box.clear()

    def on_select(self, event):
        if self.linked_box:
            print(self is event.widget)
            index = self.curselection()[0]
            value = self.get(index),

            # get the artist ID from the database row
            link_id = self.cursor.execute(self.sql_select + ' WHERE ' + self.field + '=?', value).fetchone()[1]
            print(link_id)
            self.linked_box.requery(link_id)


    # def get_songs(self, event):
    #     lb = event.widget
    #     index = int(lb.curselection()[0])
    #     album_name = lb.get(index),
    #
    #     # get the artist ID from the database row
    #     album_id = conn.execute(self.sql_select + ' WHERE ' + self.field + '=?', value).fetchone()[1]
    #     alist = []
    #     for x in conn.execute("SELECT songs.title FROM songs WHERE songs.album=? ORDER BY songs.track", album_id):
    #         alist.append(x[0])
    #     songLV.set(tuple(alist))


mainWindow = tkinter.Tk()
mainWindow.title('Music DB Browser')
mainWindow.geometry('1024x768')

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)    # spacer column on right

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# ===== labels =====
tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

# ===== Artists Listbox =====
artistList = DataListBox(mainWindow, conn, "artists", "name")
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artistList.config(border=2, relief='sunken')

artistList.requery()
# artistList.bind('<<ListboxSelect>>', DataListBox.on_select)


# ===== Albums Listbox =====
albumLV = tkinter.Variable(mainWindow)
# albumLV.set(("Choose an artist",))
albumList = DataListBox(mainWindow, conn, "albums", "name", sort_order=("name",))
# albumList.requery()
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(border=2, relief='sunken')

# albumList.bind('<<ListboxSelect>>', DataListBox.get_songs)
artistList.link(albumList, 'artist', 'albums')

# ===== Songs Listbox =====
songLV = tkinter.Variable(mainWindow)
# songLV.set(("Choose an album",))
songList = DataListBox(mainWindow, conn, "songs", "title", ("track", "title"))
# songList.requery()
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.config(border=2, relief='sunken')

albumList.link(songList, 'album', 'songs')

# ===== Main loop =====
testList = range(0, 100)
albumLV.set(('Choose an artist',))
mainWindow.mainloop()
print("closing database connection")
conn.close()
