import tkinter as tk
from tkinter import filedialog

def dialogBrowseDir(title):
	root = tk.Tk()
	root.withdraw()
	assdir = tk.filedialog.askdirectory(initialdir='.', title=title)
	root.destroy()
	return (assdir)