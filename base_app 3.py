import tkinter


class Application(tkinter.Frame):
    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.pack()
        self.CreateWidget()
    def  CreateWidget(self):
        self.textbox1=tkinter.Text()
        self.textbox1.pack()
        self.button1=tkinter.Button()
        self.button1["command"]=self.button1_click
        self.button1["text"]="click"
        self.button1.pack()
    def button1_click(self):
       pass
    def button1_click(self):
        print("%s" %(self.textbox1.get(0.0,tkinter.END)))
    
root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()        
