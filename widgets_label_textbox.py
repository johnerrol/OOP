import tkinter


class Application(tkinter.Frame):
    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.pack()
        self.CreateWidget()
    def  CreateWidgets(self):
        pass
    def  CreateWidgets(self):
        self.label1=Tkinter.Label(self)
        self.label1=config(text="Hello World")
        self.label1.pack()
 
root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()        
