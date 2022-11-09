import tkinter as tk 
from tkinter import ttk
import matplotlib.pyplot as plt
import math as m
import numpy as np
from sympy import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as fgc


class AppPar ():
    def __init__(self):
        #Set up Root
        self.root = tk.Tk()
        self.root.title('Plot Parabola.')
        self.root.geometry(f'950x770+1700+10')
        #Set Mainframe
        self.mainframe = tk.Frame(self.root, background='grey')
        self.mainframe.columnconfigure(0,weight=1)
        self.mainframe.pack(fill='both', expand=True)
        #Set title label
        self.title = ttk.Label(self.mainframe,text='Parabola',font=('Arial',20),background='grey80')
        self.title.grid(row=0,column=0, sticky='ew',columnspan=2,pady=10)
        self.title.configure(anchor='center')
        #Set label 1(A)
        self.label_A = ttk.Label(self.mainframe,text='Valor A',font=('Arial',15),background='white')
        self.label_A.grid(row=1,column=0,sticky='NWES',pady=0,padx=15)
        #Set first textbox
        self.text_A = ttk.Entry(self.mainframe)
        self.text_A.grid(row=1,column=0,pady=10)
        #Set Label 2 (B)
        self.label_B = ttk.Label(self.mainframe,text='Valor B', font=('Arial',15),background='white')
        self.label_B.grid(row=2,column=0,sticky='NWES',pady=0,padx=15)
        #Set second textbox
        self.text_B = ttk.Entry(self.mainframe)
        self.text_B.grid(row=2,column=0,pady=10)
        #Set Label 3 (C)
        self.label_C = ttk.Label(self.mainframe, text='Valor C',font=('Arial',15),background='white')
        self.label_C.grid(row=3,column=0,padx=15,sticky='NWES')
        #Set third textbox
        self.text_C = ttk.Entry(self.mainframe)
        self.text_C.grid(row=3,column=0, pady=10)
        #Set 'Calcular' button
        self.calcular = ttk.Button(self.mainframe,text='Calcular puntos de corte',command=self.px_cort)
        self.calcular.grid(row=5, column=0,pady=10,padx=5)
        #Set 'Graficar' button
        self.graficar = ttk.Button(self.mainframe, text='Graficar',command=self.plot_par)
        self.graficar.grid(row=6, column=0,padx=5,pady=10)
        


        self.root.mainloop()

    def px_cort (self):
        a = int(self.text_A.get())
        b = int(self.text_B.get())
        c = int(self.text_C.get())
        r = (pow(b,2)-4*a*c)
        

        if r>0:
            cort_x1 = float(-b+m.sqrt(r))
            cort_x2 = float(-b-m.sqrt(r))

            self.tit_labelx1 = ttk.Label(self.mainframe,text="X1                                                                      X2",font=('Arial',20),background='grey76')
            self.tit_labelx1.grid(row=7,column=0, padx=15,pady=10,sticky='ew')
            self.tit_labelx1.configure(anchor='w')

            self.label_cort = ttk.Label(self.mainframe,text=f'{cort_x1}                                                                                         {cort_x2}',font=('Arial',10))
            self.label_cort.grid(row=8, column=0, padx=20,sticky='ew')
        elif r ==0:
            x3 = -b/2*a
            self.tit_labelx3 = ttk.Label(self.mainframe,text=f"X1                 {x3}",font=('Arial',20),background='grey76')
            self.tit_labelx3.grid(row=7,column=0, padx=15,pady=10,sticky='ew')
        
        elif r<0:
            self.tit_label = ttk.Label(self.mainframe,font=('Arial',20),text='La parabola no corta x')
            self.tit_label.grid(row=7,column=0,padx=20,sticky='ew')
            self.tit_label.configure(anchor='center')
        

    def fun(self,x,a,b,c):
        return a*(x**2)+(b*x)+c

    def plot_par(self):

        a = int(self.text_A.get())
        b = int(self.text_B.get())
        c = int(self.text_C.get())

        xlist=np.linspace(-10,10,num=1000)
        ylist =self.fun(xlist,a,b,c)

        fig = plt.figure(figsize=(4,4), dpi=100)
        fig.add_subplot(111).plot(xlist,ylist)
        
        plot = fgc(fig, self.mainframe)
        plot.get_tk_widget().grid(row=9,column=0)
        plt.grid()
        plt.axhline(0,color='black')
        plt.axvline(0,color='black')
        

if __name__ == '__main__':
    AppPar()