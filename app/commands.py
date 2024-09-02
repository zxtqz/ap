from db import*

# def entryselect_radio_changed():
#     value = radiovar.get()
#     if value==1:
#         litre_entry.config(state="normal")
#         cash_entry.config(state="disabled")
#     else:
#         litre_entry.config(state="disabled")
#         cash_entry.config(state="normal")

# def gas_combo_changed(event):
#     selected_option = gas_cbox.get()
#     selected_price.set(gasprice_dict[selected_option])

gasprice_dict = {
    "A-92":1.1,
    "A-95":1.6,
    "A-98":2,
    "Dizel":0.9
}

def gas_combo_changed(cbox):
    selected_option = cbox.get()
    selected_price.set(gasprice_dict[selected_option])

def entryselect_radi_changed(first_entry,second_entry,radiovar):
    value = radiovar.get()
    if value==1:
        first_entry.config(state="normal")
        second_entry.config(state="disabled")
    else:
        first_entry.config(state="disabled")
        second_entry.config(state="normal")

