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
respondent_info = tk.Label(root, text="COVID-19 CONTACT TRACING APP", font= ("Times New Roman", 18))
respondent_info.pack(padx=20, pady=20)

root.mainloop()