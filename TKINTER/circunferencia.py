import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt 
import numpy as np
import math as m
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as fgc

class appCirc ():
    def __init__(self):
        #Root setup
        self.root = tk.Tk()
        self.root.geometry('770x520+1700+20')
        self.root.title('Circunferencia')
        #Set title from root
        self.title_r = ttk.Label(self.root,text='Grafico Circunferencia',font=('Monocraft',20))
        self.title_r.pack(side='top')
        #Set mainframe up
        self.mainframe = tk.Frame(self.root,background='grey')
        self.mainframe.pack(side='bottom',fill='both',expand=True)
        #Set labels.
        self.h_label = ttk.Label(self.mainframe,text='Valor de H >>',font=('Monocraft',15))
        self.h_label.grid(row=1,column=1,padx=5,pady=10,sticky='NWES')
        #Ser K label
        self.k_label =ttk.Label(self.mainframe,font=('Monocraft',15),text='Valor de K >>')
        self.k_label.grid(row=2,column=1,padx=5,pady=10,sticky='NWES')
        #Set R Label
        self.r_label = ttk.Label(self.mainframe,text='Valor de Radio >>',font=('Monocraft',15))
        self.r_label.grid(row=3,column=1,padx=5,pady=10,sticky='NWES')
        #Set entry h
        self.h_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.h_entry.grid(row=1,column=2,padx=5,pady=10,sticky='NWES')
        #Set entry k
        self.k_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.k_entry.grid(row=2,column=2,padx=5,pady=10,sticky='NWES')
        #Set Entry r
        self.r_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.r_entry.grid(row=3,column=2,padx=5,pady=10,sticky='NWES')

        self.save = tk.Button(self.mainframe,text='Guardar y graficar!',font=('Monocraft',17),command=self.plot_g).grid(row=5,column=1,padx=5,pady=10)

        self.root.mainloop()
    def menu (self):
        self.clear()
        self.h_label = ttk.Label(self.mainframe,text='Valor de H >>',font=('Monocraft',15))
        self.h_label.grid(row=1,column=1,padx=5,pady=10,sticky='NWES')
        #Ser K label
        self.k_label =ttk.Label(self.mainframe,font=('Monocraft',15),text='Valor de K >>')
        self.k_label.grid(row=2,column=1,padx=5,pady=10,sticky='NWES')
        #Set R Label
        self.r_label = ttk.Label(self.mainframe,text='Valor de Radio >>',font=('Monocraft',15))
        self.r_label.grid(row=3,column=1,padx=5,pady=10,sticky='NWES')
        #Set entry h
        self.h_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.h_entry.grid(row=1,column=2,padx=5,pady=10,sticky='NWES')
        #Set entry k
        self.k_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.k_entry.grid(row=2,column=2,padx=5,pady=10,sticky='NWES')
        #Set Entry r
        self.r_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.r_entry.grid(row=3,column=2,padx=5,pady=10,sticky='NWES')

        self.save = tk.Button(self.mainframe,text='Guardar y graficar!',font=('Monocraft',17),command=self.plot_g).grid(row=5,column=1,padx=5,pady=10)

    def clear (self):
        x = self.mainframe.grid_slaves()
        for i in x:
            i.destroy()
    
    def plot_g (self):
        global r,k,h 

        r = float(self.r_entry.get())
        k = float(self.k_entry.get())
        h = float(self.h_entry.get())

        t = np.linspace(0,2*m.pi)
        xlist = r*np.cos(t)
        ylist = r*np.sin(t)
        xlist_h =xlist+h
        ylist_k = ylist+k
        self.clear()

        fig = plt.figure(figsize=(4,4),dpi=100)
        fig.add_subplot(111).plot(xlist_h,ylist_k)
        plot = fgc(fig, self.mainframe)
        plot.get_tk_widget().grid(row=1,column=1,padx=10,pady=15,sticky='NWES')
        plt.grid()
        plt.axhline(0,color='black')
        plt.axvline(0,color='black')
        plt.scatter([h],[k])

        self.volver = tk.Button(self.mainframe,text='Volver a Menu Principal',font=('Monocraft',15),command=self.menu)
        self.volver.grid(row=1,column=2,padx=5,pady=10)

if __name__ == '__main__':
    appCirc()