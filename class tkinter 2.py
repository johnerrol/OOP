import tkinter
class Application(tkinter.Frame):
    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.pack()
        
        self.Morningbutton=tkinter.Button()
        self.Morningbutton["text"]= "morning"
        self.Morningbutton["command"]=self.morning
        self.Morningbutton.pack()

        self.AfternoonButton=tkinter.Button()
        self.AfternoonButton["text"]= "afternoon"
        self.AfternoonButton["command"]=self.afternoon
        self.AfternoonButton.pack()

        self.GwapoakoButton=tkinter.Button()
        self.GwapoakoButton["text"]="evening"
        self.GwapoakoButton["command"]=self.gwapoako
        self.GwapoakoButton.pack()
        
        self.quitbutton=tkinter.Button()
        self.quitbutton["text"]= "quit"
        self.quitbutton["command"]=self.exit
        self.quitbutton.pack()

    def morning(self):
        tkinter.messagebox.showinfo("Greetings","Good Morning")
    def afternoon(self):
          tkinter.messagebox.showinfo("Greetings","good afternoon")
    def gwapoako(self):
          tkinter.messagebox.showinfo("Greetings","good evening")
    def exit(self):
        response=tkinter.messagebox.askyesno("Bye bye?","Do You Want To Quit?")
        if(response==True):
            self.quit()
            
root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()
