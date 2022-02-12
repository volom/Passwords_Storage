import tkinter as tk
import tkinter.font as tkFont
import tkinter.simpledialog
import tkinter.messagebox as mb
from db_repo.db_handle import *
from encryption.encryptor import encrypt_db
from encryption.decryptor import decrypt_db
class App:
    def __init__(self, root):
        #setting title
        root.title("SET/CHANGE PASSWORD")
        #setting window size
        width=410
        height=135
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_321=tk.Button(root)
        GButton_321["bg"] = "#00ced1"
        ft = tkFont.Font(family='Times',size=10)
        GButton_321["font"] = ft
        GButton_321["fg"] = "#000000"
        GButton_321["justify"] = "center"
        GButton_321["text"] = "SET PASSWORD"
        GButton_321.place(x=10,y=30,width=172,height=62)
        GButton_321["command"] = self.GButton_321_command

        GButton_172=tk.Button(root)
        GButton_172["bg"] = "#00ced1"
        ft = tkFont.Font(family='Times',size=10)
        GButton_172["font"] = ft
        GButton_172["fg"] = "#000000"
        GButton_172["justify"] = "center"
        GButton_172["text"] = "CHANGE PASSWORD"
        GButton_172.place(x=210,y=30,width=172,height=62)
        GButton_172["command"] = self.GButton_172_command

    def GButton_321_command(self):
        if try_connect() == "connected":
            while True:
                while True:   
                    password0 = tkinter.simpledialog.askstring("Password", "Enter password:", show='*')
                    if len(set(list(map(str, password0))))==1:
                        mb.showerror("PASSWORD IS SET!", """The password must not contain the same elements""")
                        continue
                    else:
                        break
                check_password0 = tkinter.simpledialog.askstring("Password", "Enter password again", show='*')
                
                    
                if password0 == check_password0:
                    break
                else:
                    mb.showerror("PASSWORD IS SET!", """Wrong password. Try again!""")
                    continue
            encrypt_db(password0)
            mb.showerror("PASSWORD IS SET!", """Password is set""")
            return 0
        else:
            mb.showerror("PASSWORD IS SET!", """The password is already set. Press "CHANGE PASSWORD" """)
            print("""The password is already set. Press "CHANGE PASSWORD" """)
            return 0


    def GButton_172_command(self):
        if try_connect() == "file is not a database":
            old_password = tkinter.simpledialog.askstring("Password", "Enter old password", show='*')
            
            while True:
                while True:
                    while True:   
                        password1 = tkinter.simpledialog.askstring("Password", "Enter password:", show='*')
                        if len(set(list(map(str, password1))))==1:
                            mb.showerror("PASSWORD IS SET!", """The password must not contain the same elements""")
                            continue
                        else:
                            break
                    if old_password != password1:
                        break
                    else:
                        mb.showerror("Wrong password!", "The new password must not be the same as the old one!")
                        continue

                check_password1 = tkinter.simpledialog.askstring("Password", "Enter new password again", show='*')
                if password1 == check_password1:
                    try:
                        decrypt_db(old_password)
                        encrypt_db(password1)
                        mb.showerror("New password set!", "New password set!")
                        return 0
                    except:
                        mb.showerror("Wrong password!", "Wrong old password! Try again...")
                    break
                else:
                    mb.showerror("Wrong password!", "Wrong password! Try again...")
                    continue
            
        else:
            mb.showerror("Db has no password!", """Database has not password yet. Press "SET PASSWORD" """)
            return 0

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


