import tkinter as tk
from tkinter import filedialog

def dialogSelectFiles(initialdir=None):
	root = tk.Tk()
	root.withdraw()
	files = filedialog.askopenfilenames(initialdir=initialdir, multiple=True)
	return list(files)
