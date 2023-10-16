from tkinter import filedialog
import customtkinter
import random
import string
import tkinter as tk

class Window:

    def __init__(self):
        self.window = None
        self.version = "1.0"
        self.frame1 = None
        self.frame = None
        self.password= None
        self.icon_path = "Images/Password Generator logo.ico"
        self.createWindow()

    def createWindow(self):
        self.window = customtkinter.CTk()
        self.window.title(f"Password generator {self.version}")
        self.window.geometry("1120x700")
        self.window.wm_resizable(False, False)
        self.window.iconbitmap(default=self.icon_path)
#       -------------------------
        self.createOptionsFrame()
        self.createFrame()
        self.createSlider()
        self.createCheckbox()
        self.createTextBox()
        self.createTitle()
        self.createButtons()
        self.createModeMenu()
        self.window.mainloop()
#       -------------------------
        customtkinter.set_default_color_theme('themes/dark-blue.json')

    def createFrame(self):
        self.frame = customtkinter.CTkFrame(master=self.window, width=240, height=1920)
        self.frame.place(rely=0, relx=0)

    def slider_event(self, value):
        self.text.configure(text=f"Password length: {value}")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def createSlider(self):
        self.slider = customtkinter.CTkSlider(master=self.frame1, from_=1, to=51, command=self.slider_event,
                                              number_of_steps=50, width=520, height=20, border_width=5)
        self.slider.place(rely=0.10, relx=0.048)

        self.variable = self.slider.get()

        self.text = customtkinter.CTkLabel(master=self.frame1, text=f"Password length: {self.variable}",
                                           font=("Segoe UI Variable Small Semibol", 21))
        self.text.place(rely=0.09, relx=0.715)

    def createModeMenu(self):
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(master=self.frame, values=["System", "Dark", "Light"],
                                                                       command=self.change_appearance_mode_event,
                                                                       width=185, height=34, font=("Arial", 14))
        self.appearance_mode_optionemenu.place(rely=0.33, relx=0.12)

    def createButtons(self):
        self.button = customtkinter.CTkButton(master=self.frame1, text="Generate password", width=240, height=40,
                                              font=("Segoe UI Variable Small Semibol", 16), command=self.generate_password)
        self.button.place(rely=0.78, relx=0.05)

        self.button1 = customtkinter.CTkButton(master=self.frame1, text="Save my password", width=240, height=40,
                                              font=("Segoe UI Variable Small Semibol", 16), command=self.clearLogs, state="disabled")
        self.button1.place(rely=0.78, relx=0.38)

    def createCheckbox(self):
            self.check_var = customtkinter.StringVar(value="on")
            self.checkbox = customtkinter.CTkCheckBox(master=self.frame1, text=" Special characters -", variable=self.check_var,
                                                    onvalue="on", offvalue="off", checkbox_width=30, checkbox_height=30,
                                                    font=("Arial", 18), border_width=3, corner_radius=7)
            self.checkbox.place(rely=0.25, relx=0.05)

            self.check_var1 = customtkinter.StringVar(value="on")
            self.checkbox1 = customtkinter.CTkCheckBox(master=self.frame1, text=" Numbers -", variable=self.check_var1,
                                                    onvalue="on", offvalue="off", checkbox_width=30, checkbox_height=30,
                                                    font=("Arial", 18), border_width=3, corner_radius=7)
            self.checkbox1.place(rely=0.4, relx=0.05)

            self.check_var2 = customtkinter.StringVar(value="on")
            self.checkbox2 = customtkinter.CTkCheckBox(master=self.frame1, text=" Letters -", variable=self.check_var2,
                                                    onvalue="on", offvalue="off", checkbox_width=30, checkbox_height=30,
                                                    font=("Arial", 18), border_width=3, corner_radius=7)
            self.checkbox2.place(rely=0.55, relx=0.05)

    def createTitle(self):
        self.title = customtkinter.CTkLabel(master=self.frame, text=" Password\n_Generator_",
                                           font=("revamped", 23))
        self.title.place(rely=0.015, relx=0.08)

    def clearLogs(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile="My password", filetypes=[("Text Files", "*.txt")])

        if file_path:
            with open(file_path, 'w') as file:
                file.write(f'{self.password}')

            self.textbox.configure(state="normal")
            self.textbox.insert("0.0", " • Your password is saved!\n")
            self.textbox.configure(state="disabled")

    def createOptionsFrame(self):
        self.frame1 = customtkinter.CTkFrame(master=self.window, width=800, height=350)
        self.frame1.place(rely=0.04, relx=0.251)

    def createTextBox(self):
        self.textbox = customtkinter.CTkTextbox(master=self.window, height=270, width=800, corner_radius=10,
                                                font=("Cascadia Mono SemiBold", 18), state="normal")
        self.textbox.place(rely=0.574, relx=0.251)
        self.textbox.configure(state="disabled")

    def generate_password(self):
        length = int(self.slider.get())

        if self.check_var.get() == "on":
            special_characters = "!@#$%^&*()_+[]{}|;':,.<>?~"
        else:
            special_characters = ""

        if self.check_var1.get() == "on":
            numbers = "0123456789"
        else:
            numbers = ""

        if self.check_var2.get() == "on":
            letters = string.ascii_letters
        else:
            letters = ""

        use_chars = special_characters + numbers + letters

        if not use_chars:
            self.textbox.configure(state="normal")
            self.textbox.insert("0.0", " • OPTION ERROR: You have not chosen an option! You must choose one.\n")
            self.textbox.configure(state="disabled")
            return

        self.password = ''.join(random.choice(use_chars) for _ in range(length))
        self.textbox.configure(state="normal")
        self.textbox.insert("0.4", f" • Generated password: {self.password}\n")
        self.textbox.configure(state="disabled")
        self.button1.configure(state="normal")

app = Window()
