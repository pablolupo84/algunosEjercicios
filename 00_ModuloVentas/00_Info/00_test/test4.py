import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.tree = ttk.Treeview()
        

        self.tree.pack()
        list=[("manzanas",10),("peras",5)]
        for i in list:
            self.tree.insert("", "end", text="Item %s" % i[0])
        self.tree.bind("<Double-1>", self.OnDoubleClick)
        self.root.mainloop()

    def OnDoubleClick(self, event):
        item = self.tree.selection()[0]
        print("you clicked on", self.tree.item(item,"text"))

#if __name__ == "__main__":
 #   app = App()

ventana=App()