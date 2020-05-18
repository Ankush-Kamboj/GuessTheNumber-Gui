import tkinter as tk
import random

class GuessTheNumber:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("410x160")
        self.root.title("Guess the number")
        self.root.resizable('false', 'false')

        self.user_num = tk.IntVar()
        self.random_num = random.randint(1,21)
        self.count = 3

        welcomelabel = tk.Label(self.root, text = """Welcome to the Guess the Number Game.
      In this game you will have to guess the number randomly generated by 
      computer. You will get 3 chances to get the number. Enjoy the game""")
        welcomelabel.place(x = 0, y = 0)

        chancesLeftLabel = tk.Label(self.root, text="Chances left:")
        chancesLeftLabel.place(x = 310, y = 60)

        self.chancesLabel = tk.Label(self.root, text = self.count)
        self.chancesLabel.place(x = 385, y = 60)

        userNumLabel = tk.Label(self.root, text="Enter a Number between 1-20:")
        userNumLabel.place(x = 10, y =90)

        self.userNumEntry = tk.Entry(self.root, textvariable = self.user_num)
        self.userNumEntry.place(x = 183, y = 90)
        self.userNumEntry.delete(0,'end')

        self.userNumError = tk.Label(self.root, text="")
        self.userNumError.place(x = 183, y = 110)

        self.playButton = tk.Button(self.root, text = "Play", command=self.game, width = 10)
        self.playButton.place(x = 320, y = 88)

        self.resultLabel = tk.Label(self.root, text = "")
        self.resultLabel.place(x = 130, y = 125)
    
    def game(self):
        self.userNumError.config(text = "")
        if self.checkUserNum():
            self.logic()

    def logic(self):    
        if self.user_num.get() == self.random_num:
            self.playButton["state"] = "disabled"
            self.resultLabel.config(text="You Win!!, number was " + str(self.random_num) + ".")
            self.again()
        elif self.user_num.get() > self.random_num:
            self.resultLabel.config(text="Your number is High.")
        else:
            self.resultLabel.config(text="Your number is Low.")

        self.count -= 1
        self.chancesLabel.config(text = self.count)
        self.userNumEntry.delete(0,"end")
        if self.count <= 0:
            self.playButton["state"] = "disabled"
            self.resultLabel.config(text="You Lose!!, number was " + str(self.random_num)+".")
            self.again()


    def again(self):
        self.root.geometry("410x190")

        self.resetButton = tk.Button(self.root, text = "Reset", command = self.reset, width = 10)
        self.resetButton.place(x = 20, y = 155)

        self.exitButton = tk.Button(self.root, text = "Exit", command = exit, width = 10)
        self.exitButton.place(x = 310, y = 155)


    def checkUserNum(self):
        bool = False
        
        try:
            if self.user_num.get() < 21 and self.user_num.get() > 0:
                bool = True
            else:
                self.userNumError.config(text="*Enter a valid number")
        except tk.TclError:
            self.userNumEntry.delete(0,'end')
            self.userNumError.config(text = "*Enter a valid number")

        return bool
        
    def reset(self):
        self.count = 3
        self.playButton["state"] = "active"
        self.chancesLabel.config(text = self.count)
        self.random_num = random.randint(1,21)
        self.resetButton.place_forget()
        self.exitButton.place_forget()
        self.resultLabel.config(text="")
        self.root.geometry("410x160")


    def showDialog(self):
        self.root.mainloop()


if __name__ == "__main__":
    obj = GuessTheNumber()
    obj.showDialog()