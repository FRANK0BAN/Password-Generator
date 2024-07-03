from tkinter import filedialog
from PIL import Image, ImageTk
import customtkinter
import random
import string
import pyperclip
import ctypes as ct
import requests
import hashlib


def change_appearance_mode(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)


class Window:

    def __init__(self):
        # ------------------------------ Initializing UI:
        self.window = customtkinter.CTk()
        self.general_frame = None
        self.side_frame = None
        self.button_generate = None
        self.button_copy = None
        self.button_saver = None
        self.button_clear = None
        self.button_password_check = None
        self.checkbox_special_characters = None
        self.checkbox_numbers = None
        self.checkbox_letters = None
        self.checkbox_show_password = None
        self.slider = None
        self.text = None
        self.title = None
        self.textbox = None
        # ------------------------------ Initializing Variables:
        self.check_show_password = None
        self.check_special_characters = None
        self.check_letters = None
        self.check_numbers = None
        self.slider_value = None
        self.massage = None
        self.appearance_mode_option_menu = None
        self.custom_font = None
        self.font_name = None
        self.size_subtract_button = None
        self.size_add_button = None
        self.visibility_option_button = None
        self.font_size = None
        self.password = None
        self.password_visibility = True
        self.current_font = None
        self.hashes = None
        self.web_url = None
        self.hashed_password = None
        self.first_5_chars = None
        self.response = None
        self.variable = 0
        # ------------------------------ Images Opening:
        self.trash_image_path = Image.open("Images/trash.png")
        self.no_copy_image_path = Image.open("Images/NoCopy.png")
        self.copy_image_path = Image.open("Images/copy.png")
        self.visibility_image_path = Image.open("Images/Visibility.png")
        self.no_visibility_image_path = Image.open("Images/NoVisibility.png")
        self.plus_image_path = Image.open("Images/plus.png")
        self.minus_image_path = Image.open("Images/minus.png")
        # ------------------------------ Assignment to variable:
        self.trash_image = customtkinter.CTkImage(self.trash_image_path)
        self.copy_image = customtkinter.CTkImage(self.copy_image_path)
        self.visibility_image = customtkinter.CTkImage(self.visibility_image_path)
        self.no_visibility_image = customtkinter.CTkImage(self.no_visibility_image_path)
        self.plus_image = customtkinter.CTkImage(self.plus_image_path)
        self.minus_image = customtkinter.CTkImage(self.minus_image_path)
        self.no_copy_image = customtkinter.CTkImage(self.no_copy_image_path)
        # ------------------------------ General settings:
        self.current_console_font = ("Cascadia Mono SemiBold", 18)
        self.icon_path = "Images/Password Generator logo.ico"
        self._version_ = "1.2"
        self.create_window()

    def create_window(self):
        self.window.title(f"Password generator {self._version_}")
        self.window.geometry("1140x700")
        self.window.wm_resizable(False, False)
        self.window.winfo_toplevel()
        self.window.iconbitmap(default=self.icon_path)
        # ------------------------------
        try:
            customtkinter.set_default_color_theme('themes/dark-blue.json')
        except Exception as error_type:
            self.console_massage(f"{error_type}\n")
        # ------------------------------
        self.dark_title_bar()
        self.create_general_frame()
        self.create_side_frame()
        self.create_slider()
        self.create_checkbox()
        self.create_text_box()
        self.create_console_options()
        self.create_title()
        self.create_buttons()
        self.create_mode_menu()
        self.window.mainloop()
        # ------------------------------

    def console_massage(self, massage):
        self.textbox.configure(state="normal")
        self.textbox.insert("0.4", f"{massage}")
        self.textbox.configure(state="disabled")

    def dark_title_bar(self):
        try:
            self.window.update()
            ct.windll.dwmapi.DwmSetWindowAttribute(ct.windll.user32.GetParent(self.window.winfo_id()), 20,
                                                   ct.byref(ct.c_int(2)), ct.sizeof(ct.c_int(2)))
        except Exception as error_type:
            self.console_massage(f"{error_type}\n")

    def slider_event(self, value):
        value = int(value)
        self.text.configure(text=f"Password length: {value}")

    def password_saver(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile="My password",
                                                     filetypes=[("Text Files", "*.txt")])
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(f'{self.password}')

                self.textbox.configure(state="normal")
                self.textbox.insert("0.0", " • Your password is saved!\n")
                self.textbox.configure(state="disabled")
        except Exception as error_type:
            self.console_massage(f"{error_type}\n")

    def password_copy(self):
        try:
            pyperclip.copy(f'{self.password}')
            self.textbox.configure(state="normal")
            self.textbox.insert("0.0", " • The password has been copied\n")
            self.textbox.configure(state="disabled")
        except Exception as error_type:
            self.console_massage(f"{error_type}\n")

    def increase_font_size(self):
        try:
            self.font_name, self.font_size = self.current_console_font
            self.font_size = int(self.font_size) + 2
            if self.font_size > 26:
                self.font_size = 26
            self.current_console_font = (self.font_name, self.font_size)
            self.textbox.configure(font=(self.font_name, self.font_size))
        except Exception as error_type:
            self.console_massage(f"{error_type}\n")

    def decrease_font_size(self):
        try:
            self.font_name, self.font_size = self.current_console_font
            self.font_size = int(self.font_size) - 2
            if self.font_size < 8:
                self.font_size = 8
            self.current_console_font = (self.font_name, self.font_size)
            self.textbox.configure(font=(self.font_name, self.font_size))
        except Exception as error_type:
            self.console_massage(f"{error_type}\n")

    def visibility_option(self):
        if self.variable == 0:
            self.password_visibility = False
            self.visibility_option_button.configure(image=self.no_visibility_image)
            self.variable += 1
        else:
            self.password_visibility = True
            self.visibility_option_button.configure(image=self.visibility_image)
            self.variable -= 1

    def clear_textbox(self):
        self.textbox.configure(state="normal")
        self.textbox.delete('1.0', 'end')
        self.textbox.insert("0.0", " • The console has been cleaned\n")
        self.textbox.configure(state="disabled")

    def password_stats_checker(self):
        self.hashed_password = hashlib.sha1(self.password.encode()).hexdigest().upper()
        self.first_5_chars = self.hashed_password[:5]

        self.web_url = f"https://api.pwnedpasswords.com/range/{self.first_5_chars}"
        self.response = requests.get(self.web_url)
        if self.response.status_code == 200:
            self.hashes = dict(line.split(':') for line in self.response.text.splitlines())
            count = self.hashes.get(self.hashed_password[5:])
            if count:
                self.console_massage(f" • WARNING: Generated password has been revealed {count} times! \n "
                                     f"- We recommend not using this password.\n\n")
            else:
                self.console_massage(f" • NOTICE: Your password has not been revealed anywhere! \n "
                                     f"- You can use it safely.\n\n")
        else:
            self.console_massage(" • CONNECTION ERROR: Cannot connect to api.pwnedpasswords.com\n")

    def create_side_frame(self):
        self.side_frame = customtkinter.CTkFrame(master=self.window, width=240, height=640)
        self.side_frame.place(rely=0.038, relx=0.024)

    def create_slider(self):
        try:
            self.slider = customtkinter.CTkSlider(master=self.general_frame, from_=1, to=50, command=self.slider_event,
                                                  number_of_steps=50, width=520, height=20, border_width=5)
            self.slider.place(rely=0.10, relx=0.048)

            self.slider_value = int(self.slider.get())

            self.text = customtkinter.CTkLabel(master=self.general_frame, text=f"Password length: {self.slider_value}",
                                               font=("Segoe UI Variable Small Semibol", 21))
            self.text.place(rely=0.09, relx=0.715)
        except Exception as error_type:
            self.console_massage(f"{error_type}\n")

    def create_mode_menu(self):
        try:
            self.appearance_mode_option_menu = customtkinter.CTkOptionMenu(master=self.side_frame,
                                                                           values=["System", "Dark", "Light"],
                                                                           command=change_appearance_mode,
                                                                           width=185, height=34, font=("Arial", 14))
            self.appearance_mode_option_menu.place(rely=0.9, relx=0.12)
        except Exception as error_type:
            self.console_massage(f"{error_type}\n")

    def create_buttons(self):
        try:
            self.button_generate = customtkinter.CTkButton(master=self.general_frame, text="Generate password",
                                                           width=225,
                                                           height=40,
                                                           font=("Segoe UI Variable Small Semibol", 16),
                                                           command=self.generate_password)
            self.button_generate.place(rely=0.78, relx=0.05)

            self.button_saver = customtkinter.CTkButton(master=self.general_frame, text="Save my password", width=225,
                                                        height=40,
                                                        font=("Segoe UI Variable Small Semibol", 16),
                                                        command=self.password_saver, state="disabled")
            self.button_saver.place(rely=0.78, relx=0.36)

            self.button_password_check = customtkinter.CTkButton(master=self.general_frame, text="Check my password",
                                                                 width=225,
                                                                 height=40,
                                                                 font=("Segoe UI Variable Small Semibol", 16),
                                                                 command=self.password_stats_checker, state="disabled")
            self.button_password_check.place(rely=0.78, relx=0.67)
        except Exception as error_type:
            self.console_massage(f"{error_type}\n")

    def create_checkbox(self):
        try:
            self.check_special_characters = customtkinter.StringVar(value="on")
            self.checkbox_special_characters = customtkinter.CTkCheckBox(master=self.general_frame,
                                                                         text=" Special characters ",
                                                                         variable=self.check_special_characters,
                                                                         onvalue="on", offvalue="off",
                                                                         checkbox_width=30,
                                                                         checkbox_height=30,
                                                                         font=("Arial", 18), border_width=3,
                                                                         corner_radius=7)
            self.checkbox_special_characters.place(rely=0.25, relx=0.05)

            self.check_numbers = customtkinter.StringVar(value="on")
            self.checkbox_numbers = customtkinter.CTkCheckBox(master=self.general_frame, text=" Numbers ",
                                                              variable=self.check_numbers,
                                                              onvalue="on", offvalue="off", checkbox_width=30,
                                                              checkbox_height=30,
                                                              font=("Arial", 18), border_width=3, corner_radius=7)
            self.checkbox_numbers.place(rely=0.4, relx=0.05)

            self.check_letters = customtkinter.StringVar(value="on")
            self.checkbox_letters = customtkinter.CTkCheckBox(master=self.general_frame, text=" Letters ",
                                                              variable=self.check_letters,
                                                              onvalue="on", offvalue="off", checkbox_width=30,
                                                              checkbox_height=30,
                                                              font=("Arial", 18), border_width=3, corner_radius=7)
            self.checkbox_letters.place(rely=0.55, relx=0.05)
        except Exception as error_type:
            self.console_massage(f"{error_type}\n")

    def create_title(self):
        try:
            self.custom_font = customtkinter.CTkFont(family="Revamped", size=23)

            self.title = customtkinter.CTkLabel(master=self.side_frame, text=" Password\n_Generator_",
                                                font=self.custom_font)
            self.title.place(rely=0.043, relx=0.08)
        except Exception as error_type:
            self.console_massage(f"{error_type}\n")

    def create_general_frame(self):
        self.general_frame = customtkinter.CTkFrame(master=self.window, width=800, height=350)
        self.general_frame.place(rely=0.04, relx=0.263)

    def create_text_box(self):
        self.textbox = customtkinter.CTkTextbox(master=self.window, height=270, width=760, corner_radius=10,
                                                font=("Cascadia Mono SemiBold", 18), state="normal")
        self.textbox.place(rely=0.573, relx=0.264)
        self.textbox.configure(state="disabled")

    def create_console_options(self):
        self.button_clear = customtkinter.CTkButton(master=self.window, image=self.trash_image, border_width=0,
                                                    border_color=None, text="", fg_color="transparent", width=32,
                                                    height=32, command=self.clear_textbox)
        self.button_clear.place(rely=0.573, relx=0.935)

        self.button_copy = customtkinter.CTkButton(master=self.window, image=self.no_copy_image, border_width=0,
                                                   border_color=None, text="", fg_color="transparent", width=32,
                                                   height=32, command=self.password_copy, state='disabled')
        self.button_copy.place(rely=0.633, relx=0.935)

        self.visibility_option_button = customtkinter.CTkButton(master=self.window, image=self.visibility_image,
                                                                border_width=0,
                                                                border_color=None, text="", fg_color="transparent",
                                                                width=32,
                                                                height=32, command=self.visibility_option)
        self.visibility_option_button.place(rely=0.693, relx=0.935)

        self.size_add_button = customtkinter.CTkButton(master=self.window, image=self.plus_image, border_width=0,
                                                       border_color=None, text="", fg_color="transparent", width=32,
                                                       height=32, command=self.increase_font_size)
        self.size_add_button.place(rely=0.873, relx=0.935)

        self.size_subtract_button = customtkinter.CTkButton(master=self.window, image=self.minus_image, border_width=0,
                                                            border_color=None, text="", fg_color="transparent",
                                                            width=32,
                                                            height=32, command=self.decrease_font_size)
        self.size_subtract_button.place(rely=0.92, relx=0.935)

    def generate_password(self):
        try:
            length = int(self.slider.get())

            if self.check_special_characters.get() == "on":
                special_characters = "!@#$%^&*()_+[]{}|;':,.<>?~"
            else:
                special_characters = ""

            if self.check_numbers.get() == "on":
                numbers = "0123456789"
            else:
                numbers = ""

            if self.check_letters.get() == "on":
                letters = string.ascii_letters
            else:
                letters = ""

            use_chars = special_characters + numbers + letters

            if not use_chars:
                return self.console_massage(" • OPTION ERROR: You have not chosen an option!\n"
                                            " - You must choose one.\n")

            self.password = ''.join(random.choice(use_chars) for _ in range(length))
            if self.password_visibility:
                self.massage = f' • Generated password: {self.password}\n'
            else:
                self.massage = f' • Password was successfully generated\n'
            self.console_massage(f"{self.massage}")
            self.button_saver.configure(state="normal")
            self.button_password_check.configure(state="normal")
            self.button_copy.configure(state="normal", image=self.copy_image)
        except Exception as error_type:
            self.console_massage(f"{error_type}\n")


app = Window()
