import re
import tkinter as tk
from tkinter import ttk


# set up root window
root = tk.Tk()
root.geometry('800x600')
root.state('zoomed')

def regexSearch():
    pass

# make the search bar
searchText = tk.StringVar()

searchBar = ttk.Labelframe(root, text='RegEx Search:')
searchBar.place(relx=0.3, y=0, relwidth=0.7, relheight=0.075)

searchEntry = ttk.Entry(searchBar, textvariable=searchText)
searchEntry.place(relx=0.005, y=0, relheight=0.9, relwidth=0.795)

startSearchButton = ttk.Button(searchBar, command=regexSearch, text='Search')
startSearchButton.place(relx=0.825, y=0, relheight=0.9, relwidth=0.15)


# options panel
optionsPanel = ttk.Labelframe(root, text='Filter Options')
optionsPanel.place(x=0, y=0, relwidth=0.3, relheight=1)

twosTo48List = [str(i) for i in range(49)]
pinCountChooser = ttk.Spinbox(optionsPanel, increment=2, values=twosTo48List)
pinCountChooser.place(relx=0.1, rely=0.5, relwidth=0.3)


# Results panel
resultsPanel = ttk.Labelframe(root, text=f'0 Results')
resultsPanel.place(relx=0.3, rely=0.075, relwidth=0.7, relheight=0.925)

root.mainloop()
