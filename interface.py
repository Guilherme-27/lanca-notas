from tkinter import *
from tkinter import ttk, Text, Scrollbar
from app import abrir_chrome, lancar_notas, carregar_csv


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="Abrir Chrome", command=abrir_chrome).grid(column=0, row=0)
ttk.Button(frm, text="Carregar CSV", command=carregar_csv).grid(column=0, row=1)
ttk.Button(frm, text="Lançar notas", command=lancar_notas).grid(column=0, row=2)



root.mainloop()