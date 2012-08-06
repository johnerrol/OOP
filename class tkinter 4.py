import tkinter
class Application(tkinter.Frame):
    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.pack()
        self.points=0
        self.Morningbutton=tkinter.Button()
        self.Morningbutton["text"]= "clickhere"
        self.Morningbutton["command"]=self.morning
        self.Morningbutton.pack()

        self.AfternoonButton=tkinter.Button()
        self.AfternoonButton["text"]= "clickme"
        self.AfternoonButton["command"]=self.afternoon
        self.AfternoonButton.pack()

        self.GwapoakoButton=tkinter.Button()
        self.GwapoakoButton["text"]="click"
        self.GwapoakoButton["command"]=self.gwapoako
        self.GwapoakoButton.pack()
        
        self.pointsbutton=tkinter.Button()
        self.pointsbutton["text"]= "points"
        self.pointsbutton["command"]=self.Displaypoints
        self.pointsbutton.pack()

        self.quitbutton=tkinter.Button()
        self.quitbutton["text"]= "quit"
        self.quitbutton["command"]=self.exit
        self.quitbutton.pack()


    def morning(self):
        response=tkinter.messagebox.showinfo("Question #1 Is  Yellow Sun Yellow?")
        if(response==True):
            self.points+=1
    def afternoon(self):
          response=tkinter.messagebox.showinfo("Question#2 Is Wood Edible?")
          if(response==False):
              self.points+=1
              tkinter.messagebox.showinfo("Results","Total Points is %i" %(points))
    def gwapoako(self):
          response=tkinter.messagebox.showinfo("Question #3 Is Fried Chickren Madc Of Pigs?")
          if(response==True):
               self.points+=1
    def exit(self):
        response=tkinter.messagebox.askyesno("Your Total Points Is 2?")
        if(response==True):
            self.points+=1
    def displaypoints(self):
        if(response==True):
            self.points+=1
       
root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()
