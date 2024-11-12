import tkinter

class Favorite_Saying:
    def __init__(self):
        # Create window
        self.main_window = tkinter.Tk()

        # Create label
        self.saying = tkinter.Label(self.main_window, text = "Hard work beats talent when talent doesn't work hard")

        # Pack label
        self.saying.pack()

        tkinter.mainloop()

favorite_saying = Favorite_Saying()