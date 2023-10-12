import tkinter as tk
import tkinter.font as tkFont
from tkinter import PhotoImage
from tkinter import ttk  # Import ttk module for Treeview
from merge import SearchDB

class ResultsWindow:
    def __init__(self, root, data):
        self.root = root
        self.root.title("Search Results")
        self.root.geometry("600x200")

        if data:
            self.display_table(data)
        else:
            self.display_no_data()

    def display_table(self, data):
        tree = ttk.Treeview(self.root, columns=("Title", "Author", "Edition"))
        tree.heading("#1", text="Title")
        tree.heading("#2", text="Author")
        tree.heading("#3", text="Edition")
        tree["show"] = "headings"

        for row in data:
            tree.insert("", "end", values=row)

        tree.pack(fill=tk.BOTH, expand=True)

    def display_no_data(self):
        label = tk.Label(self.root, text="No Data Found!", font=("Times", 16))
        label.pack(pady=50)

class RetrieveApp:
    def __init__(self, root):
        self.root = root

        # Create an instance of SearchDB
        self.db = SearchDB()

        # Setting title
        root.title("Data Retrieve (Librarian)")
        # Setting window size
        width = 730
        height = 426
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Load the background image
        self.background_image = PhotoImage(file="./librarian_end/library2.png")
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        '''Welcome Title'''
        ft = tkFont.Font(family='Times', size=16, weight='bold')
        # Create a label for "BIT Digital Library"
        welcome_title = tk.Label(self.root, text="BIT Digital Library", font=ft, bg="#18ccc6", highlightbackground="#E9EDC9", highlightcolor="#E9EDC9")
        # Place the label on top of the background image
        welcome_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Title Entry
        self.title_entry = tk.Entry(self.root)
        self.title_entry["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times', size=10)
        self.title_entry["font"] = ft
        self.title_entry["fg"] = "#333333"
        self.title_entry["justify"] = "center"
        self.title_entry["text"] = ""
        self.title_entry.place(x=40, y=150, width=221, height=50)

        # Title Label (without background color)
        title_label = tk.Label(self.root, text="Book Name", font=ft, bg="#87db63", highlightbackground="#E9EDC9", highlightcolor="#E9EDC9")
        title_label.place(x=110, y=120, width=88, height=30)

        # Author Entry
        self.author_entry = tk.Entry(self.root)
        self.author_entry["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times', size=10)
        self.author_entry["font"] = ft
        self.author_entry["fg"] = "#333333"
        self.author_entry["justify"] = "center"
        self.author_entry["text"] = ""
        self.author_entry.place(x=300, y=150, width=195, height=50)

        # Author Label (without background color)
        author_label = tk.Label(self.root, text="Author Name", font=ft, bg="#edc16f", highlightbackground="#E9EDC9", highlightcolor="#E9EDC9")
        author_label.place(x=360, y=120, width=88, height=30)

        # Edition Entry
        self.edition_entry = tk.Entry(self.root)
        self.edition_entry["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times', size=10)
        self.edition_entry["font"] = ft
        self.edition_entry["fg"] = "#333333"
        self.edition_entry["justify"] = "center"
        self.edition_entry["text"] = ""
        self.edition_entry.place(x=530, y=150, width=141, height=50)

        # Edition Label (without background color)
        edition_label = tk.Label(self.root, text="Edition", font=ft, bg="#ebed6f", highlightbackground="#E9EDC9", highlightcolor="#E9EDC9")
        edition_label.place(x=570, y=120, width=70, height=30)

        # Search Button
        search_button = tk.Button(self.root)
        search_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        search_button["font"] = ft
        search_button["fg"] = "#000000"
        search_button["justify"] = "center"
        search_button["text"] = "Search"
        search_button.place(x=600, y=220, width=70, height=25)
        search_button["command"] = self.search_button_command

        # Quit Button
        quit_button = tk.Button(self.root)
        quit_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        quit_button["font"] = ft
        quit_button["fg"] = "#000000"
        quit_button["bg"] = "#8ca3ed"
        quit_button["justify"] = "center"
        quit_button["text"] = "Quit"
        quit_button.place(x=600, y=390, width=70, height=25)
        quit_button["command"] = self.quit_button_command

    def search_button_command(self):
        book_name = self.title_entry.get()
        author_name = self.author_entry.get()
        edition = self.edition_entry.get()
        self.db.title = book_name
        self.db.author = author_name
        self.db.edition = edition
        data = self.db.search()  # Assuming search returns a list of data
        self.open_results_window(data)
        print("Book: ", book_name)
        print("Author: ", author_name)
        print("Edition: ", edition)

    def open_results_window(self, data):
        results_window = tk.Toplevel(self.root)
        ResultsWindow(results_window, data)

    def quit_button_command(self):
        self.root.destroy()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = RetrieveApp(root)
#     root.mainloop()
