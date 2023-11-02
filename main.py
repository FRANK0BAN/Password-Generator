from tkinter import filedialog
import customtkinter
import random
import string
import ctypes as ct

def change_appearance_mode(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)

class Window:

    def __init__(self):
        self.window = None
        self.general_frame = None
        self.side_frame = None
        self.password= None
        self.button = None
        self.button1 = None
        self.text = None
        self.check_var = None
        self.check_var1 = None
        self.check_var2 = None
        self.checkbox = None
        self.checkbox1 = None
        self.checkbox2 = None
        self.slider = None
        self.variable = None
        self.appearance_mode_option_menu = None
        self.title = None
        self.textbox = None
        self.custom_font = None
#       -------------------------
        self.icon_path = "Images/Password Generator logo.ico"
        self.version = "1.0"
        self.create_window()

    def create_window(self):
        self.window = customtkinter.CTk()
        self.window.title(f"Password generator {self.version}")
        self.window.geometry("1120x700")
        self.window.wm_resizable(False, False)
        self.window.winfo_toplevel()
        self.window.iconbitmap(default=self.icon_path)
#       -------------------------
        try:
            customtkinter.set_default_color_theme('themes/dark-blue.json')
        except Exception as error_type:
            self.check_error(error_type)
#       -------------------------
        self.create_general_frame()
        self.create_side_frame()
        self.create_slider()
        self.create_checkbox()
        self.create_text_box()
        self.create_title()
        self.create_buttons()
        self.create_mode_menu()
        self.dark_title_bar()
        self.window.mainloop()
#       -------------------------

    def check_error(self, error_type):
        self.textbox.configure(state="normal")
        self.textbox.insert("0.0", f" • ERROR: {error_type}\n")
        self.textbox.configure(state="disabled")

    def dark_title_bar(self):
        try:
            # Using ctypes library
            self.window.update()
            DWMWA_USE_IMMERSIVE_DARK_MODE = 20
            set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
            get_parent = ct.windll.user32.GetParent
            hwnd = get_parent(self.window.winfo_id())
            rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
            value = 2
            value = ct.c_int(value)
            set_window_attribute(hwnd, rendering_policy, ct.byref(value),
                                ct.sizeof(value))
        except Exception as error_type:
            self.check_error(error_type)

    def create_side_frame(self):
        self.side_frame = customtkinter.CTkFrame(master=self.window, width=240, height=700)
        self.side_frame.place(rely=0, relx=0)

    def slider_event(self, value):
        value = int(value)
        self.text.configure(text=f"Password length: {value}")

    def create_slider(self):
        try:
            self.slider = customtkinter.CTkSlider(master=self.general_frame, from_=1, to=50, command=self.slider_event,
                                                    number_of_steps=50, width=520, height=20, border_width=5)
            self.slider.place(rely=0.10, relx=0.048)

            self.variable = int(self.slider.get())

            self.text = customtkinter.CTkLabel(master=self.general_frame, text=f"Password length: {self.variable}",
                                            font=("Segoe UI Variable Small Semibol", 21))
            self.text.place(rely=0.09, relx=0.715)
        except Exception as error_type:
            self.check_error(error_type)

    def create_mode_menu(self):
        try:
            self.appearance_mode_option_menu = customtkinter.CTkOptionMenu(master=self.side_frame, values=["System", "Dark", "Light"],
                                                                           command=change_appearance_mode,
                                                                           width=185, height=34, font=("Arial", 14))
            self.appearance_mode_option_menu.place(rely=0.9, relx=0.12)
        except Exception as error_type:
            self.check_error(error_type)

    def create_buttons(self):
        try:
            self.button = customtkinter.CTkButton(master=self.general_frame, text="Generate password", width=240, height=40,
                                                font=("Segoe UI Variable Small Semibol", 16), command=self.generate_password)
            self.button.place(rely=0.78, relx=0.05)

            self.button1 = customtkinter.CTkButton(master=self.general_frame, text="Save my password", width=240, height=40,
                                                font=("Segoe UI Variable Small Semibol", 16), command=self.password_saver, state="disabled")
            self.button1.place(rely=0.78, relx=0.38)
        except Exception as error_type:
            self.check_error(error_type)

    def create_checkbox(self):
        try:
            self.check_var = customtkinter.StringVar(value="on")
            self.checkbox = customtkinter.CTkCheckBox(master=self.general_frame, text=" Special characters ", variable=self.check_var,
                                                    onvalue="on", offvalue="off", checkbox_width=30, checkbox_height=30,
                                                    font=("Arial", 18), border_width=3, corner_radius=7)
            self.checkbox.place(rely=0.25, relx=0.05)

            self.check_var1 = customtkinter.StringVar(value="on")
            self.checkbox1 = customtkinter.CTkCheckBox(master=self.general_frame, text=" Numbers ", variable=self.check_var1,
                                                    onvalue="on", offvalue="off", checkbox_width=30, checkbox_height=30,
                                                    font=("Arial", 18), border_width=3, corner_radius=7)
            self.checkbox1.place(rely=0.4, relx=0.05)

            self.check_var2 = customtkinter.StringVar(value="on")
            self.checkbox2 = customtkinter.CTkCheckBox(master=self.general_frame, text=" Letters ", variable=self.check_var2,
                                                    onvalue="on", offvalue="off", checkbox_width=30, checkbox_height=30,
                                                    font=("Arial", 18), border_width=3, corner_radius=7)
            self.checkbox2.place(rely=0.55, relx=0.05)
        except Exception as error_type:
            self.check_error(error_type)


    def create_title(self):
        self.custom_font = customtkinter.CTkFont(family="Revamped", size=23)

        self.title = customtkinter.CTkLabel(master=self.side_frame, text=" Password\n_Generator_", font=self.custom_font)
        self.title.place(rely=0.043, relx=0.08)

    def password_saver(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile="My password", filetypes=[("Text Files", "*.txt")])

            if file_path:
                with open(file_path, 'w') as file:
                    file.write(f'{self.password}')

                self.textbox.configure(state="normal")
                self.textbox.insert("0.0", " • Your password is saved!\n")
                self.textbox.configure(state="disabled")
        except Exception as error_type:
            self.check_error(error_type)

    def create_general_frame(self):
        self.general_frame = customtkinter.CTkFrame(master=self.window, width=800, height=350)
        self.general_frame.place(rely=0.04, relx=0.251)

    def create_text_box(self):
        self.textbox = customtkinter.CTkTextbox(master=self.window, height=270, width=800, corner_radius=10,
                                                font=("Cascadia Mono SemiBold", 18), state="normal")
        self.textbox.place(rely=0.574, relx=0.251)
        self.textbox.configure(state="disabled")

    def generate_password(self):
        try:
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
        except Exception as error_type:
            self.check_error(error_type)

app = Window()
