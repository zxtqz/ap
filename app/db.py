import tkinter as tk

window = tk.Tk()
window.geometry("600x600")

gasprice_dict={
    "A-92":1.1,
    "A-95":1.6,
    "A-98":2,
    "DIZEL":1

}

selected_price = tk.DoubleVar(window)
radiovar = tk.IntVar(window,value=1)

