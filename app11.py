import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x600")

# first_frame = tk.Frame(width=10,height=10,bd=2)
# first_frame.pack(side="bottom")
# second_frame = tk.Frame()
# second_frame.pack(side="top")

# label = tk.Label(text = "Ilk framin ilk label i",font=("Helvetica",18),bg="red")
# label.pack()

bottom_frame = tk.Frame()
bottom_frame.pack(fill="x",side="bottom")
# black_button = tk.Button(bottom_frame,text="Black",borderwidth=2,font=("Helvetice",18),fg="black")
# black_button.pack()

top_frame = tk.Frame()
top_frame.pack(side="top",fill="both")
# blue_button = tk.Button(top_frame,text="Blue",borderwidth=2,font=("Helvetice",18),fg="blue")
# blue_button.pack(side = "right")
# brown_button = tk.Button(top_frame,text="Brown",borderwidth=2,font=("Helvetice",18),fg="brown")
# brown_button.pack(side="right")
# red_button = tk.Button(top_frame,text="Red",borderwidth=2,font=("Helvetice",18),fg="red")
# red_button.pack(side="right")

gasprice_dict={
    "A-92":1.1,
    "A-95":1.6,
    "A-98":2,
    "DIZEL":1

}

def gas_combo_changed(event):
    seleceted_option = gas_cbox.get()
    selected_price.set(gasprice_dict[seleceted_option])

def entryselect_radio_changed():
    value = radiovar.get()
    if value==1:
        litre_entry.config(state="normal")
        cash_entry.config(state="disabled")
    else:
        litre_entry.config(state="normal")
        cash_entry.config(state="disabled")

selected_price = tk.DoubleVar()

mm_lframe = tk.LabelFrame(text = "Mini Market")
gs_lframe = tk.LabelFrame(text = "Yanacaqdoldurma")
pa_lframe = tk.LabelFrame(text = "Odenis")
mm_lframe.pack(fill="x",expand="yes",side ="left",padx=15,pady=5)
gs_lframe.pack(fill="x",expand="yes",side ="left",padx=15,pady=5)
pa_lframe.pack(fill="x",expand="yes",side ="bottom",padx=15,pady=5)

label = tk.Label(gs_lframe,text="Benzin")
label2 = tk.Label(mm_lframe,text = "hotdog")
label.pack()
label2.pack()

checkout_btn = tk.Button(pa_lframe,text="Ode",padx=10,pady=5)
checkout_btn.pack()
gasselect_frame = tk.Frame(gs_lframe)
gasselect_frame.pack(side="left",padx=15)
gas_lbl = tk.Label(gasselect_frame,text="Benzin")
gas_lbl.pack(side = "left",padx=15)
gas_cbox = ttk.Combobox(gs_lframe,values=["A-92",'A-95','A-98','DIZEL'])
gas_cbox.bind("<<ComboboxSelected",gas_combo_changed)
selected_option = gas_cbox.get()
gas_cbox.pack(side = "left",fill="x",expand ="yes",pady=15)

gasprice_frame = tk.Frame(gs_lframe)
gasprice_frame.pack(fill="x",expand="yes",pady=20)
gprice_lbl = tk.Label(gasprice_frame,text="Qiymet")
gprice_lbl.pack(side="left",padx=15)

gprice_ety = tk.Entry(gasprice_frame,state="readonly",textvariable=selected_price)
gprice_ety.pack(side="left",padx=15)

entervalue_frame = tk.Frame(gs_lframe)
entervalue_frame.pack(fill="x",expand="yes",pady=20)

radio_lframe = tk.LabelFrame(entervalue_frame)
radio_lframe.pack(fill="x",expand="yes",side="left",padx=15)

entries_frame = tk.Frame(gs_lframe)
entervalue_frame.pack(fill="x",expand="yes",side="left",padx=15)

radiovar = tk.IntVar(value=1)
litre_radio = tk.Radiobutton(radio_lframe,text="Litirle",variable=radiovar,value=1,command=entryselect_radio_changed)
litre_radio.pack()
cash_radio=tk.Radiobutton(radio_lframe,text = "Pulla",variable=radiovar,value=2,command=entryselect_radio_changed)
cash_radio.pack()

litre_entry = tk.Entry(entries_frame)
litre_entry.pack(fill="x",expand="yes")
cash_entry = tk.Entry(entries_frame,state="disabled")
cash_entry.pack(fill="x",expand="yes")


window.mainloop()