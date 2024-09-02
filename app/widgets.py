import tkinter as tk
from tkinter import ttk
from db import*
from commands import *


top_frame = tk.Frame()
top_frame.pack(fill="both",side="top")
bottom_frame = tk.Frame()
bottom_frame.pack(fill="x",side="bottom")

mm_lframe = tk.LabelFrame(top_frame,text="Mini-market")
gs_lframe = tk.LabelFrame(top_frame,text="Yanacaqdoldurma")
pa_lframe = tk.LabelFrame(bottom_frame,text="Ödəniş")
gs_lframe.pack(fill="x",expand="yes", side="left",padx=15,pady=5)
mm_lframe.pack(fill="x",expand="yes",side="left",padx=15,pady=5)
pa_lframe.pack(fill="x",expand="yes",side="bottom",padx=15,pady=5)

def onCheckButtonchange(var,name):
    if var.get()==1:
        print(f"{name} checkbutton aciqdi")
    else:
        print(f"{name} checkbutton baglidir")


hdCheckVar= tk.IntVar()
hbCheckVar= tk.IntVar()
FriesCheckVar = tk.IntVar()
ColaCheckVar = tk.IntVar()
# mm_lframe

hot_dog_frame = tk.Frame(mm_lframe)
hotdog_subframe = tk.Frame(hot_dog_frame)
hot_dog_frame.pack(side="top",fill="x",expand="yes",padx=10,pady=10)
hot_dog_cbutton = tk.Checkbutton(hotdog_subframe,text="Hotdog",relief="groove",onvalue=1,offvalue=0,variable=hdCheckVar,command=lambda :onCheckButtonchange(hdCheckVar,"Hotdog"))
hot_dog_cbutton.pack()
hotdog_subframe.pack(side="left")
hamburger_cbutton = tk.Checkbutton(hotdog_subframe,text="Hamburger",relief="groove",onvalue=1,offvalue=0,variable=hbCheckVar,command=lambda :onCheckButtonchange(hbCheckVar,"Hamburger"))
hamburger_cbutton.pack()

Fries_frame = tk.Frame(mm_lframe)
Fries_subframe = tk.Frame(hot_dog_frame)
Fries_frame.pack(side="top",fill="x",expand="yes",padx=10,pady=10)
Fries_cbutton = tk.Checkbutton(hotdog_subframe,text="Fries",relief="groove",onvalue=1,offvalue=0,variable=FriesCheckVar,command=lambda :onCheckButtonchange(hdCheckVar,"Fries"))
Fries_cbutton.pack()
hotdog_subframe.pack(side="left")
Cola_cbutton = tk.Checkbutton(hotdog_subframe,text="Cola",relief="groove",onvalue=1,offvalue=0,variable=ColaCheckVar,command=lambda :onCheckButtonchange(hbCheckVar,"Coke"))
Cola_cbutton.pack()

entervalue_frame = tk.Frame(mm_lframe)
entervalue_frame.pack(fill="x",expand="yes",pady=10)


cola_entry = tk.Entry(mm_lframe,width = 10,state="readonly")
cola_entry.pack(fill="x",expand="yes",side="left")
fries_entry = tk.Entry(mm_lframe,width = 10)
fries_entry.pack(fill="x",expand="yes",side="left")

# label2 = tk.Label(mm_lframe,text="hotdog")
# label2.pack(side="left")

# gs_lframe


gasselect_frame = tk.Frame(gs_lframe)
gasselect_frame.pack(fill="x",expand="yes")
gas_lbl = tk.Label(gasselect_frame,text="Benzin")
gas_lbl.pack(side="left",padx=15)
gas_cbox = ttk.Combobox(gasselect_frame,values=["A-92","A-95","A-98","Dizel"])
gas_cbox.bind("<<ComboboxSelected>>",lambda event:gas_combo_changed(gas_cbox))
selected_option = gas_cbox.get()
gas_cbox.pack(side="left",fill="x",expand="yes",padx=15)

gasprice_frame = tk.Frame(gs_lframe)
gasprice_frame.pack(fill="x",expand="yes",pady=20)
gprice_lbl = tk.Label(gasprice_frame,text="Qiyməti")
gprice_lbl.pack(side="left",padx=15)

gprice_ety = tk.Entry(gasprice_frame,state="readonly",textvariable=selected_price)
gprice_ety.pack(side="left",fill="x",expand="yes",padx=15)

entervalue_frame = tk.Frame(gs_lframe)
entervalue_frame.pack(fill="x",expand="yes",pady=20)

radio_lframe = tk.LabelFrame(entervalue_frame)
radio_lframe.pack(fill="x",expand="yes",side="left",padx=15)

entries_frame = tk.Frame(entervalue_frame)
entries_frame.pack(fill="x",expand="yes",side="left",padx=15)


litre_radio = tk.Radiobutton(radio_lframe,text="Litrlə",variable=radiovar,value=1,command=lambda :entryselect_radio_changed(litre_entry,cash_entry,radiovar))
litre_radio.pack()
cash_radio = tk.Radiobutton(radio_lframe,text="Pulla",variable=radiovar,value=2,command=lambda :entryselect_radio_changed(litre_entry,cash_entry,radiovar))
cash_radio.pack()

litre_entry = tk.Entry(entries_frame)
litre_entry.pack(fill="x",expand="yes")
cash_entry = tk.Entry(entries_frame,state="disabled")
cash_entry.pack(fill="x",expand="yes")


# label2 = tk.Label(mm_lframe,text="hotdog")
# label2.pack()
checkout_btn = tk.Button(pa_lframe,text="Ödə",padx=10,pady=5)
checkout_btn.pack()

window.mainloop()