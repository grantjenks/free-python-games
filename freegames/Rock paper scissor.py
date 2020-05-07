# exercise
# Keep the count of wins
# Ask user If he wants to continue



from tkinter import *
import tkinter.font as tkFont
import random as r

class app():
    
    def __init__(self, obj):
        self.obj = obj
        self.obj.title("User Interface")
        self.height = self.obj.winfo_screenheight() 
        self.width = self.obj.winfo_screenwidth()
        self.app_width = int(0.5*self.width)
        self.app_length = int(0.5*self.height)
        self.obj.geometry(str(self.app_width)+"x"+str(self.app_length))
        
    def letsplay(self):
            
            
        def logic1(entrybox,game):

                computer_choice = r.choice(["P", "R", "S"])
                text = entrybox.get()
                if 'R' in text:
                    label1 = Label(game, text= "you Entered "+str(text) )
                    label1.pack()
                elif "P" in text:
                    label1 = Label(game, text= "you Entered "+str(text) )
                    label1.pack()            
                elif "S" in user_choice:
                    label1 = Label(game, text= "you Entered "+str(text) )
                    label1.pack()
                else:
                    label1 = Label(game, text= "you Entered "+str(text) )
                    label1.pack()           


                if "R" in computer_choice:
                    label1 = Label(game, text= "computer Entered "+str(computer_choice) )
                    label1.pack()
                elif "P" in computer_choice:
                    label1 = Label(game, text= "computer Entered "+str(computer_choice) )
                    label1.pack()
                else:
                    label1 = Label(game, text= "computer Entered "+str(computer_choice) )
                    label1.pack()


                if text == 'R':
                    if computer_choice == "R":
                        label1 = Label(game, text= "Match Draw" )
                        label1.pack()
                    elif computer_choice == "P":
                        label1 = Label(game, text= "computer won" )
                        label1.pack()
                    else:
                        label1 = Label(game, text= "You won" )
                        label1.pack()

         



        # if user choose Paper as "P"

                elif text == 'P':

                    if computer_choice == 'P':
                        label1 = Label(game, text= "Match Draw" )
                        label1.pack()
                    elif computer_choice == 'R':
                        label1 = Label(game, text= "computer won" )
                        label1.pack()
                    else:
                        label1 = Label(game, text= "You won" )
                        label1.pack()

        # if user choose Scissors as "S"

                else:
                    if computer_choice == 'S':
                        label1 = Label(game, text= "You won" )
                        label1.pack()
                    elif computer_choice == 'R':
                        label1 = Label(game, text= "You won" )
                        label1.pack()
                    else:
                        label1 = Label(game, text= "You won" )
                        label1.pack()
                return           
                        
                
        game=Tk()
        e=Entry(game, width=30,bg='yellow')
        button = Button(game,text='okay',command= lambda:logic1(e,game),bg='green')
        button.pack()
        
        label1 = Label(game, text= "Type your choice for Rock R, for paper P ,  for scissors S  : " )
        label1.pack()
        
        e.pack()
        
    def start_app(self):
        
        
        welcome = tkFont.Font(family='arial', size=55)
        welcome = Label(self.obj, text='Rock paper  \n\n\n',font=welcome,background="green")
        welcome.pack(fill='both', expand=True, anchor=CENTER)
        
        
        
        button = Button(self.obj,text='Lets play',command= lambda: self.letsplay())
        button.pack()
        
                   
        
if __name__ == "__main__": 
    object1 = Tk()
    object2 = app(object1)
    object2.start_app()
    object1.mainloop()        
