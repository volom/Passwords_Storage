from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as mb
import tkinter.simpledialog
from db_repo.db_handle import *
from encryption.decryptor import decrypt_db
from encryption.encryptor import encrypt_db
# ask password
tk.Tk().withdraw()

if try_connect() != "connected":
    while True:
        password = tkinter.simpledialog.askstring("Password", "Enter password:", show='*')
        try:
            decrypt_db(password)
            all_passwords = get_all_passwords()
        except:
            pass
        if try_connect() == "connected":
            encrypt_db(password)
            break
        else:
            mb.showerror("Error!", "Wrong password!")
            print("Wrong password!")
            continue
else:
     all_passwords = get_all_passwords()
#
#print(password)
if all_passwords == []:
    all_passwords = ['1']
    
class App:
    def __init__(self, root):
        #setting title
        root.title("Password Storage")
        #setting window size
        width=root.winfo_screenwidth()
        height=root.winfo_screenheight()
        alignstr = '%dx%d' % (width, height)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_54=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_54["font"] = ft
        GLabel_54["fg"] = "#333333"
        GLabel_54["justify"] = "center"
        GLabel_54["text"] = "Get password"
        GLabel_54.place(x=0,y=30,width=598,height=30)

        options = tk.StringVar(root)
        options.trace_add('write', lambda *args: print(options.get()))
        def on_option_change(event):
            global GLabel_624
            GLabel_624=tk.Label(root)
            GLabel_624["text"] = [x[2] for x in all_passwords if x[0]==options.get()]
            GLabel_624.place(x=80,y=150,width=1000,height=30)

            global GLabel_908
            GLabel_908=tk.Label(root)
            GLabel_908["text"] = [x[1] for x in all_passwords if x[0]==options.get()]
            GLabel_908.place(x=80,y=110,width=1000,height=30)

        secs = [x[0] for x in all_passwords]
        GListBox_504=tk.OptionMenu(root, options, *secs, command=on_option_change)
        GListBox_504.grid(row=1, column=2)

        GListBox_504["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_504["font"] = ft
        GListBox_504["fg"] = "#333333"
        GListBox_504["justify"] = "center"
        GListBox_504.place(x=180,y=70,width=236,height=30)

        GLabel_936=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_936["font"] = ft
        GLabel_936["fg"] = "#333333"
        GLabel_936["justify"] = "left"
        GLabel_936["text"] = "login"
        GLabel_936.place(x=20,y=110,width=63,height=30)

        GLabel_602=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_602["font"] = ft
        GLabel_602["fg"] = "#333333"
        GLabel_602["justify"] = "left"
        GLabel_602["text"] = "password"
        GLabel_602.place(x=20,y=150,width=63,height=30)

        GLabel_418=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_418["font"] = ft
        GLabel_418["fg"] = "#333333"
        GLabel_418["justify"] = "center"
        GLabel_418["text"] = "Update database"
        GLabel_418.place(x=0,y=180,width=607,height=30)

        global entry1
        entry1 = tk.StringVar(root)
        global entry2
        entry2 = tk.StringVar(root)
        global entry3
        entry3 = tk.StringVar(root)

        GLineEdit_783=tk.Entry(root, textvariable=entry1)
        GLineEdit_783["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_783["font"] = ft
        GLineEdit_783["fg"] = "#333333"
        GLineEdit_783["justify"] = "center"
        GLineEdit_783.place(x=150,y=260,width=183,height=30)
        

        GLineEdit_499=tk.Entry(root, textvariable=entry2)
        GLineEdit_499["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_499["font"] = ft
        GLineEdit_499["fg"] = "#333333"
        GLineEdit_499["justify"] = "center"
        GLineEdit_499.place(x=150,y=300,width=182,height=30)

        GLineEdit_199=tk.Entry(root, textvariable=entry3)
        GLineEdit_199["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_199["font"] = ft
        GLineEdit_199["fg"] = "#333333"
        GLineEdit_199["justify"] = "center"
        GLineEdit_199.place(x=150,y=220,width=184,height=30)
        
        name = entry3.get()
        #print(GLineEdit_199.get())
        #print(name)

        GLabel_949=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_949["font"] = ft
        GLabel_949["fg"] = "#333333"
        GLabel_949["justify"] = "center"
        GLabel_949["text"] = "Enter profile"
        GLabel_949.place(x=20,y=220,width=75,height=30)

        GLabel_981=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_981["font"] = ft
        GLabel_981["fg"] = "#333333"
        GLabel_981["justify"] = "center"
        GLabel_981["text"] = "Enter login"
        GLabel_981.place(x=20,y=260,width=65,height=30)

        GLabel_630=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_630["font"] = ft
        GLabel_630["fg"] = "#333333"
        GLabel_630["justify"] = "center"
        GLabel_630["text"] = "Enter password"
        GLabel_630.place(x=20,y=300,width=92,height=30)

        GButton_955=tk.Button(root)
        GButton_955["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_955["font"] = ft
        GButton_955["fg"] = "#000000"
        GButton_955["justify"] = "center"
        GButton_955["text"] = "Update"
        GButton_955.place(x=490,y=250,width=93,height=36)
        GButton_955["command"] = self.GButton_955_command

    def GButton_955_command(self):
        if try_connect() != "connected":
            decrypt_db(password)
            add_password(entry3.get(), entry1.get(), entry2.get())
            globals()["all_passwords"] = get_all_passwords()
            mb.showinfo('message', f"Profile {entry3.get()} is updated with login - {entry1.get()} and password - {entry2.get()}")
            encrypt_db(password)
        else:
            add_password(entry3.get(), entry1.get(), entry2.get())
            globals()["all_passwords"] = get_all_passwords()
            mb.showinfo('message', f"Profile {entry3.get()} is updated with login - {entry1.get()} and password - {entry2.get()}")
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
