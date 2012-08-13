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
        
        
        self.button2=tkinter.Button()
        self.button2["command"]=self.button2_save
        self.button2["text"]="save"
        self.button2.pack()

        
        self.button3=tkinter.Button()
        self.button3["command"]=self.button3_load
        self.button3["text"]="load"
        self.button3.pack()

        
    def button1_click(self):
        text=self.textbox.get(0.0,tkinter.END)
        print(text.upper())
        print(text.lower())
        print(text.title())

    def button2_save(self):
        text=self.textbox1.get(0.0,tkinter.END)
        f=open("quote.txt","w")
        f.write(text)
        f.close()
    def button3_load(self):
        pass
    

root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()        
