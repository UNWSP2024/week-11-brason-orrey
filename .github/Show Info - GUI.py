import tkinter

class ShowInfoGUI:
    def __init__(self):
        # Create window
        self.main_window = tkinter.Tk()

        # Create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create label
        self.value = tkinter.StringVar()
        self.address = tkinter.Label(self.top_frame, textvariable = self.value)

        # Create buttons
        self.address_button = tkinter.Button(self.bottom_frame, text = "Show Info",
        command = self.show_info)
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Quit",
        command = self.main_window.destroy)

        # Pack label
        self.address.pack()

        # Pack button
        self.address_button.pack(side = "left")
        self.quit_button.pack(side = "left")

        # Pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_info(self):
        self.value.set("Brason Orrey\n11764 Naples Cir NE\n Blaine, MN 55449")

show_info = ShowInfoGUI()
