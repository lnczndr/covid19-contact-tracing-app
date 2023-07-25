# LANA CAZANDRA U. LEGASPI
# BSCPE 1-5

# COVID-19 CONTACT TRACING APP

# IMPORTING TKINTER
import tkinter as tk
from tkinter import ttk

# MAKING A WINDOW
root = tk.Tk()
root.geometry ("870x500")

# GIVING TITLE TO THE WINDOW
root.title ("COVID-19 CONTACT TRACING APP")

# MAKING LABEL
title_label = tk.Label(root, text="COVID-19 CONTACT TRACING APP", font= ("Times New Roman", 18, 'bold'))
title_label.pack(padx=20)

instruction_label = tk.Label(root, text = "NOTE: Please fill up the details needed for contact tracing", font= ("Cambria", 12, 'italic'))
instruction_label.pack()

respondent_info = tk.Label(root,text="RESPONDENT'S PERSONAL INFORMATION:",font=('Cambria', 10, 'bold'))
respondent_info.place (x=10, y=60)

# MAKING ENTRY TEXTBOX FOR RESPONDENT'S PERSONAL INFORMATION
# NAME:
# SURNAME
respondent_surname = tk.Label (root, text="Surname: ", font=('Cambria', 10))
respondent_surname.place (x=10, y= 90)
respondent_surname = tk.Entry (root)
respondent_surname.place (width= 175, x=70, y= 90)

# FIRST NAME
respondent_fn = tk.Label (root, text="First Name: ", font=('Cambria', 10))
respondent_fn.place (x=270, y= 90)
respondent_fn = tk.Entry (root)
respondent_fn.place (width= 175, x=350, y= 90)

# MIDDLE NAME
respondent_mn = tk.Label (root, text="Middle Name: ", font=('Cambria', 10))
respondent_mn.place (x=550, y= 90)
respondent_mn = tk.Entry (root)
respondent_mn.place (width= 175, x=640, y= 90)

# GENDER
respondent_gender = tk.Label (root, text="Gender: ", font= ("Cambria",10))
respondent_gender.place (x=10, y=120)
respondent_gender = ttk.Combobox(root, values=("Male", "Female", "Others", "Prefer not to say"))
respondent_gender.place (width= 115, x=70, y=120)

# AGE
respondent_age = tk.Label (root, text="Age: ", font= ("Cambria",10))
respondent_age.place (x=200, y=120)
respondent_age = tk.Entry(root)
respondent_age.place (width= 100, x=235, y=120)

# CONTACT NUMBER

respondent_contact = tk.Label (root, text="Contact Number: ", font= ("Cambria",10))
respondent_contact.place (x=350, y=120)
respondent_contact = tk.Entry(root)
respondent_contact.place (width= 130, x=450, y=120)

root.mainloop()