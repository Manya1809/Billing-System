from tkinter import *
from tkinter import messagebox
import tempfile
import os
import random
from PIL import ImageTk,Image

qb = Tk()
qb.title("LOGIN SYSTEM")
qb.geometry('1300x1400')
qb.resizable(False, False)
#qb['bg'] = "navajo white"
bg=PhotoImage(file="images/bii.png")
lbl= Label(image=bg).pack()
frame1 = LabelFrame(font=("timesnewrommon", 12, "bold"), bg="plum1", bd=10)
frame1.place(x=320, y=90, width=520, height=500)


def login():
    username = entry1.get()
    password = entry2.get()
    if (username == "" and password == ""):
        messagebox.showerror("Error", 'Blank Not Allowed')
    elif (username == ""):
        messagebox.showinfo('Error', "please enter username")
    elif (password == ""):
        messagebox.showinfo('Error', 'Please enter password')
    elif (username == "a1store" and password == '1234567'):
        root = Toplevel(qb)
        root.title("BILLING SYSTEM")
        root.geometry("1900x1800")
        f1 = LabelFrame(root, text="CUSTOMER DETAILS", font=("timesnewrommon", 12, "bold"), fg="gold2", bg="cadet blue",
                        relief=GROOVE, bd=10)
        f1.place(x=5, y=80, width=1350, height=100)
        global rdovar
        rdovar = IntVar()
        nme = StringVar()
        ph = StringVar()
        name = Label(f1, text="CUSTOMER NAME", font=("timesnewroman", 14, "bold"), bd=7, fg="forest green").place(x=3,
                                                                                                                  y=14)
        nme_txt = Entry(f1, font=("timesnewroman", 12, "bold"), fg="brown", bd=7, textvariable=nme).place(x=340, y=14)
        phn = Label(f1, text="PHONE NO:", font=("timesnewroman", 14, "bold"), bd=7, fg="forest green").place(x=740,
                                                                                                             y=14)
        ph_txt = Entry(f1, font=("timesnewroman", 12, "bold"), fg="brown", bd=7, textvariable=ph).place(x=960, y=14)
        # ========VARIABLE========
        bodywash = IntVar()
        hairoil = IntVar()
        shampoo = IntVar()
        broom = IntVar()
        soap = IntVar()
        hairDye = IntVar()
        cream = IntVar()
        nailcutter = IntVar()
        total = DoubleVar()
        # =========COSTVARIABLE==========
        bc = StringVar()
        hc = StringVar()
        sc = StringVar()
        brc = StringVar()
        soc = StringVar()
        hac = StringVar()
        crc = StringVar()
        nc = StringVar()
        total_cost = StringVar()
        bill_num = StringVar()
        x = random.randint(1000, 9999)
        bill_num.set(x)

        # =======FUNCTIONS===========
        def Total():
            if bodywash.get() == 0 and hairoil.get() == 0 and shampoo.get() == 0 and broom.get() == 0 and soap.get() == 0 and hairDye.get() == 0 and cream.get() == 0 and nailcutter.get() == 0 :
                messagebox.showerror("Error", "Please Select Number Of Quantity")
            else:
                b = bodywash.get()
                h = hairoil.get()
                s = shampoo.get()
                br = broom.get()
                so = soap.get()
                hd = hairDye.get()
                c = cream.get()
                n = nailcutter.get()
                to = float(b * 255 + h * 90 + s * 260 + br * 40 + so * 40 + hd * 22 + c * 100 + n * 18)
                total.set(b + h + s + br + so + hd + c + n)
                total_cost.set(str(round(to, 2)))

                bc.set('Rs.' + str(b * 155))
                hc.set('Rs.' + str(h * 90))
                sc.set('Rs.' + str(s * 260))
                brc.set('Rs.' + str(br * 40))
                soc.set('Rs.' + str(so * 40))
                hac.set('Rs.' + str(hd * 22))
                crc.set('Rs.' + str(c * 100))
                nc.set('Rs.' + str(n * 18))

        def reciept():
            textarea.delete(1.0, END)
            textarea.insert(END, f'\t\tWELCOME \n')
            textarea.insert(END, f'\t\t A1 Store\n')
            textarea.insert(END, f'BILLER NAME\t:\t\t ARYAN GOSWAMI\n')
            textarea.insert(END, f'BILL NUMBER\t:\t\t{bill_num.get()}\n')
            textarea.insert(END, f'CUSTOMER NAME\t:\t\t{nme.get()}\n')
            textarea.insert(END, f'PHONE NUMBER\t:\t\t{ph.get()}\n')
            textarea.insert(END, f"========================================")
            textarea.insert(END, '\n\nItems\t\tQTY\tCost Of Items')
            if bodywash.get() != 0:
                textarea.insert(END, f'\n\nBodywash\t\t{bodywash.get()}\t{bc.get()}')
            if hairoil.get() != 0:
                textarea.insert(END, f'\n\nHairOil\t\t{hairoil.get()}\t{hc.get()}')
            if shampoo.get() != 0:
                textarea.insert(END, f'\n\nShampoo\t\t{shampoo.get()}\t{sc.get()}')
            if broom.get() != 0:
                textarea.insert(END, f'\n\nBroom\t\t{broom.get()}\t{brc.get()}')
            if soap.get() != 0:
                textarea.insert(END, f'\n\nSoap\t\t{soap.get()}\t{soc.get()}')
            if hairDye.get() != 0:
                textarea.insert(END, f'\n\nHairDye\t\t{hairDye.get()}\t{hac.get()}')
            if cream.get() != 0:
                textarea.insert(END, f'\n\nCream\t\t{cream.get()}\t{crc.get()}')
            if nailcutter.get() != 0:
                textarea.insert(END, f'\n\nNailCutter\t\t{nailcutter.get()}\t{nc.get()}')
            textarea.insert(END, f'\n========================================')
            textarea.insert(END, f'\nTotal Price\t\t{total.get()}\t{total_cost.get()}\n')
            textarea.insert(END, f'==========================================')
            #textarea.insert(END, f'Ammount Paid by cash {rdovar.get()}')

            textarea.insert(END, '\n\t\tTHANK YOU!\n\t\tVISIT AGAIN')

        def print():
            q = textarea.get('1.0', 'end')
            filename = tempfile.mktemp('.txt')
            open(filename, 'w').write(q)
            os.startfile(filename, 'Print')
            with open("record2.txt", 'a') as f:
                f.write(q)

        def reset():
            nme.set('')
            ph.set('')
            textarea.delete('1.0', END)
            bodywash.set(0)
            hairoil.set(0)
            shampoo.set(0)
            broom.set(0)
            soap.set(0)
            hairDye.set(0)
            cream.set(0)
            nailcutter.set(0)
            total.set(0)

            bc.set('')
            hc.set('')
            sc.set('')
            brc.set('')
            soc.set('')
            hac.set('')
            crc.set('')
            nc.set('')
            total_cost.set('')

        def pay():
            asd = Tk()
            asd.geometry("300x400")
            asd['bg'] = "sky blue"
            rdobtn1 = Radiobutton(asd, text="Cash", variable=rdovar, value=0, height=2, width=10, bg="gray")
            rdobtn1.place(x=130, y=10)
            rdobtn2 = Radiobutton(asd, text="NetBanking", variable=rdovar, value=1, height=2, width=10, bg="gray")
            rdobtn2.place(x=130, y=100)
            rdobtn3 = Radiobutton(asd, text="Debit/Credit Card", variable=rdovar, value=2, height=2, width=10,
                                  bg="gray")
            rdobtn3.place(x=130, y=200)

            def payok():
                if rdovar == '':
                    messagebox.showerror("Error", "blank")
                else:
                    asd.destroy()

            aokbtn = Button(asd, text="OK", font=" Arial 16 bold", bd=2, bg="red", command=payok)
            aokbtn.place(x=150, y=290)

        def exit():
            root.destroy()
            qb.destroy()

        ########################################################################
        Label(root, text="BILLING SYSTEM", font="ALGERIAN 20", bg="cadet blue", fg="white", bd=12,
              relief=SUNKEN).pack(fill=X, pady=12)
        F1 = LabelFrame(root, text="Product Details", font=('timesnewromman 18 bold'), fg="gold", bg="cadet blue")
        F1.place(x=5, y=185, width=950, height=445)
        # =========HEADING==========
        itm = Label(F1, text="Items", font="timesnewrommon 22 bold underline", fg="black")
        itm.grid(row=0, column=0, padx=30, pady=3)
        n = Label(F1, text="Number Of Items", font="Helvetic 22 bold underline", fg="black")
        n.grid(row=0, column=1, padx=60, pady=3)
        cost = Label(F1, text="Cost Of Items", font="Helvetic 22 bold underline", fg="black")
        cost.grid(row=0, column=2, padx=80, pady=3)
        # =====product======
        Bodywash = Label(F1, text="1.Bodywash:RS.155", font="timesnewrommon 16 bold ", fg="forest green")
        Bodywash.grid(row=1, column=0, padx=10, pady=4)
        bodywashquantity = Entry(F1, font="timesnewrommon 16 bold", fg="brown", bg="light grey", bd=5, relief=SUNKEN,
                                 justify=CENTER, textvariable=bodywash)
        bodywashquantity.grid(row=1, column=1, pady=4)
        bodywashcost = Entry(F1, font="timesnewrommon 16 bold", fg="brown", bg="light grey", bd=5, relief=SUNKEN,
                             justify=CENTER, textvariable=bc)
        bodywashcost.grid(row=1, column=2, padx=10, pady=4)

        Hairoil = Label(F1, text="2.HairOil RS.90", font="timesnewrommon 16 bold ", fg="forest green")
        Hairoil.grid(row=2, column=0, padx=10, pady=4)
        hairoilquantity = Entry(F1, font="timesnewrommon 16 bold", fg="brown", bg="light grey", bd=5, relief=SUNKEN,
                                justify=CENTER, textvariable=hairoil)
        hairoilquantity.grid(row=2, column=1, padx=10, pady=4)
        hairoilcost = Entry(F1, font="timesnewrommon 16 bold", fg="brown", bg="light grey", bd=5, relief=SUNKEN,
                            justify=CENTER, textvariable=hc)
        hairoilcost.grid(row=2, column=2, padx=10, pady=4)

        Shampoo = Label(F1, text="3.SHAMPOO RS.260", font="timesnewrommon 16 bold ", fg="forest green")
        Shampoo.grid(row=3, column=0, padx=10, pady=4)
        shampooquantity = Entry(F1, font="timesnewrommon 16 bold", fg="brown", bg="light grey", bd=5, relief=SUNKEN,
                                justify=CENTER, textvariable=shampoo)
        shampooquantity.grid(row=3, column=1, padx=10, pady=4)
        shampoocost = Entry(F1, font="timesnewrommon 16 bold", fg="brown", bg="light grey", bd=5, relief=SUNKEN,
                            justify=CENTER, textvariable=sc)
        shampoocost.grid(row=3, column=2, padx=10, pady=4)

        Broom = Label(F1, text="4.BROOM RS.40", font="timesnewrommon 16 bold", fg="forest green")
        Broom.grid(row=4, column=0, padx=10, pady=4)
        broomquantity = Entry(F1, font="timesnewrommon 16 bold", fg="brown", bg="light grey", bd=5, relief=SUNKEN,
                              justify=CENTER, textvariable=broom)
        broomquantity.grid(row=4, column=1, padx=10, pady=4)
        broomcost = Entry(F1, font="timesnewrommon 16 bold", fg="brown", bg="light grey", bd=5, relief=SUNKEN,
                          justify=CENTER, textvariable=brc)
        broomcost.grid(row=4, column=2, padx=10, pady=4)

        Soap = Label(F1, text="5.SOAP RS.40", font="timesnewrommon 16 bold", fg="forest green")
        Soap.grid(row=5, column=0, padx=10, pady=4)
        soapquantity = Entry(F1, font="timesnewrommon 16 bold", fg="brown", bg="light grey", bd=5, relief=SUNKEN,
                             justify=CENTER, textvariable=soap)
        soapquantity.grid(row=5, column=1, padx=10, pady=4)
        soapcost = Entry(F1, font="timesnewrommon 16 bold", fg="brown", bg="light grey", bd=5, relief=SUNKEN,
                         justify=CENTER, textvariable=soc)
        soapcost.grid(row=5, column=2, padx=10, pady=4)

        HairDye = Label(F1, text="6.HAIRDYE:RS.22", font="timesnewrommon 16 bold ", fg="forest green")
        HairDye.grid(row=6, column=0, padx=10, pady=4)
        hairdyequantity = Entry(F1, font="timesnewrommon 16 bold", fg="brown", bg="light grey", bd=5, relief=SUNKEN,
                                justify=CENTER, textvariable=hairDye)
        hairdyequantity.grid(row=6, column=1, pady=4)
        hairdyecost = Entry(F1, font="timesnewrommon 16 bold", fg="brown", bg="light grey", bd=5, relief=SUNKEN,
                            justify=CENTER, textvariable=hac)
        hairdyecost.grid(row=6, column=2, padx=10, pady=4)

        Cream = Label(F1, text="7.CREAM RS.100", font="timesnewrommon 16 bold ", fg="forest green")
        Cream.grid(row=7, column=0, padx=10, pady=4)
        creamquantity = Entry(F1, font="timesnewrommon 16 bold", fg="brown", bg="light grey", bd=5, relief=SUNKEN,
                              justify=CENTER, textvariable=cream)
        creamquantity.grid(row=7, column=1, padx=10, pady=4)
        creamcost = Entry(F1, font="timesnewrommon 16 bold", fg="brown", bg="light grey", bd=5, relief=SUNKEN,
                          justify=CENTER, textvariable=crc)
        creamcost.grid(row=7, column=2, padx=10, pady=4)

        NailCutter = Label(F1, text="8.NAIL CUTTER RS.18", font="timesnewrommon 16 bold ", fg="forest green")
        NailCutter.grid(row=8, column=0, pady="4")
        niquantity = Entry(F1, font="timesnewrommon 16 bold", fg="brown", bg="light grey", bd=5, relief=SUNKEN,
                           justify=CENTER, textvariable=nailcutter)
        niquantity.grid(row=8, column=1, padx=10, pady=4)
        nicost = Entry(F1, font="timesnewrommon 16 bold", fg="brown", bg="light grey", bd=5, relief=SUNKEN,
                       justify=CENTER, textvariable=nc)
        nicost.grid(row=8, column=2, padx=10, pady=4)

        # =========BILLAREA===========
        f2 = Frame(root, relief=GROOVE, bd=10)
        f2.place(x=935, y=185, width=420, height=448)
        bill_title = Label(f2, text="RECEIPT", font="Ariel 12 bold", bd=5, relief=GROOVE).pack(fill=X)
        storename = Label(f2, text="A1 STORE", font="timesnewrommon 18 bold", bd=7, bg='lemon chiffon', relief=GROOVE)
        storename.pack(fill=X)
        scroll = Scrollbar(f2, orient=VERTICAL)
        scroll.pack(side=RIGHT, fill=Y)
        textarea = Text(f2, font="Arial 12 bold", yscrollcommand=set)
        textarea.pack(fill=BOTH)
        scroll.config(command=textarea.yview)
        # ==========button==============
        f3 = Frame(root, relief=GROOVE, bd=10)
        f3.place(x=5, y=630, width=1350, height=80)
        totalbtn = Button(f3, text="TOTAL", font="Arial 17 bold ", bg="yellow", fg="red", bd=2, relief=GROOVE,
                          command=lambda: Total())
        totalbtn.grid(row=0, column=0, padx=60)

        paybtn = Button(f3, text=" PAY", font="Arial 18 bold", bg="yellow", fg="red", bd=2, relief=GROOVE, command=pay)
        paybtn.grid(row=0, column=1, padx=60)

        recieptbtn = Button(f3, text="RECIEPT", font="Arial 18 bold", bg="yellow", fg="red", bd=2, relief=GROOVE,
                            command=reciept)
        recieptbtn.grid(row=0, column=2, padx=60)

        printbtn = Button(f3, text="PRINT", font="Arial 18 bold", bg="yellow", fg="red", bd=2, relief=GROOVE,
                          command=print)
        printbtn.grid(row=0, column=3, padx=60)

        resetbtn = Button(f3, text="RESET", font="Arial 18 bold", bg="yellow", fg="red", bd=2, relief=GROOVE,
                          command=reset)
        resetbtn.grid(row=0, column=4, padx=60)
        exitbtn = Button(f3, text="EXIT", font="Arial 18 bold", bg="yellow", fg="red", bd=2, relief=GROOVE,
                         command=exit)
        exitbtn.grid(row=0, column=5, padx=60)
        root.mainloop()

    else:
        messagebox.showerror("oops", "invalid username/password")


def quit():
    qb.destroy()


label = Label(frame1, text='BILLING SYSTEM LOGIN', font=('Times New Roman', 26 ), bg='orange2', fg='white')
label.place(x=40, y=50)
usernamelabel = Label(frame1, text='USERNAME', font=('Times New Roman', 22), bg='deep pink', fg='white', bd=5)
usernamelabel.place(x=15, y=200)
passwordlabel = Label(frame1, text='PASSWORD', font=('Times New Roman', 20), bg='deep pink', fg='white', bd=5)
passwordlabel.place(x=15, y=300)
entry1 = Entry(frame1, font=('Times New Roman', 18), show="*", bg="white", fg="red", bd=5)
entry1.place(x=200, y=200)
entry2 = Entry(frame1, font=("Times New Roman", 18), show="*", bg='white', fg='red', bd=5)
entry2.place(x=200, y=300)
loginbtn = Button(frame1, text="LOGIN", font=('Times New Roman', 25), bg='medium blue', fg='white',
                  command=lambda: login())
loginbtn.place(x=90, y=400)
quitbtn = Button(frame1, text="QUIT", font=('Times New Roman', 25), bg='medium blue', fg='white', command=lambda: quit())
quitbtn.place(x=290, y=400)
qb.mainloop()
