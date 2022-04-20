import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image

conn = sqlite3.connect('Project_database.db')

c = conn.cursor()


def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


def Main_page():
    window1 = tk.Tk()
    window1.geometry("500x500")
    window1.title("Login screen")
    window1.resizable(False, False)
    window1.configure(bg='#c4e0eb')

    window1.iconbitmap('doctor_red.ico')

    load = Image.open("doctor.jpg")
    load = load.resize((340, 340))
    render = ImageTk.PhotoImage(load)
    img = tk.Label(window1, image=render)
    img.place(x=70, y=0)

    load1 = Image.open("hospital.png")
    load1 = load1.resize((70, 70))
    render1 = ImageTk.PhotoImage(load1)
    img1 = tk.Label(window1, image=render1, bg='#c4e0eb')
    img1.place(x=350, y=430)

    load2 = Image.open("pharmacy.png")
    load2 = load2.resize((70, 70))
    render2 = ImageTk.PhotoImage(load2)
    img2 = tk.Label(window1, image=render2, bg='#c4e0eb')
    img2.place(x=70, y=430)

    def login():
        username_v = username_f.get()
        password_v = password_f.get()
        id_v = id_f.get()

        flag = -1
        count = -1
        count_char = -1
        count_num = -1
        count_letter = -1

        if 5 < len(username_v) < 9:
            count = 0
            for x in range(len(username_v)):
                if 48 <= ord(username_v[x]) <= 57:
                    count = count+1

        if 7 < len(password_v) < 11:
            count_char = 0
            count_num = 0
            count_letter = 0
            for x in range(len(password_v)):
                if 48 <= ord(password_v[x]) <= 57:
                    count_num = count_num+1
                elif 65 <= ord(password_v[x]) <= 90 or 97 <= ord(password_v[x]) <= 122:
                    count_letter = count_letter + 1
                else:
                    count_char = count_char + 1

        if len(id_v) == 9:
            flag = 1

        if 0 <= count <= 2 and count_char > 0 and count_num > 0 and count_letter > 0 and flag == 1:
            user = conn.execute(
                    "SELECT username, password, id FROM Login WHERE username=:username AND password=:password AND "
                    "id=:id",
                    {'username': username_v, 'password': password_v, 'id': id_v})

            result = user.fetchall()

            if result:
                # opens a new page
                window1.destroy()
                add()
            else:
                tkinter.messagebox.showwarning(title="Warning", message="One or more of the fields is incorrect.")
        else:
            tkinter.messagebox.showwarning(title="Warning", message="One or more of the fields is incorrect.")

    username_l = Label(window1, text="Username: ", bg='#c4e0eb')
    username_l.place(x=150, y=350)
    password_l = Label(window1, text="Password: ", bg='#c4e0eb')
    password_l.place(x=150, y=380)
    id_l = Label(window1, text="Id: ", bg='#c4e0eb')
    id_l.place(x=150, y=410)

    username_f = Entry(window1, text="", width=16)
    username_f.place(x=220, y=352)
    password_f = Entry(window1, text="", width=16, show="*")
    password_f.place(x=220, y=382)
    id_f = Entry(window1, text="", width=16)
    id_f.place(x=220, y=412)

    login_b = tk.Button(window1, text="Login", width=12, bg='#639bc0', fg='black', command=login)
    login_b.place(x=200, y=440)

    Quit_b = tk.Button(window1, text="Quit", width=12, bg='#639bc0', fg='black', command=window1.destroy)
    Quit_b.place(x=200, y=470)

    window1.mainloop()


def add():
    window = tkinter.Tk()
    window.geometry("500x510")
    window.title("list")
    window.resizable(False, False)

    window.configure(bg='#c4e0eb')

    window.iconbitmap('doctor_red.ico')

    lable = Label(window, text="Patient name", bg='#c4e0eb')
    lable.place(x=120, y=5)
    lable1 = Label(window, text="Patient ID", bg='#c4e0eb')
    lable1.place(x=120, y=30)
    lable2 = Label(window, text="Gender", bg='#c4e0eb')
    lable2.place(x=120, y=55)
    lable3 = Label(window, text="Country", bg='#c4e0eb')
    lable3.place(x=120, y=80)
    lable4 = Label(window, text="Region", bg='#c4e0eb')
    lable4.place(x=120, y=105)
    lable5 = Label(window, text="Age", bg='#c4e0eb')
    lable5.place(x=120, y=130)
    lable6 = Label(window, text="WBC", bg='#c4e0eb')
    lable6.place(x=120, y=155)
    lable7 = Label(window, text="Neut (%)", bg='#c4e0eb')
    lable7.place(x=120, y=180)
    lable8 = Label(window, text="Lymph (%)", bg='#c4e0eb')
    lable8.place(x=120, y=205)
    lable9 = Label(window, text="RBC", bg='#c4e0eb')
    lable9.place(x=120, y=230)
    lable10 = Label(window, text="HCT (%)", bg='#c4e0eb')
    lable10.place(x=120, y=255)
    lable11 = Label(window, text="Urea", bg='#c4e0eb')
    lable11.place(x=120, y=280)
    lable12 = Label(window, text="Hb", bg='#c4e0eb')
    lable12.place(x=120, y=305)
    lable13 = Label(window, text="Creatinine", bg='#c4e0eb')
    lable13.place(x=120, y=330)
    lable14 = Label(window, text="Iron", bg='#c4e0eb')
    lable14.place(x=120, y=355)
    lable15 = Label(window, text="HDL", bg='#c4e0eb')
    lable15.place(x=120, y=380)
    lable16 = Label(window, text="Alkaline Phosphatase", bg='#c4e0eb')
    lable16.place(x=120, y=405)

    # 2 change the name
    def Patients_list():
        window2 = tk.Tk()
        window2.geometry("1490x400")
        window2.title("Patients_list")
        window2.resizable(False, False)

        window2.configure(bg='#c4e0eb')

        window2.iconbitmap('doctor_red.ico')

        top = Label(window2, text="Patient\nname", bg='#c4e0eb')
        top.place(x=30, y=5)
        top1 = Label(window2, text="Patient\nid", bg='#c4e0eb')
        top1.place(x=115, y=5)
        top2 = Label(window2, text="Gender", bg='#c4e0eb')
        top2.place(x=200, y=5)
        top3 = Label(window2, text="Country", bg='#c4e0eb')
        top3.place(x=285, y=5)
        top4 = Label(window2, text="Region", bg='#c4e0eb')
        top4.place(x=375, y=5)
        top5 = Label(window2, text="Age", bg='#c4e0eb')
        top5.place(x=470, y=5)
        top6 = Label(window2, text="WBC", bg='#c4e0eb')
        top6.place(x=555, y=5)
        top7 = Label(window2, text="Neut(%)", bg='#c4e0eb')
        top7.place(x=635, y=5)
        top8 = Label(window2, text="Lymph(%)", bg='#c4e0eb')
        top8.place(x=715, y=5)
        top9 = Label(window2, text="RBC", bg='#c4e0eb')
        top9.place(x=815, y=5)
        top10 = Label(window2, text="HCT(%)", bg='#c4e0eb')
        top10.place(x=895, y=5)
        top11 = Label(window2, text="Urea", bg='#c4e0eb')
        top11.place(x=985, y=5)
        top12 = Label(window2, text="Hb", bg='#c4e0eb')
        top12.place(x=1080, y=5)
        top13 = Label(window2, text="Creatinine", bg='#c4e0eb')
        top13.place(x=1145, y=5)
        top14 = Label(window2, text="Iron", bg='#c4e0eb')
        top14.place(x=1250, y=5)
        top15 = Label(window2, text="HDL", bg='#c4e0eb')
        top15.place(x=1340, y=5)
        top16 = Label(window2, text="Alkaline\nPhosphatase", bg='#c4e0eb')
        top16.place(x=1402, y=5)

        r_set = conn.execute("SELECT name,id,gender,country,region,age,wbc,neut,lymph,rbc,hct,urea,hb,"
                             "creatinine,iron,hdl,alkaline_phosphatase from patient")
        i = 50  # row value inside the loop
        t = 7
        for patient in r_set:
            for j in range(len(patient)):
                e = Entry(window2, width=13, fg='black')
                e.place(x=t, y=i)
                e.insert(END, patient[j])
                e["state"] = 'readonly'
                t = t + 87
            t = 7
            i = i + 25

        def after_time():
            windowmessage2.config(text="", bg='#c4e0eb')

        entry_id = tkinter.Entry(window2, width=14, fg='blue')
        entry_id.place(x=747, y=i + 12)

        def _help_():
            try:
                int(entry_id.get())
            except ValueError:
                windowmessage2.config(text="Not a valid input!", bg='#c4e0eb', fg='red')
                windowmessage2.after(2000, after_time)
                return 0

            analysis()
            window2.destroy()

        exitbutton = tkinter.Button(window2, text="Back", command=lambda: [window2.destroy(), add()], width=11,
                                    bg='#639bc0', fg='black')
        exitbutton.place(x=700, y=i + 40)

        exitbutton1 = tkinter.Button(window2, text="Analysis by Id", command=lambda: _help_()
                                     , width=11, bg='#639bc0', fg='black')
        exitbutton1.place(x=655, y=i + 10)

        windowmessage2 = Label(window2, text="", bg='#c4e0eb')
        windowmessage2.place(x=696, y=i + 70)

        def analysis():
            window3 = tk.Tk()
            window3.geometry("500x600")
            window3.title("Analysis")
            window3.resizable(False, False)
            window3.focus_force()

            window3.configure(bg='#c4e0eb')

            window3.iconbitmap('doctor_red.ico')

            val = entry_id.get()

            lable = Label(window3, text="Do you smoke?", bg='#c4e0eb')
            lable.place(x=10, y=0)
            lable1 = Label(window3, text="Are you pregnant?", bg='#c4e0eb')
            lable1.place(x=10, y=30)
            lable2 = Label(window3, text="Are you on any medications?", bg='#c4e0eb')
            lable2.place(x=10, y=60)
            lable3 = Label(window3, text="Do you consume protein in your meals?", bg='#c4e0eb')
            lable3.place(x=10, y=90)
            lable4 = Label(window3, text="Do you have high body temperatures?", bg='#c4e0eb')
            lable4.place(x=10, y=120)
            lable5 = Label(window3, text="Are you on low protein diet?", bg='#c4e0eb')
            lable5.place(x=10, y=150)
            lable7 = Label(window3, text="Have you puked or had diarrhea recently?", bg='#c4e0eb')
            lable7.place(x=10, y=180)
            lable8 = Label(window3, text="Do you eat a lot of food with protein?", bg='#c4e0eb')
            lable8.place(x=10, y=210)
            lable10 = Label(window3, text="Do you have any malnutrition disorders?", bg='#c4e0eb')
            lable10.place(x=10, y=240)

            # to add to text file
            f = open(val + ".txt", "a")
            f.write("\nThe Survey Answers :")
            f.close()

            options_list = ["Yes", "No"]
            value_inside = tkinter.StringVar(window3)
            value_inside.set("Answer")
            question_menu = tkinter.OptionMenu(window3, value_inside, *options_list)
            question_menu.config(bg='#c4e0eb')
            question_menu.place(x=320, y=0)

            options_list1 = ["Yes", "No"]
            value_inside1 = tkinter.StringVar(window3)
            value_inside1.set("Answer")
            question_menu1 = tkinter.OptionMenu(window3, value_inside1, *options_list1)
            question_menu1.config(bg='#c4e0eb')
            question_menu1.place(x=320, y=30)

            options_list2 = ["Yes", "No"]
            value_inside2 = tkinter.StringVar(window3)
            value_inside2.set("Answer")
            question_menu2 = tkinter.OptionMenu(window3, value_inside2, *options_list2)
            question_menu2.config(bg='#c4e0eb')
            question_menu2.place(x=320, y=60)

            options_list3 = ["Yes", "No"]
            value_inside3 = tkinter.StringVar(window3)
            value_inside3.set("Answer")
            question_menu3 = tkinter.OptionMenu(window3, value_inside3, *options_list3)
            question_menu3.config(bg='#c4e0eb')
            question_menu3.place(x=320, y=90)

            options_list4 = ["Yes", "No"]
            value_inside4 = tkinter.StringVar(window3)
            value_inside4.set("Answer")
            question_menu4 = tkinter.OptionMenu(window3, value_inside4, *options_list4)
            question_menu4.config(bg='#c4e0eb')
            question_menu4.place(x=320, y=120)

            options_list5 = ["Yes", "No"]
            value_inside5 = tkinter.StringVar(window3)
            value_inside5.set("Answer")
            question_menu5 = tkinter.OptionMenu(window3, value_inside5, *options_list5)
            question_menu5.config(bg='#c4e0eb')
            question_menu5.place(x=320, y=150)

            options_list7 = ["Yes", "No"]
            value_inside7 = tkinter.StringVar(window3)
            value_inside7.set("Answer")
            question_menu7 = tkinter.OptionMenu(window3, value_inside7, *options_list7)
            question_menu7.config(bg='#c4e0eb')
            question_menu7.place(x=320, y=180)

            options_list8 = ["Yes", "No"]
            value_inside8 = tkinter.StringVar(window3)
            value_inside8.set("Answer")
            question_menu8 = tkinter.OptionMenu(window3, value_inside8, *options_list8)
            question_menu8.config(bg='#c4e0eb')
            question_menu8.place(x=320, y=210)

            options_list10 = ["Yes", "No"]
            value_inside10 = tkinter.StringVar(window3)
            value_inside10.set("Answer")
            question_menu10 = tkinter.OptionMenu(window3, value_inside10, *options_list10)
            question_menu10.config(bg='#c4e0eb')
            question_menu10.place(x=320, y=240)

            def ask():
                answer = value_inside.get()
                answer1 = value_inside1.get()
                answer2 = value_inside2.get()
                answer3 = value_inside3.get()
                answer4 = value_inside4.get()
                answer5 = value_inside5.get()
                answer7 = value_inside7.get()
                answer8 = value_inside8.get()
                answer10 = value_inside10.get()

                with conn:
                    c.execute(
                        """UPDATE patient SET question = ?, question1 = ?, question2 = ?, question3 = ?, 
                        question4 = ?, question5 = ?, question7 = ?, question8 = ?, question10 = ? WHERE id = ?""",
                        (answer, answer1, answer2, answer3, answer4, answer5, answer7, answer8, answer10, val))

                flag_normal = 0

                count = [['Anemia', 0, 'Two 10 mg B12 pills a day for a month.'],
                         ['Bleeding', 0, 'To be evacuated urgently to the hospital.'],
                         ['Hyperlipidemia', 0, 'Schedule an appointment with a nutritionist and a 5 mg pill of '
                                               'Simobil daily\n for a week.'],
                         ['Disruption of blood production', 0, '10 mg pill of B12 a day for a month and 5 mg pill of '
                                                               'folic acid a day for a month'],
                         ['Hematological disorder', 0, 'An injection of a hormone to encourage red blood cell '
                                                       'production'],
                         ['Iron poisoning', 0, 'To be evacuated to the hospital'],
                         ['Dehydration', 0, 'Rest while lying down, drink a lot of water and fluids'],
                         ['Infection', 0, 'Dedicated antibiotics'],
                         ['Vitamin deficiency', 0, 'Referral for a blood test to identify the missing vitamins'],
                         ['Viral disease', 0, 'Rest at home'],
                         ['Diseases of the biliary tract', 0, 'Referral to surgical treatment'],
                         ['heart diseases', 0, 'Schedule an appointment with a nutritionist'],
                         ['Blood disease', 0, 'A combination of cyclophosphamide and corticosteroids'],
                         ['Liver disease', 0, 'Referral to a specific diagnosis for the purpose of determining '
                                              'treatment'],
                         ['Kidney disease', 0, 'Balance blood sugar levels'],
                         ['Iron deficiency', 0, 'Two 10 mg B12 pills a day for a month'],
                         ['Muscle diseases', 0, 'Two 5 mg pills of Altman c3 turmeric a day for a month'],
                         ['Lung disease', 0, 'Stop smoking / refer to X-ray of the lungs'],
                         ['Overactive thyroid gland', 0, 'Propylthiouracil to reduce thyroid activity'],
                         ['Adult diabetes', 0, 'Insulin adjustment for the patient'],
                         ['Cancer', 0, ' Entrectinib'], ['Smoking', 0, 'Stop smoking'],
                         ['Diet', 0, 'Schedule an appointment with a nutritionist'],
                         ['Malnutrition', 0, 'Schedule an appointment with a nutritionist'],
                         ['Increased consumption of meat', 0, 'Schedule an appointment with a nutritionist'],
                         ['Pregnancy', 0, 'A side effect of pregnancy.'],
                         ['use of multiple medications', 0, 'Referral to a family doctor to understand the '
                                                            'compatibility between\n medications.']]

                # WBC
                y1 = conn.execute(
                    "SELECT wbc,age FROM patient WHERE ID=:ID",
                    {'ID': val})
                x1 = y1.fetchall()

                if x1[0][0] > 11000 and x1[0][1] >= 18:
                    flag_normal = 1

                    if answer4 == 'Yes':
                        count[7][1] = count[7][1] + 1

                    if answer4 == 'No':
                        count[12][1] = count[12][1] + 1
                        count[20][1] = count[20][1] + 1

                if x1[0][0] < 4500 and x1[0][1] >= 18:
                    flag_normal = 1
                    count[9][1] = count[9][1] + 1
                    count[20][1] = count[20][1] + 1

                if x1[0][0] > 15500 and 4 <= x1[0][1] < 18:
                    flag_normal = 1

                    if answer4 == 'Yes':
                        count[7][1] = count[7][1] + 1

                    if answer4 == 'No':
                        count[12][1] = count[12][1] + 1
                        count[20][1] = count[20][1] + 1

                if x1[0][0] < 5500 and 4 <= x1[0][1] < 18:
                    flag_normal = 1
                    count[9][1] = count[9][1] + 1
                    count[20][1] = count[20][1] + 1

                if x1[0][0] > 17500 and 0 <= x1[0][1] < 4:
                    flag_normal = 1

                    if answer4 == 'Yes':
                        count[7][1] = count[7][1] + 1

                    if answer4 == 'No':
                        count[12][1] = count[12][1] + 1
                        count[20][1] = count[20][1] + 1

                if x1[0][0] < 6000 and 0 <= x1[0][1] < 4:
                    flag_normal = 1
                    count[9][1] = count[9][1] + 1
                    count[20][1] = count[20][1] + 1

                # Neut
                y2 = conn.execute(
                    "SELECT neut FROM patient WHERE ID=:ID",
                    {'ID': val})
                x2 = y2.fetchall()

                if x2[0][0] > 54:
                    flag_normal = 1
                    count[7][1] = count[7][1] + 1

                if x2[0][0] < 28:
                    flag_normal = 1
                    count[3][1] = count[3][1] + 1
                    count[7][1] = count[7][1] + 1
                    count[20][1] = count[20][1] + 1

                # Lymph
                y3 = conn.execute(
                    "SELECT lymph FROM patient WHERE ID=:ID",
                    {'ID': val})
                x3 = y3.fetchall()

                if x3[0][0] > 52:
                    flag_normal = 1
                    count[20][1] = count[20][1] + 1
                    count[7][1] = count[7][1] + 1

                if x3[0][0] < 36:
                    flag_normal = 1
                    count[3][1] = count[3][1] + 1

                # RBC
                y4 = conn.execute(
                    "SELECT rbc FROM patient WHERE ID=:ID",
                    {'ID': val})
                x4 = y4.fetchall()

                if x4[0][0] > 6:
                    flag_normal = 1
                    count[3][1] = count[3][1] + 1
                    count[17][1] = count[17][1] + 1
                    if answer == 'Yes':
                        count[21][1] = count[21][1] + 1

                if float(x4[0][0]) < 4.5:
                    flag_normal = 1
                    count[0][1] = count[0][1] + 1
                    count[1][1] = count[1][1] + 1

                # HCT
                y5 = conn.execute(
                    "SELECT hct,gender FROM patient WHERE ID=:ID",
                    {'ID': val})
                x5 = y5.fetchall()

                if x5[0][0] > 47 and x5[0][1] == 'Female':
                    flag_normal = 1
                    count[21][1] = count[21][1] + 1

                if x5[0][0] < 33 and x5[0][1] == 'Female':
                    flag_normal = 1
                    count[0][1] = count[0][1] + 1
                    count[1][1] = count[1][1] + 1

                if x5[0][0] > 54 and x5[0][1] == 'Male':
                    flag_normal = 1
                    count[21][1] = count[21][1] + 1

                if x5[0][0] < 37 and x5[0][1] == 'Male':
                    flag_normal = 1
                    count[0][1] = count[0][1] + 1
                    count[1][1] = count[1][1] + 1

                # Urea
                y6 = conn.execute(
                    "SELECT urea,region FROM patient WHERE ID=:ID",
                    {'ID': val})
                x6 = y6.fetchall()

                if x6[0][0] > 43 and x6[0][1] != 'East':
                    flag_normal = 1
                    count[14][1] = count[14][1] + 1
                    count[6][1] = count[6][1] + 1
                    if answer8 == 'Yes':
                        count[22][1] = count[22][1] + 1

                if x6[0][0] < 17 and x6[0][1] != 'East':
                    flag_normal = 1
                    count[23][1] = count[23][1] + 1
                    if answer5 == 'Yes':
                        count[22][1] = count[22][1] + 1
                    count[13][1] = count[13][1] + 1
                    if answer1 == 'Yes':
                        count[25][1] = count[25][1] + 1

                if float(x6[0][0]) > 47.3 and x6[0][1] == 'East':
                    flag_normal = 1
                    count[14][1] = count[14][1] + 1
                    count[6][1] = count[6][1] + 1
                    if answer8 == 'Yes':
                        count[22][1] = count[22][1] + 1

                if float(x6[0][0]) < 18.7 and x6[0][1] == 'East':
                    flag_normal = 1
                    count[23][1] = count[23][1] + 1
                    if answer5 == 'Yes':
                        count[22][1] = count[22][1] + 1
                    count[13][1] = count[13][1] + 1
                    if answer1 == 'Yes':
                        count[25][1] = count[25][1] + 1

                # Hb
                y7 = conn.execute(
                    "SELECT hb,gender,age,iron FROM patient WHERE ID=:ID",
                    {'ID': val})
                x7 = y7.fetchall()

                if x7[0][0] < 12 and x7[0][1] == 'Female' and x7[0][2] > 17:
                    flag_normal = 1
                    count[0][1] = count[0][1] + 1
                    count[4][1] = count[4][1] + 1
                    count[1][1] = count[1][1] + 1

                    if x7[0][3] < 60:
                        count[15][1] = count[15][1] + 1

                if x7[0][0] < 12 and x7[0][1] == 'Male' and x7[0][2] > 17:
                    flag_normal = 1
                    count[0][1] = count[0][1] + 1
                    count[4][1] = count[4][1] + 1
                    count[1][1] = count[1][1] + 1

                    if x7[0][3] < 60:
                        count[15][1] = count[15][1] + 1

                if float(x7[0][0]) < 11.5 and 17 >= x7[0][2] >= 0:
                    flag_normal = 1
                    count[0][1] = count[0][1] + 1
                    count[4][1] = count[4][1] + 1
                    count[1][1] = count[1][1] + 1

                    if x7[0][3] < 60:
                        count[15][1] = count[15][1] + 1

                # Creatinine
                y8 = conn.execute(
                    "SELECT creatinine,age FROM patient WHERE ID=:ID",
                    {'ID': val})
                x8 = y8.fetchall()

                if float(x8[0][0]) > 0.5 and 0 < x8[0][1] <= 2:
                    if answer7 == 'No':
                        flag_normal = 1
                        count[14][1] = count[14][1] + 1
                        count[24][1] = count[24][1] + 1
                        count[16][1] = count[16][1] + 1

                if float(x8[0][0]) < 0.2 and 0 <= x8[0][1] <= 2:
                    if answer3 == 'No':
                        flag_normal = 1
                        count[16][1] = count[16][1] + 1
                    if answer3 == 'Yes':
                        flag_normal = 1
                        count[23][1] = count[23][1] + 1

                if x8[0][0] > 1 and 3 <= x8[0][1] <= 17:
                    if answer7 == 'No':
                        flag_normal = 1
                        count[14][1] = count[14][1] + 1
                        count[24][1] = count[24][1] + 1
                        count[16][1] = count[16][1] + 1

                if float(x8[0][0]) < 0.5 and 3 <= x8[0][1] <= 17:
                    if answer3 == 'No':
                        flag_normal = 1
                        count[16][1] = count[16][1] + 1
                    if answer3 == 'Yes':
                        flag_normal = 1
                        count[23][1] = count[23][1] + 1

                if x8[0][0] > 1 and 18 <= x8[0][1] <= 59:
                    if answer7 == 'No':
                        flag_normal = 1
                        count[14][1] = count[14][1] + 1
                        count[24][1] = count[24][1] + 1
                        count[16][1] = count[16][1] + 1

                if float(x8[0][0]) < 0.6 and 18 <= x8[0][1] <= 59:
                    if answer3 == 'No':
                        flag_normal = 1
                        count[16][1] = count[16][1] + 1
                    if answer3 == 'Yes':
                        flag_normal = 1
                        count[23][1] = count[23][1] + 1

                if float(x8[0][0]) > 1.2 and x8[0][1] >= 60:
                    if answer7 == 'No':
                        flag_normal = 1
                        count[14][1] = count[14][1] + 1
                        count[24][1] = count[24][1] + 1
                        count[16][1] = count[16][1] + 1

                if float(x8[0][0]) < 0.6 and x8[0][1] >= 60:
                    if answer3 == 'No':
                        flag_normal = 1
                        count[16][1] = count[16][1] + 1
                    if answer3 == 'Yes':
                        flag_normal = 1
                        count[23][1] = count[23][1] + 1

                # Iron
                y9 = conn.execute(
                    "SELECT iron,gender FROM patient WHERE ID=:ID",
                    {'ID': val})
                x9 = y9.fetchall()

                if int(x9[0][0]) > 160 and x9[0][1] == 'Male':
                    flag_normal = 1
                    count[5][1] = count[5][1] + 1

                if int(x9[0][0]) < 60 and x9[0][1] == 'Male':
                    if answer10 == 'Yes':
                        flag_normal = 1
                        count[23][1] = count[23][1] + 1
                    if answer10 == 'No':
                        flag_normal = 1
                        count[15][1] = count[15][1] + 1
                        count[1][1] = count[1][1] + 1

                if int(x9[0][0]) > 128 and x9[0][1] == 'Female':
                    flag_normal = 1
                    count[5][1] = count[5][1] + 1

                if int(x9[0][0]) < 48 and x9[0][1] == 'Female':
                    if answer10 == 'Yes':
                        flag_normal = 1
                        count[23][1] = count[23][1] + 1
                    if answer10 == 'No':
                        flag_normal = 1
                        count[15][1] = count[15][1] + 1
                        if answer1 == 'Yes':
                            count[25][1] = count[25][1] + 1
                        count[1][1] = count[1][1] + 1

                # HDL
                y10 = conn.execute(
                    "SELECT hdl,gender,country FROM patient WHERE ID=:ID",
                    {'ID': val})
                x10 = y10.fetchall()

                if float(x10[0][0]) < 34.8 and x10[0][1] == 'Male' and x10[0][2] == 'Ethiopia':
                    flag_normal = 1
                    count[11][1] = count[11][1] + 1
                    count[2][1] = count[2][1] + 1
                    count[19][1] = count[19][1] + 1

                if float(x10[0][0]) < 40.8 and x10[0][1] == 'Female' and x10[0][2] == 'Ethiopia':
                    flag_normal = 1
                    count[11][1] = count[11][1] + 1
                    count[2][1] = count[2][1] + 1
                    count[19][1] = count[19][1] + 1

                if int(x10[0][0]) < 29 and x10[0][1] == 'Male' and x10[0][2] != 'Ethiopia':
                    flag_normal = 1
                    count[11][1] = count[11][1] + 1
                    count[2][1] = count[2][1] + 1
                    count[19][1] = count[19][1] + 1

                if int(x10[0][0]) < 34 and x10[0][1] == 'Female' and x10[0][2] != 'Ethiopia':
                    flag_normal = 1
                    count[11][1] = count[11][1] + 1
                    count[2][1] = count[2][1] + 1
                    count[19][1] = count[19][1] + 1

                # Alkaline Phosphatase
                y11 = conn.execute(
                    "SELECT alkaline_phosphatase,region FROM patient WHERE ID=:ID",
                    {'ID': val})
                x11 = y11.fetchall()

                if int(x11[0][0]) > 120 and x11[0][1] == 'East':
                    flag_normal = 1
                    count[13][1] = count[13][1] + 1
                    count[10][1] = count[10][1] + 1
                    count[18][1] = count[18][1] + 1
                    if answer2 == 'Yes':
                        count[26][1] = count[26][1] + 1
                    if answer1 == 'Yes':
                        count[25][1] = count[25][1] + 1

                if int(x11[0][0]) < 60 and x11[0][1] == 'East':
                    flag_normal = 1
                    if answer3 == 'Yes':
                        count[8][1] = count[8][1] + 1
                    if answer3 == 'No':
                        count[23][1] = count[23][1] + 1

                if int(x11[0][0]) > 90 and x11[0][1] != 'East':
                    flag_normal = 1
                    count[13][1] = count[13][1] + 1
                    count[10][1] = count[10][1] + 1
                    count[18][1] = count[18][1] + 1
                    if answer2 == 'Yes':
                        count[26][1] = count[26][1] + 1
                    if answer1 == 'Yes':
                        count[25][1] = count[25][1] + 1

                if int(x11[0][0]) < 30 and x11[0][1] != 'East':
                    flag_normal = 1
                    if answer3 == 'Yes':
                        count[8][1] = count[8][1] + 1
                    if answer3 == 'No':
                        count[23][1] = count[23][1] + 1

                # not sick
                if flag_normal == 0:
                    lable = Label(window3, text="Healthy person, No procedures are required.")
                    lable.place(x=10, y=370)

                    f = open(val + ".txt", "a")
                    f.write("\nHealthy person, No procedures are required.")
                    f.close()

                def after_time():
                    windowmessage1.config(text="", bg='#c4e0eb')

                if answer != 'Answer' and answer1 != 'Answer' and answer2 != 'Answer' and answer3 != 'Answer' and \
                        answer4 != 'Answer' and answer5 != 'Answer' and answer7 != 'Answer' and answer8 != 'Answer'\
                        and answer10 != 'Answer':

                    windowmessage1.config(text="", bg='#c4e0eb')

                    # to add to text file
                    f = open(val + ".txt", "a")
                    f.write("\nDo you smoke?" + answer)
                    f.close()

                    # to add to text file
                    f = open(val + ".txt", "a")
                    f.write("\nAre you pregnant?" + answer1)
                    f.close()

                    # to add to text file
                    f = open(val + ".txt", "a")
                    f.write("\nAre you on any medications?" + answer2)
                    f.close()

                    # to add to text file
                    f = open(val + ".txt", "a")
                    f.write("\nDo you consume protein in your meals?" + answer3)
                    f.close()

                    # to add to text file
                    f = open(val + ".txt", "a")
                    f.write("\nDo you have high body temperatures?" + answer4)
                    f.close()

                    # to add to text file
                    f = open(val + ".txt", "a")
                    f.write("\nAre you on protein diet?" + answer5)
                    f.close()

                    # to add to text file
                    f = open(val + ".txt", "a")
                    f.write("\nHave you puked or had diarrhea recently?" + answer7)
                    f.close()

                    # to add to text file
                    f = open(val + ".txt", "a")
                    f.write("\nDo you eat a lot of food with protein?" + answer8)
                    f.close()

                    # to add to text file
                    f = open(val + ".txt", "a")
                    f.write("\nDo you have any malnutrition disorders?" + answer10)
                    f.close()

                    # sick
                    if flag_normal == 1:
                        arr_size = 26
                        first = second = third = -1
                        place1 = place2 = place3 = -1
                        for i in range(0, arr_size):
                            # print(i)
                            if count[i][1] > first:
                                place1 = i
                                third = second
                                second = first
                                first = count[i][1]

                            elif count[i][1] > second:
                                place2 = i
                                third = second
                                second = count[i][1]

                            elif count[i][1] > third:
                                place3 = i
                                third = count[i][1]

                        equal = count[place1][1] + count[place2][1] + count[place3][1]
                        percent1 = count[place1][1]/equal
                        percent2 = count[place2][1]/equal
                        percent3 = count[place3][1]/equal

                        result1 = Label(window3, text=count[place1][0] + "{: .2%}".format(percent1), fg='red',
                                        bg='#c4e0eb')
                        result1.place(x=10, y=310)
                        solution1 = Label(window3, text=count[place1][2], bg='#c4e0eb')
                        solution1.place(x=10, y=340)

                        f = open(val + ".txt", "a")
                        f.write("\nResult: " + result1.cget("text") + "\nSolution: " + solution1.cget("text"))
                        f.close()

                        if count[place2][1] > 0:
                            result2 = Label(window3, text=count[place2][0] + "{: .2%}".format(percent2), fg='red',
                                            bg='#c4e0eb')
                            result2.place(x=10, y=370)
                            solution2 = Label(window3, text=count[place2][2], bg='#c4e0eb')
                            solution2.place(x=10, y=400)

                            f = open(val + ".txt", "a")
                            f.write("\nResult: " + result2.cget("text") + "\nSolution: " + solution2.cget("text"))
                            f.close()

                        if count[place3][1] > 0:
                            result3 = Label(window3, text=count[place3][0] + "{: .2%}".format(percent3), fg='red',
                                            bg='#c4e0eb')
                            result3.place(x=10, y=430)
                            solution3 = Label(window3, text=count[place3][2], bg='#c4e0eb')
                            solution3.place(x=10, y=460)

                            f = open(val + ".txt", "a")
                            f.write("\nResult: " + result3.cget("text") + "\nSolution: " + solution3.cget("text"))
                            f.close()

                if answer == 'Answer' or answer1 == 'Answer' or answer2 == 'Answer' or answer3 == 'Answer' or \
                        answer4 == 'Answer' or answer5 == 'Answer' or answer7 == 'Answer' or answer8 == 'Answer' \
                        or answer10 == 'Answer':
                    try:
                        int(answer)
                    except ValueError:
                        windowmessage1.config(text="Not a valid input!", bg='#c4e0eb', fg='red')
                        windowmessage1.after(2000, after_time)
                        return 0

                    windowmessage1.config(text="", bg='#c4e0eb')

            exitbutton2 = tkinter.Button(window3, text="Back", command=lambda: [window3.destroy(), add()], width=12,
                                         bg='#639bc0', fg='black')
            exitbutton2.place(x=100, y=280)

            exitbutton2 = tkinter.Button(window3, text="Analyze", command=lambda: ask(), width=12,
                                         bg='#639bc0', fg='black')
            exitbutton2.place(x=290, y=280)

            windowmessage1 = Label(window3, text="", bg='#c4e0eb')
            windowmessage1.place(x=195, y=310)

    def add_Patients():
        flag = 0
        val = entry.get().lower().capitalize()
        val2 = Genderbox.get()  # Gender
        val15 = Countrybox.get()  # Country
        val16 = Regionbox.get()  # Region
        val17 = ""
        val18 = ""
        val19 = ""
        val20 = ""
        val21 = ""
        val22 = ""
        val24 = ""
        val25 = ""
        val27 = ""

        def after_time():
            windowmessage.config(text="", bg='#c4e0eb')

        try:
            if val2 == '' or val15 == '' or val16 == '':
                int(val2)
                int(val15)
                int(val16)
            for x in range(len(val)):
                if 48 <= ord(val[x]) <= 57:
                    flag = 1
                    int(entry.get())
            int(entry1.get())
            val1 = entry1.get()
            int(entry3.get())
            val3 = entry3.get()
            int(entry4.get())
            val4 = entry4.get()
            int(entry5.get())
            val5 = entry5.get()
            int(entry6.get())
            val6 = entry6.get()
            float(entry7.get())
            val7 = entry7.get()
            int(entry8.get())
            val8 = entry8.get()
            int(entry9.get())
            val9 = entry9.get()
            float(entry10.get())
            val10 = entry10.get()
            float(entry11.get())
            val11 = entry11.get()
            int(entry12.get())
            val12 = entry12.get()
            int(entry13.get())
            val13 = entry13.get()
            int(entry14.get())
            val14 = entry14.get()
        except ValueError:
            windowmessage.config(text="Not a valid input!", bg='#c4e0eb', fg='red')
            windowmessage.after(2000, after_time)
            return 0

        windowmessage.config(text="", bg='#c4e0eb')

        if flag == 0:
            f = open(val1 + ".txt", "x")
            # Patient details txt file
            f.write("Patient Details" +
                    "\nName of patient: " + val + "\nPatient ID: " + val1 + "\nGender: " + val2 + "\nCountry: " + val15
                    + "\nRegion: " + val16 + "\nAge: " + val3 + "\nWbc: " + val4 + "\nNeut: " +
                    val5 + "\nLymph: " + val6 + "\nRbc: " + val7 + "\nHct: " + val8 + "\nUrea: " + val9 + "\nHb: " +
                    val10 + "\nCreatinine: " + val11 + "\nIron: " + val12 + "\nHdl: " + val13 +
                    "\nAlkaline Phosphatase: " + val14)
            # Symptoms

            f.close()

        if flag == 0:
            entry.delete(0, END)
            Genderbox.set('')
            Countrybox.set('')
            Regionbox.set('')
            entry1.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry6.delete(0, END)
            entry7.delete(0, END)
            entry8.delete(0, END)
            entry9.delete(0, END)
            entry10.delete(0, END)
            entry11.delete(0, END)
            entry12.delete(0, END)
            entry13.delete(0, END)
            entry14.delete(0, END)

        if flag == 0:
            with conn:
                c.execute(
                    "INSERT INTO patient VALUES (:name,:id,:gender,:country,:region,:age,:wbc,:neut,:lymph,:rbc,"
                    ":hct,:urea,:hb,:creatinine,:iron,:hdl,:alkaline_phosphatase,:question,:question1,:question2,"
                    ":question3, :question4, :question5, :question7, :question8, :question10) ",
                    {'name': val, 'id': val1, 'gender': val2, 'country': val15, 'region': val16, 'age': val3,
                     'wbc': val4, 'neut': val5, 'lymph': val6, 'rbc': val7,
                     'hct': val8, 'urea': val9, 'hb': val10, 'creatinine': val11, 'iron': val12, 'hdl': val13,
                     'alkaline_phosphatase': val14, 'question': val17, 'question1': val18, 'question2': val19,
                     'question3': val20, 'question4': val21, 'question5': val22, 'question7': val24, 'question8': val25,
                     'question10': val27})

    entry = tkinter.Entry(window, width=20, fg='blue')
    entry.place(x=240, y=7)
    entry1 = tkinter.Entry(window, width=20, fg='blue')
    entry1.place(x=240, y=32)

    n = tk.StringVar()
    Genderbox = ttk.Combobox(window, width=17, textvariable=n)
    # Adding combobox drop down list
    Genderbox['values'] = ("Male", "Female")
    Genderbox.place(x=240, y=57)
    Genderbox.current()

    n1 = tk.StringVar()
    Countrybox = ttk.Combobox(window, width=17, textvariable=n1)
    # Adding combobox drop down list
    Countrybox['values'] = ("Afghanistan", "Albania", "Algeria", "Argentina", "Australia", "Austria",
                            "Bangladesh",
                            "Belgium", "Bolivia", "Botswana", "Brazil", "Bulgaria", "Cambodia", "Cameroon",
                            "Canada",
                            "Chile", "China", "Colombia", "Costa Rica", "Croatia", "Cuba", "Czech Republic",
                            "Denmark",
                            "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "England", "Estonia",
                            "Ethiopia",
                            "Fiji", "Finland", "France", "Germany", "Ghana", "Greece", "Guatemala", "Haiti",
                            "Honduras",
                            "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
                            "Italy",
                            "Jamaica", "Japan", "Jordan", "Kenya", "Kuwait", "Laos", "Latvia", "Lebanon", "Libya",
                            "Lithuania", "Madagascar", "Malaysia", "Mali", "Malta", "Mexico", "Mongolia", "Morocco",
                            "Mozambique", "Namibia", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Nigeria",
                            "Norway", "Pakistan", "Panama", "Paraguay", "Peru", "Philippines", "Poland", "Portugal",
                            "Romania", "Russia", "Saudi Arabia", "Scotland", "Senegal", "Serbia", "Singapore",
                            "Slovakia",
                            "South Africa", "South Korea", "Spain", "Sri Lanka", "Sudan", "Sweden", "Switzerland",
                            "Syria", "Taiwan", "Tajikistan", "Thailand", "Tonga", "Tunisia", "Turkey", "Ukraine",
                            "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Venezuela",
                            "Vietnam", "Wales", "Zambia", "Zimbabwe")
    Countrybox.place(x=240, y=82)
    Countrybox.current()

    n2 = tk.StringVar()
    Regionbox = ttk.Combobox(window, width=17, textvariable=n2)
    # Adding combobox drop down list
    Regionbox['values'] = ("East", "West")
    Regionbox.place(x=240, y=107)
    Regionbox.current()

    entry3 = tkinter.Entry(window, width=20, fg='blue')
    entry3.place(x=240, y=132)
    entry4 = tkinter.Entry(window, width=20, fg='blue')
    entry4.place(x=240, y=157)
    entry5 = tkinter.Entry(window, width=20, fg='blue')
    entry5.place(x=240, y=182)
    entry6 = tkinter.Entry(window, width=20, fg='blue')
    entry6.place(x=240, y=207)
    entry7 = tkinter.Entry(window, width=20, fg='blue')
    entry7.place(x=240, y=232)
    entry8 = tkinter.Entry(window, width=20, fg='blue')
    entry8.place(x=240, y=257)
    entry9 = tkinter.Entry(window, width=20, fg='blue')
    entry9.place(x=240, y=282)
    entry10 = tkinter.Entry(window, width=20, fg='blue')
    entry10.place(x=240, y=307)
    entry11 = tkinter.Entry(window, width=20, fg='blue')
    entry11.place(x=240, y=332)
    entry12 = tkinter.Entry(window, width=20, fg='blue')
    entry12.place(x=240, y=357)
    entry13 = tkinter.Entry(window, width=20, fg='blue')
    entry13.place(x=240, y=382)
    entry14 = tkinter.Entry(window, width=20, fg='blue')
    entry14.place(x=240, y=407)

    btn2 = tkinter.Button(window, text="add", command=lambda: [add_Patients()], width=13, bg='#639bc0', fg='black')
    btn2.place(x=150, y=430)

    btn1 = tkinter.Button(window, text="Patients list",
                          command=lambda: [window.destroy(), Patients_list()], width=13, bg='#639bc0', fg='black')
    btn1.place(x=255, y=430)

    exitbutton = tkinter.Button(window, text="Logout", command=lambda: [window.destroy(), Main_page()], width=13,
                                bg='#639bc0', fg='black')
    exitbutton.place(x=200, y=460)

    windowmessage = Label(window, text="", bg='#c4e0eb')
    windowmessage.place(x=200, y=490)


Main_page()