from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from PIL import ImageTk, Image
from model1 import extract
from merge import Database

class Scan_APP:
    def __init__(self, root):
        self.root = root
        self.photo = None

        self.edited_title = ""
        self.edited_author = ""
        self.edited_edition = ""
        self.edit_button_pressed = False

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

        '''Welcome Title'''
        welcome_title=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=16, weight='bold')
        welcome_title["font"] = ft
        welcome_title["fg"] = "#333333"
        welcome_title["bg"] = "#E9EDC9"
        welcome_title["justify"] = "center"
        welcome_title["text"] = "BIT Digital Library"
        welcome_title.place(x=130,y=30,width=445,height=46)

        '''Scan Label'''
        scan_label=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=14, weight='bold')
        scan_label["font"] = ft
        scan_label["fg"] = "#333333"
        scan_label["bg"] = "#E9EDC9"
        scan_label["justify"] = "center"
        scan_label["text"] = "Scan"
        scan_label.place(x=140,y=80,width=70,height=25)


        '''Photo Label'''
        self.photo_label=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        self.photo_label["font"] = ft
        self.photo_label["fg"] = "#333333"
        self.photo_label["justify"] = "center"
        self.photo_label["text"] = "Photo"
        self.photo_label.place(x=80,y=120,width=185,height=153)

        '''Data Entry Label'''
        dataEntry_label=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=14, weight='bold')
        dataEntry_label["font"] = ft
        dataEntry_label["fg"] = "#333333"
        dataEntry_label["bg"] = "#E9EDC9"
        dataEntry_label["justify"] = "center"
        dataEntry_label["text"] = "Data Entry"
        dataEntry_label.place(x=480,y=80,width=100,height=30)

        '''Title Label'''
        title_label=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        title_label["font"] = ft
        title_label["fg"] = "#333333"
        title_label["bg"] = "#E9EDC9"
        title_label["justify"] = "center"
        title_label["text"] = "Title"
        title_label.place(x=370,y=130,width=30,height=30)

        '''Title Entry'''
        self.title_entry=tk.Entry(self.root)
        self.title_entry["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=10)
        self.title_entry["font"] = ft
        self.title_entry["fg"] = "#333333"
        self.title_entry["justify"] = "left"
        self.title_entry.place(x=410,y=130,width=249,height=30)

        '''Author Label'''
        author_label=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        author_label["font"] = ft
        author_label["fg"] = "#333333"
        author_label["bg"] = "#E9EDC9"
        author_label["justify"] = "center"
        author_label["text"] = "Author"
        author_label.place(x=360,y=190,width=45,height=30)


        '''Author Entry'''
        self.author_entry=tk.Entry(self.root)
        self.author_entry["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=10)
        self.author_entry["font"] = ft
        self.author_entry["fg"] = "#333333"
        self.author_entry["justify"] = "left"
        self.author_entry.place(x=410,y=190,width=250,height=30)

        '''Entry Label'''
        editon_label=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        editon_label["font"] = ft
        editon_label["fg"] = "#333333"
        editon_label["bg"] = "#E9EDC9"
        editon_label["justify"] = "center"
        editon_label["text"] = "Edition"
        editon_label.place(x=360,y=250,width=45,height=30)

        '''Edition Entry'''
        self.edition_entry=tk.Entry(self.root)
        self.edition_entry["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=10)
        self.edition_entry["font"] = ft
        self.edition_entry["fg"] = "#333333"
        self.edition_entry["justify"] = "left"
        self.edition_entry.place(x=410,y=250,width=250,height=30)



        '''Scan Button'''
        scan_button=tk.Button(self.root)
        scan_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        scan_button["font"] = ft
        scan_button["fg"] = "#000000"
        scan_button["justify"] = "center"
        scan_button["text"] = "Scan"
        scan_button.place(x=90,y=300,width=70,height=25)
        scan_button["command"] = self.scan_button_command

        '''Cover Page Upload Button'''
        photo_upload_button=tk.Button(self.root)
        photo_upload_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        photo_upload_button["font"] = ft
        photo_upload_button["fg"] = "#000000"
        photo_upload_button["justify"] = "center"
        photo_upload_button["text"] = "Upload"
        photo_upload_button.place(x=180,y=300,width=70,height=25)
        photo_upload_button["command"] = self.photo_upload_button_command

        '''Edit Button'''
        edit_button=tk.Button(self.root)
        edit_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        edit_button["font"] = ft
        edit_button["fg"] = "#000000"
        edit_button["justify"] = "center"
        edit_button["text"] = "Edit"
        edit_button.place(x=410,y=300,width=70,height=25)
        edit_button["command"] = self.edit_button_command

        '''Check Button'''
        check_button=tk.Button(self.root)
        check_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        check_button["font"] = ft
        check_button["fg"] = "#000000"
        check_button["justify"] = "center"
        check_button["text"] = "Check"
        check_button.place(x=500,y=300,width=70,height=25)
        check_button["command"] = self.check_button_command


        '''Data Upload Button'''
        data_upload_button=tk.Button(self.root)
        data_upload_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        data_upload_button["font"] = ft
        data_upload_button["fg"] = "#000000"
        data_upload_button["justify"] = "center"
        data_upload_button["text"] = "Upload"
        data_upload_button.place(x=590,y=300,width=70,height=25)
        data_upload_button["command"] = self.data_upload_button_command

        '''clear button'''
        clear_button=tk.Button(self.root)
        clear_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        clear_button["font"] = ft
        clear_button["fg"] = "#000000"
        clear_button["justify"] = "center"
        clear_button["text"] = "Clear"
        clear_button.place(x=530,y=360,width=70,height=25)
        clear_button["command"] = self.clear_button_command

        '''Quit Button'''
        quit_button=tk.Button(self.root)
        quit_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        quit_button["font"] = ft
        quit_button["fg"] = "#000000"
        quit_button["justify"] = "center"
        quit_button["text"] = "Quit"
        quit_button.place(x=620,y=360,width=70,height=25)
        quit_button["command"] = self.quit_button_command


    def scan_button_command(self):
        path = self.file_path()
        self.title, self.author = extract(path)
        text_var = tk.StringVar()
        text_var.set(self.title)
        self.title_entry.config(textvariable=text_var)
        self.title_entry.text = text_var

        author_var = tk.StringVar()
        author_var.set(self.author)
        self.author_entry.config(textvariable=author_var)


    def photo_upload_button_command(self):
        self.filepath = filedialog.askopenfilename(title="Open file", filetypes=(("Image files", "*.jpg"), ("Image files", "*.png")), parent=self.root)

        '''Preview the image'''
        if self.filepath:
            image = Image.open(self.filepath)
            image = image.resize((185,153))

            self.photo = ImageTk.PhotoImage(image=image)

            self.photo_label.config(image=self.photo)
            self.photo_label.image = self.photo


    def update_widgets(self, edited_title, edited_author, edited_edition):
        self.edited_title = edited_title
        self.edited_author = edited_author
        self.edited_edition = edited_edition
        '''title update'''
        self.title_entry.delete(0, "end")
        self.title_entry.insert("end", edited_title)

        '''author update'''
        self.author_entry.delete(0, "end")
        self.author_entry.insert("end", edited_author)

        '''edition update'''
        self.edition_entry.delete(0, "end")
        self.edition_entry.insert("end", edited_edition)

    def edit_button_command(self):
        self.edit_button_pressed = True
        edit_root = tk.Toplevel(self.root)
        edit_app = EditApp(edit_root, self.title, self.author, self.update_widgets)
        edit_root.mainloop()

    
    def check_button_command(self):
        if not self.edit_button_pressed:
            self.edited_title = self.title_entry.get()
            self.edited_author = self.author_entry.get()
            self.edited_edition = self.edition_entry.get()

        notification_root = tk.Toplevel(self.root)
        notification_app = NotificationApp(notification_root)    
        db = Database(self.edited_title, self.edited_author, self.edited_edition, notification_app.update_message)
        db.threshold()        


    def data_upload_button_command(self):
        if not self.update_widgets:
            self.edited_title = self.title_entry.get()
            self.edited_author = self.author_entry.get()
            self.edited_edition = self.edition_entry.get()

        notification_root = tk.Toplevel(self.root)
        notification_app = NotificationApp(notification_root)    
        db = Database(self.edited_title, self.edited_author, self.edited_edition, notification_app.update_message)
        db.insert()


    def clear_button_command(self):

        self.title_entry.delete(0, "end")
        self.author_entry.delete(0, "end")
        self.edition_entry.delete(0, "end")

        empty_img = PhotoImage()
        self.photo_label.config(image=empty_img)
        self.photo_label.image = empty_img

        self.title = ""
        self.author = ""


    def quit_button_command(self):
        self.root.destroy()

    def file_path(self):
        return self.filepath

    

class EditApp:
    def __init__(self, root, title, author, update_callback):
        self.root = root
        self.title = title
        self.author = author
        self.update_callback = update_callback
        #setting title
        root.title("Edit")
        #setting window size
        width=736
        height=310
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.root.configure(bg='#E9EDC9')

        '''Title Label'''
        title_label=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        title_label["font"] = ft
        title_label["fg"] = "#333333"
        title_label["bg"] = "#E9EDC9"
        title_label["justify"] = "center"
        title_label["text"] = "Title"
        title_label.place(x=320,y=30,width=30,height=30)

        '''Edit Title'''
        self.edit_title=tk.Entry(self.root)
        self.edit_title["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=10)
        self.edit_title["font"] = ft
        self.edit_title["fg"] = "#333333"
        self.edit_title["justify"] = "left"
        self.edit_title.place(x=360,y=30,width=337,height=39)

        '''Author Label'''
        author_label=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        author_label["font"] = ft
        author_label["fg"] = "#333333"
        author_label["bg"] = "#E9EDC9"
        author_label["justify"] = "center"
        author_label["text"] = "Author"
        author_label.place(x=310,y=100,width=45,height=30)

        '''Edit Author'''
        self.edit_author=tk.Entry(self.root)
        self.edit_author["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=10)
        self.edit_author["font"] = ft
        self.edit_author["fg"] = "#333333"
        self.edit_author["justify"] = "left"
        self.edit_author.place(x=360,y=100,width=337,height=39)

        '''Entry Label'''
        editon_label=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        editon_label["font"] = ft
        editon_label["fg"] = "#333333"
        editon_label["bg"] = "#E9EDC9"
        editon_label["justify"] = "center"
        editon_label["text"] = "Edition"
        editon_label.place(x=310,y=170,width=45,height=30)

        '''Edit Edition'''
        self.edit_edition=tk.Entry(self.root)
        self.edit_edition["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=10)
        self.edit_edition["font"] = ft
        self.edit_edition["fg"] = "#333333"
        self.edit_edition["justify"] = "left"
        self.edit_edition.place(x=360,y=170,width=337,height=39)

        '''OK Button'''
        ok_button=tk.Button(self.root)
        ok_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        ok_button["font"] = ft
        ok_button["fg"] = "#000000"
        ok_button["justify"] = "center"
        ok_button["text"] = "OK"
        ok_button.place(x=290,y=260,width=70,height=25)
        ok_button["command"] = self.ok_button_command

        '''Cancel Button'''
        cancel_button=tk.Button(self.root)
        cancel_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        cancel_button["font"] = ft
        cancel_button["fg"] = "#000000"
        cancel_button["justify"] = "center"
        cancel_button["text"] = "Cancel"
        cancel_button.place(x=390,y=260,width=70,height=25)
        cancel_button["command"] = self.cancel_button_command

        '''Raw Input'''
        raw_text = tk.Text(self.root)
        raw_text["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=10)
        raw_text["font"] = ft
        raw_text["fg"] = "#333333"
        raw_text["wrap"] = tk.WORD
        raw_text.place(x=60,y=30,width=217,height=181)
        raw_text.insert(tk.END, f"Title: {self.title}\nAuthor: {self.author}")


    def ok_button_command(self):
        edited_title = self.edit_title.get()
        edited_author = self.edit_author.get()
        edited_edition = self.edit_edition.get()

        self.update_callback(edited_title, edited_author, edited_edition)
        self.root.destroy()


    def cancel_button_command(self):
        self.root.destroy()

class NotificationApp:
    def __init__(self, root):
        self.root = root

        # Pass the update function as a callback to Database
        self.db = Database(None, None, None, self.update_message)

        #setting title
        root.title("Notification")
        #setting window size
        width=439
        height=149
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.message_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=8)
        self.message_label["font"] = ft
        self.message_label["fg"] = "#333333"
        self.message_label["justify"] = "center"
        self.message_label["text"] = self.update_message
        self.message_label.place(x=10,y=20,width=417,height=65)

        ok_button=tk.Button(root)
        ok_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        ok_button["font"] = ft
        ok_button["fg"] = "#000000"
        ok_button["justify"] = "center"
        ok_button["text"] = "OK"
        ok_button.place(x=180,y=100,width=70,height=25)
        ok_button["command"] = self.ok_button_command

    def update_message(self, message):
        self.message_label.config(text = message)

    def ok_button_command(self):
        self.root.destroy()



if __name__ == "__main__":
    root = tk.Toplevel()
    app = Scan_APP(root)
    root.mainloop()