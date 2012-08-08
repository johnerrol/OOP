import tkinter


class Application(tkinter.Frame):
    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.config(width=1000)
        self.config(height=200)
        self.config(bg="#FF0000")
        self.pack()
        self.CreateWidget()
    def  CreateWidget(self):
        pass

root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()        
