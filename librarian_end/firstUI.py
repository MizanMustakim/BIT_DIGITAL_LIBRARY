from tkinter import *
from secondUI import *
from secondUI import Scan_APP
from thirdUI import RetrieveApp
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from PIL import ImageTk, Image

class App:
    def __init__(self, root):
        self.root = root
        #setting title
        self.root.title("Digital Library")
        #setting window size
        self.width=717
        self.height=399
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (self.width, self.height, (screenwidth - self.width) / 2, (screenheight - self.height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)
        self.root.configure(bg='#E9EDC9')

        self.background_image = PhotoImage(file="./librarian_end/library.png")  # Change to your image file
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        '''Welcome Title'''
        ft = tkFont.Font(family='Times', size=16, weight='bold')

        # Create a label for "BIT Digital Library"
        welcome_title = tk.Label(self.root, text="BIT Digital Library", font=ft)

        # Place the label on top of the background image
        welcome_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        
        '''Scan Button'''
        scan=tk.Button(self.root)
        scan["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10, weight='bold')
        scan["font"] = ft
        scan["fg"] = "#000000"
        scan["bg"] = "#f2cf1d"
        scan["justify"] = "center"
        scan["text"] = "Scan & Store"
        scan.place(x=130,y=130,width=156,height=69)
        scan["command"] = self.scan_command

        '''Data Retrieval'''
        data_retrieval=tk.Button(self.root)
        data_retrieval["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10, weight='bold')
        data_retrieval["font"] = ft
        data_retrieval["fg"] = "#000000"
        data_retrieval["bg"] = "#4ddb73"
        data_retrieval["justify"] = "center"
        data_retrieval["text"] = "Data Retrieval"
        data_retrieval.place(x=420,y=130,width=156,height=69)
        data_retrieval["command"] = self.data_retrieval_command

        '''Quit Button'''
        quit_button=tk.Button(self.root)
        quit_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        quit_button["font"] = ft
        quit_button["fg"] = "#000000"
        quit_button["bg"] = "#8ca3ed"
        quit_button["justify"] = "center"
        quit_button["text"] = "Quit"
        quit_button.place(x=620,y=360,width=70,height=25)
        quit_button["command"] = self.quit_button_command

        

    def scan_command(self):
        # self.root.destroy()
        root2 = tk.Toplevel(self.root)
        # root2.attributes('-topmost', True)
        app2 = Scan_APP(root2)
        root2.grab_set()
        root2.mainloop()
        # self.root.destroy()
        

    def data_retrieval_command(self):
        root3 = tk.Toplevel(self.root)
        app3 = RetrieveApp(root3)
        root3.grab_set()
        root3.mainloop()
        # self.root.destroy()

    def quit_button_command(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
