# LANA CAZANDRA U. LEGASPI
# BSCPE 1-5

# COVID-19 CONTACT TRACING APP

# IMPORTING TKINTER
import tkinter as tk
from tkinter import ttk

# MAKING A WINDOW
root = tk.Tk()
root.geometry ("850x650")

# GIVING TITLE TO THE WINDOW
root.title ("COVID-19 CONTACT TRACING APP")

# MAKING TITLE LABEL
title_label = tk.Label(root, text="COVID-19 CONTACT TRACING APP", font= ("Times New Roman", 18, 'bold'))
title_label.pack(padx=20)

# MAKING INSTRUCTION LABEL
instruction_label = tk.Label(root, text = "NOTE: Please fill up the details needed for contact tracing", font= ("Cambria", 12, 'italic'))
instruction_label.pack()

# ADDING DIVIDER FOR DESIGN
divider1 = tk.Label (root,text="_" * 141, font=('Cambria',12))
divider1.place (y=75)

# MAKING LABEL FOR PERSONAL INFORMATION CATEGORY
respondent_info = tk.Label(root,text="RESPONDENT'S PERSONAL INFORMATION:",font=('Cambria', 12, 'bold'))
respondent_info.place (x=10, y=80)

# MAKING ENTRY TEXTBOX FOR RESPONDENT'S PERSONAL INFORMATION
# NAME:SURNAME
respondent_surname = tk.Label (root, text="Surname: ", font=('Cambria', 10))
respondent_surname.place (x=10, y= 110)
respondent_surname = tk.Entry (root)
respondent_surname.place (width= 175, x=80, y= 110)

# NAME:FIRST NAME
respondent_fn = tk.Label (root, text="First Name: ", font=('Cambria', 10))
respondent_fn.place (x=270, y= 110)
respondent_fn = tk.Entry (root)
respondent_fn.place (width= 175, x=350, y= 110)

# NAME:MIDDLE NAME
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
divider2 = tk.Label (root,text="_" * 141, font=('Cambria',12))
divider2.place (y=230)

# COVID-19 INFORMATION
# ADDING DIVIDER FOR DESIGN
divider3 = tk.Label (root,text="_" * 141, font=('Cambria',12))
divider3.place (y=280)

# MAKING LABEL FOR VACCINATION INFORMATION CATEGORY
vacc_info = tk.Label(root,text="VACCINATION INFORMATION:",font=('Cambria', 12, 'bold'))
vacc_info.place (x=10, y=285)

# NOTE
vacc_note = tk.Label(root,text="(Questions refer to the past 14 days)", font=("Cambria", 8, 'italic'))
vacc_note.place(x=240, y=289)

# VACCINATION STATUS
vacc_stat = tk.Label (root, text="Status: ", font= ("Cambria",10))
vacc_stat.place (x=10, y=315)
vacc_stat = ttk.Combobox(root, values=("Not Yet", "First Dose", "Second Dose", "First Booster Shot", "Second Booster Shot"))
vacc_stat.place (width= 135, x=55, y=315)

# CONTACT WITH PROBABLE CASES
contact = tk.Label (root, text="Have you had contact with a probable case?: ", font= ("Cambria",10))
contact.place (x=195, y=315)
contact = ttk.Combobox(root, values=("Yes", "No"))
contact.place (width= 50, x=445, y=315)

# RECENT COVID-19 TEST RESULT
test_result = tk.Label (root, text="Have you been tested for COVID-19?: ", font= ("Cambria",10))
test_result.place (x=500, y=315)
test_result = ttk.Combobox(root, values=("Yes - POSITIVE", "Yes - NEGATIVE","Yes - PENDING", "No"))
test_result.place (width= 100, x=710, y=315)

# SYMPTOMS
divider4 = tk.Label (root,text="_" * 141, font=('Cambria',12))
divider4.place (y=340)
symptom_label = ttk.Label (root, text="Symptoms: ", font=("Cambria",12))
symptom_label.place (x=10, y=345)

# SYMPTOM 1: FEVER
symptoms1 = tk.IntVar()
symptom1 = tk.Checkbutton(root, text="Fever", font=("Cambria",11), variable=symptoms1, onvalue='/', offvalue='x')
symptom1.place (x=10, y=370)

# SYMPTOM 2: COUGH
symptoms2 = tk.IntVar()
symptom2 = tk.Checkbutton(root, text="Cough", font=("Cambria",11), variable=symptoms2, onvalue='/', offvalue='x')
symptom2.place (x=100, y=370)

# SYMPTOM 3: COLD
symptoms3 = tk.IntVar()
symptom3 = tk.Checkbutton(root, text="Colds", font=("Cambria",11), variable=symptoms3, onvalue='/', offvalue='x')
symptom3.place (x=190, y=370)

# SYMPTOM 4: MUSCLE/BODY PAIN
symptoms4 = tk.IntVar()
symptom4 = tk.Checkbutton(root, text="Muscle/Body Pains", font=("Cambria",11), variable=symptoms4, onvalue='/', offvalue='x')
symptom4.place (x=280, y=370)

# SYMPTOM 5: SORE THROAT
symptoms5 = tk.IntVar()
symptom5 = tk.Checkbutton(root, text="Sore Throat", font=("Cambria",11), variable=symptoms5, onvalue='/', offvalue='x')
symptom5.place (x=450, y=370)

# SYMPTOM 6: DIARRHEA
symptoms6 = tk.IntVar()
symptom6 = tk.Checkbutton(root, text="Diarrhea", font=("Cambria",11), variable=symptoms6, onvalue='/', offvalue='x')
symptom6.place (x=580, y=370)

# SYMPTOM 7: HEADACHE
symptoms7 = tk.IntVar()
symptom7 = tk.Checkbutton(root, text="Headache", font=("Cambria",11), variable=symptoms7, onvalue='/', offvalue='x')
symptom7.place (x=680, y=370)

# SYMPTOM 8: SHORTNESS OF BREATH
symptoms8 = tk.IntVar()
symptom8 = tk.Checkbutton(root, text="Shortness of Breath", font=("Cambria",11), variable=symptoms8, onvalue='/', offvalue='x')
symptom8.place (x=10, y=400)

# SYMPTOM 9: DIFFICULTY OF BREATHING
symptoms9 = tk.IntVar()
symptom9 = tk.Checkbutton(root, text="Difficulty of Breathing", font=("Cambria",11), variable=symptoms9, onvalue='/', offvalue='x')
symptom9.place (x=175, y=400)

# SYMPTOM 10: LOSS OF TASTE
symptoms10 = tk.IntVar()
symptom10 = tk.Checkbutton(root, text="Loss of Taste", font=("Cambria",11), variable=symptoms10, onvalue='/', offvalue='x')
symptom10.place (x=360, y=400)

# SYMPTOM 11: LOSS OF SMELL
symptoms11 = tk.IntVar()
symptom11 = tk.Checkbutton(root, text="Loss of Smell", font=("Cambria",11), variable=symptoms11, onvalue='/', offvalue='x')
symptom11.place (x=495, y=400)

# NO SYMPTOMS
nosymptoms = tk.IntVar()
nosymptom = tk.Checkbutton(root, text="None of the Above", font=("Cambria",11), variable=nosymptoms, onvalue='/', offvalue='x')
nosymptom.place (x=625, y=400)

# DIVIDER
divider5 = tk.Label (root,text="_" * 141, font=('Cambria',12))
divider5.place (y=430)

# ADDING DIVIDER FOR DESIGN
divider6 = tk.Label (root,text="_" * 141, font=('Cambria',12))
divider6.place (y=480)

# MAKING LABEL FOR CONTACT INFORMATION CATEGORY
contact_info = tk.Label(root,text="CONTACT INFORMATION:",font=('Cambria', 12, 'bold'))
contact_info.place (x=10, y=485)

# NAME:SURNAME
contact_surname = tk.Label (root, text="Surname: ", font=('Cambria', 10))
contact_surname.place (x=10, y= 525)
contact_surname = tk.Entry (root)
contact_surname.place (width= 175, x=80, y= 525)

# NAME:FIRST NAME
contact_fn = tk.Label (root, text="First Name: ", font=('Cambria', 10))
contact_fn.place (x=270, y= 525)
contact_fn = tk.Entry (root)
contact_fn.place (width= 175, x=350, y= 525)

# NAME:MIDDLE NAME
contact_mn = tk.Label (root, text="Middle Name: ", font=('Cambria', 10))
contact_mn.place (x=550, y= 525)
contact_mn = tk.Entry (root)
contact_mn.place (width= 175, x=640, y= 525)
 
# CONTACT NUMBER
contact_number = tk.Label (root, text="Contact Number: ", font=('Cambria', 10))
contact_number.place (x=10, y= 555)
contact_number = tk.Entry (root)
contact_number.place (width= 175, x=115, y= 555)

# EMAIL
contact_email = tk.Label (root, text="Email: ", font=('Cambria', 10))
contact_email.place (x=305, y= 555)
contact_email = tk.Entry (root)
contact_email.place (width= 175, x=350, y= 555)

# RELATIONSHIP
contact_rela = tk.Label (root, text="Relationship: ", font=('Cambria', 10))
contact_rela.place (x=550, y= 555)
contact_rela = tk.Entry (root)
contact_rela.place (width= 175, x=640, y= 555)

# ADDING DIVIDER FOR DESIGN
divider7 = tk.Label (root,text="_" * 141, font=('Cambria',12))
divider7.place (y=580)

# MAKING SUBMIT BUTTON
submit_button = tk.Button (root, text="Submit Entry", font=("Cambria",12)).pack(side=tk.BOTTOM, pady=10)

# DEFINING SUBMIT FUNCTIONS
def submit(self):
    # PERSONAL INFORMATION
    getsurname=respondent_surname.get()
    getfirstname=respondent_fn.get()
    getmiddlename=respondent_mn.get()
    getgender=respondent_gender.get()
    getage=respondent_age.get()
    getr_email=respondent_email.get()
    gethousenum=respondent_housenum.get()
    getbarangay=respondent_barangay.get()
    getmunicipality=respondent_municipality.get()
    getpostal=respondent_postal.get()
    getprovince=respondent_province.get()
    getregion=respondent_region.get()

    # VACCINATION INFORMATION
    getstatus=vacc_stat.get()
    getcontact=contact.get()
    gettest_result=test_result.get()
    getsymptom1=symptoms1.get()
    getsymptom2=symptoms2.get()
    getsymptom3=symptoms3.get()
    getsymptom4=symptoms4.get()
    getsymptom5=symptoms5.get()
    getsymptom6=symptoms6.get()
    getsymptom7=symptoms7.get()
    getsymptom8=symptoms8.get()
    getsymptom9=symptoms9.get()
    getsymptom10=symptoms10.get()
    getsymptom11=symptoms11.get()
    getnosymptom=nosymptoms.get()

    # CONTACT INFORMATION
    getcontact_surname=contact_surname.get()
    getcontact_fn=contact_fn.get()
    getcontact_mn=contact_mn.get()
    getcontact_number=contact_number.get()
    getcontact_email=contact_email.get()
    getcontact_rela=contact_rela.get()

    # CSV LABEL
    csvlabel=["Surname", "First Name", "Middle Name", "Gender", "Age", "E-mail", "Bldg/House No.", "Barangay", "Municipality", "Postal", "Province", "Region", "Vaccination Status", "Probable Contact", "Covid Test Result", "Fever", "Cough", "Colds", "Muscle/Body Pains", "Sore Throat", "Diarrhea", "Headache", "Shortness of Breath", "Difficulty of Breathing", "Loss of Taste", "Loss of Taste", "Loss of Smell", "None", "Contact Surname", "Contact First Name", "Contact Middle Name", "Contact Number", "Contact Email", "Contact Re;atopn"]
    csvinput=[getsurname, getfirstname, getmiddlename ,getgender, getage, getr_email, gethousenum, getbarangay, getmunicipality, getpostal, getprovince, getregion, getstatus, getcontact, gettest_result, getsymptom1, getsymptom2, getsymptom3, getsymptom4, getsymptom5, getsymptom6, getsymptom7, getsymptom8, getsymptom9, getsymptom10, getsymptom11, getnosymptom, getcontact,getcontact_surname, getcontact_fn,getcontact_mn, getcontact_number, getcontact_email, getcontact_rela]

root.mainloop()