# LANA CAZANDRA U. LEGASPI
# BSCPE 1-5

# COVID-19 CONTACT TRACING APP

# IMPORTING TKINTER
import tkinter as tk
from tkinter import ttk

# MAKING A WINDOW
root = tk.Tk()
root.geometry ("850x500")

# GIVING TITLE TO THE WINDOW
root.title ("COVID-19 CONTACT TRACING APP")

# MAKING A LABEL
title_label = tk.Label(root, text="COVID-19 CONTACT TRACING APP", font= ("Times New Roman", 18))
title_label.pack(padx=20)

instruction_label = tk.Label(root, text = "NOTE: Please fill up the details needed for contact tracing", font= ("Cambria", 12))
instruction_label.pack()


root.mainloop()