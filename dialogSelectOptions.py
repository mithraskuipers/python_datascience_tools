import tkinter as tk


def choose_options(options):
    """
    Prompts the user to choose one or more options from a list using a Tkinter GUI.

    Args:
        options (list): A list of options to choose from.

    Returns:
        list: A list of the chosen options.
    """
    chosen_options = []

    def submit_choices():
        nonlocal chosen_options
        for i in listbox.curselection():
            chosen_options.append(options[i])
        top.destroy()

    top = tk.Toplevel()
    top.title("Choose options")

    label = tk.Label(top, text="Please choose one or more options:")
    label.pack()

    listbox = tk.Listbox(top, selectmode=tk.MULTIPLE)
    for option in options:
        listbox.insert(tk.END, option)
    listbox.pack()

    button_ok = tk.Button(top, text="OK", command=submit_choices)
    button_ok.pack(side=tk.LEFT)

    button_cancel = tk.Button(top, text="Cancel", command=top.destroy)
    button_cancel.pack(side=tk.RIGHT)

    top.grab_set()
    top.focus_set()

    top.wait_window()

    return (chosen_options)