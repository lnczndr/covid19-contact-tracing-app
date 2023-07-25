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

# MAKING LABEL
title_label = tk.Label(root, text="COVID-19 CONTACT TRACING APP", font= ("Times New Roman", 18, 'bold'))
title_label.pack(padx=20)

instruction_label = tk.Label(root, text = "NOTE: Please fill up the details needed for contact tracing", font= ("Cambria", 12, 'italic'))
instruction_label.pack()

# MAKING BACKGROUND
frame = tk.Frame(root, width=850, height=170, bg="lightblue")
frame.place(y=70)

respondent_info = tk.Label(root,text="RESPONDENT'S PERSONAL INFORMATION:",font=('Cambria', 12, 'bold'))
respondent_info.place (x=10, y=80)

# MAKING ENTRY TEXTBOX FOR RESPONDENT'S PERSONAL INFORMATION
# NAME:
# SURNAME
respondent_surname = tk.Label (root, text="Surname: ", font=('Cambria', 10))
respondent_surname.place (x=10, y= 110)
respondent_surname = tk.Entry (root)
respondent_surname.place (width= 175, x=80, y= 110)

# FIRST NAME
respondent_fn = tk.Label (root, text="First Name: ", font=('Cambria', 10))
respondent_fn.place (x=270, y= 110)
respondent_fn = tk.Entry (root)
respondent_fn.place (width= 175, x=350, y= 110)

# MIDDLE NAME
respondent_mn = tk.Label (root, text="Middle Name: ", font=('Cambria', 10))
respondent_mn.place (x=550, y= 110)
respondent_mn = tk.Entry (root)
respondent_mn.place (width= 175, x=640, y= 110)

# GENDER
respondent_gender = tk.Label (root, text="Gender: ", font= ("Cambria",10))
respondent_gender.place (x=10, y=140)
respondent_gender = ttk.Combobox(root, values=("Male", "Female", "Others", "Prefer not to say"))
respondent_gender.place (width= 115, x=70, y=140)

# AGE
respondent_age = tk.Label (root, text="Age: ", font= ("Cambria",10))
respondent_age.place (x=200, y=140)
respondent_age = tk.Entry(root)
respondent_age.place (width= 100, x=240, y=140)

# CONTACT NUMBER
respondent_contact = tk.Label (root, text="Contact Number: ", font= ("Cambria",10))
respondent_contact.place (x=350, y=140)
respondent_contact = tk.Entry(root)
respondent_contact.place (width= 130, x=460, y=140)

# EMAIL
respondent_email = tk.Label (root, text="Email: ", font= ("Cambria", 10))
respondent_email.place(x=600, y=140)
respondent_email = tk.Entry(root)
respondent_email.place (width= 165, x=650, y=140)

# ADDRESS
# BLDG/HOUSE NUMBER
respondent_housenum = tk.Label (root, text="Bldg/House No: ", font= ("Cambria", 10))
respondent_housenum.place (x=10, y=170)
respondent_housenum = tk.Entry(root)
respondent_housenum.place (width= 170, x=120, y=170)

# BARANGAY
respondent_brgy = tk.Label (root, text="Barangay: ", font= ("Cambria", 10))
respondent_brgy.place (x=300, y=170)
respondent_brgy = tk.Entry(root)
respondent_brgy.place (width= 170, x=370, y=170)

# MUNICIPALITY
respondent_municipality = tk.Label (root, text="Municipality: ", font=("Cambria", 10))
respondent_municipality.place (x=560, y=170)
respondent_municipality = tk.Entry(root)
respondent_municipality.place (width= 165, x=650, y=170)

# POSTAL CODE
respondent_postal = tk.Label (root, text="Postal Code: ", font=("Cambria", 10))
respondent_postal.place (x=10, y=200)
respondent_postal = tk.Entry(root)
respondent_postal.place (width= 170, x=100, y=200)

# PROVINCE
respondent_province = tk.Label (root, text="Province: ", font= ("Cambria", 10))
respondent_province.place (x=300, y=200)
respondent_province = tk.Entry(root)
respondent_province.place (width= 170, x=370, y=200)

# REGION
respondent_region = tk.Label (root, text="Region: ", font=("Cambria", 10))
respondent_region.place (x=560, y=200)
respondent_region = tk.Entry(root)
respondent_region.place (width= 170, x=645, y=200)


# DIVIDER
divider = tk.Label (root,text="_" * 141, font=('Cambria',12))
divider.place (y=250)

# COVID-19 INFORMATION




root.mainloop()