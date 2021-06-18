import os
import tkinter as tk
from tkinter import messagebox


class ResetPassword(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.iconbitmap('images/icon.ico')
        self.master.title("PassLock")
        self.master.geometry("500x500")
        self.master.resizable(0, 0)
        # ---------------------------StringVar
        self.username = tk.StringVar()
        self.key = tk.StringVar()
        self.new_password = tk.StringVar()
        self.confirm = tk.StringVar()
        # ---------------------------frame1
        self.frame1 = tk.Frame(self.master, bg="pale turquoise", relief="ridge")
        self.frame1.pack(side="top", expand='true', fill='both', anchor='c')
        # ---------------------------title label
        self.title_label = tk.Label(self.frame1, text="Recovery", font="Arial 20 bold", bg="pale turquoise")
        self.title_label.grid(row=1, column=0, columnspan=2, sticky='n', pady=40)
        # ---------------------------image
        # Add image file
        self.img = tk.PhotoImage(file="images/logo.png")
        # ---------------------------canvas
        self.canvas = tk.Canvas(self.frame1, height=110, bg="white", width=500)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.canvas.create_image(250, 60, image=self.img)
        # ---------------------------Program UI
        self.username_label = tk.Label(self.frame1, text="                                    Username:",
                                           font="Arial 10 bold", bg="pale turquoise")
        self.username_entry = tk.Entry(self.frame1, width=25, textvariable=self.username)
        self.key_label = tk.Label(self.frame1, text="                                              Key:",
                                  font="Arial 10 bold", bg="pale turquoise")
        self.key_entry = tk.Entry(self.frame1, width=25, textvariable=self.key)

        self.new_password_label = tk.Label(self.frame1, text="                             New password:",
                                           font="Arial 10 bold", bg="pale turquoise")
        self.new_password_entry = tk.Entry(self.frame1, width=25, show="*", textvariable=self.new_password)

        self.confirm_label = tk.Label(self.frame1, text="                        Confirm password:",
                                      font="Arial 10 bold", bg="pale turquoise")
        self.confirm_entry = tk.Entry(self.frame1, width=25, show="*", textvariable=self.confirm)

        # n, e, s, w, ne, se, sw, 
        # Grid on the screen
        self.username_label.grid(row=2, column=0, columnspan=2, sticky='w', pady=10)
        self.username_entry.grid(row=2, column=1, columnspan=2, sticky='e', pady=10, padx=130)

        self.key_label.grid(row=3, column=0, columnspan=2, sticky='w', pady=10)
        self.key_entry.grid(row=3, column=1, columnspan=2, sticky='e', pady=10, padx=130)

        self.new_password_label.grid(row=4, column=0, columnspan=2, sticky='w', pady=10)
        self.new_password_entry.grid(row=4, column=1, columnspan=2, sticky='e', pady=10, padx=130)

        self.confirm_label.grid(row=5, column=0, columnspan=2, sticky='w', pady=10)
        self.confirm_entry.grid(row=5, column=1, columnspan=2, sticky='e', pady=10, padx=130)
        
        # Enter btn
        btn_enter = tk.Button(self.frame1, text="Enter", font="Arial 10 bold", width=7,
                              bg="#0001a7", fg='white', command=self.change,
                              activeforeground='white', activebackground='#00dee1')
        btn_enter.grid(row=6, column=0, columnspan=2, pady=20)
        # -------------------------------Events
        self.master.bind('<Return>', self.change)

    def change(self, *_):
        new_password = self.new_password.get()
        confirm = self.confirm.get()
        print(new_password, confirm)
        if len(new_password) == 0:
            messagebox.showerror("PassLock", "Enter your password")
        elif new_password == confirm and len(new_password) >= 8:
            # store the new password in Database
            file = open('password.txt', 'w')
            file.seek(0, 0)
            file.write(self.username.get() + '\n')
            file.write(new_password)
            self.master.destroy()
            os.system('python login.py')
            # bgLabel.destroy()
            # return Login(self)
        elif new_password == confirm and len(new_password) < 8:
            messagebox.showerror("PassLock Error", "Your password is less than 8 characters")
        else:
            messagebox.showerror("PassLock Error", "Your password and confirmation password do not match")


if __name__ == "__main__":
    form = tk.Tk()
    app = ResetPassword(form)
    # Adjust size
    form.mainloop()
