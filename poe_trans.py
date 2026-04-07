import customtkinter as ctk
from tkinter import filedialog
import subprocess
import os
import json
import threading
import sys

# ==============================
# PoE Professional Palette
# ==============================
COLOR_BG = "#050505"
COLOR_GOLD = "#8C7853"
COLOR_TEXT_GOLD = "#D4C29D"
COLOR_BLOOD = "#5E0000"
COLOR_SUCCESS = "#1B3022"
COLOR_BORDER = "#2A2A2A"

CONFIG_FILE = "config.json"

class PoETranslatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Path of Exile - GGPK Translator Portal")
        
        # Fixed Window Size
        self.resizable(False, False)
        
        window_width = 650
        window_height = 550 # Adjusted height since there's no background
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.configure(fg_color=COLOR_BG)

        self.config_data = self.load_config()

        # ------------------------------
        # Title Section
        # ------------------------------
        self.title_label = ctk.CTkLabel(
            self, text="POE TRANSLATION TOOL", 
            font=ctk.CTkFont(family="Georgia", size=32, weight="bold"), 
            text_color=COLOR_GOLD
        )
        self.title_label.pack(pady=(60, 40))

        # ------------------------------
        # Main Input Container
        # ------------------------------
        self.container = ctk.CTkFrame(self, fg_color="#121212", border_width=2, border_color=COLOR_GOLD, corner_radius=0)
        self.container.pack(padx=60, pady=10, fill="x")

        self.tool_entry = self.add_input_group("Translator Tool (PoeChinese.exe)", self.config_data.get("tool_path", ""))
        self.ggpk_entry = self.add_input_group("Game Data File (Content.ggpk)", self.config_data.get("ggpk_path", ""))

        # Status Label
        self.status_label = ctk.CTkLabel(self.container, text=" ", font=("Georgia", 14), text_color=COLOR_TEXT_GOLD, height=20)
        self.status_label.pack(pady=(0, 10))

        # ------------------------------
        # Action Button
        # ------------------------------
        self.btn_run = ctk.CTkButton(
            self, text="TRANSLATE", 
            font=ctk.CTkFont(family="Georgia", size=22, weight="bold"),
            height=65, width=320, corner_radius=0, 
            fg_color=COLOR_BLOOD, hover_color="#7D0000",
            text_color=COLOR_GOLD, border_width=2, border_color=COLOR_GOLD, 
            command=self.run_process
        )
        self.btn_run.pack(pady=40)

    def add_input_group(self, title, initial_value):
        lbl = ctk.CTkLabel(self.container, text=title, font=("Georgia", 14), text_color=COLOR_TEXT_GOLD)
        lbl.pack(padx=20, pady=(15, 5), anchor="w")
        
        row_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        row_frame.pack(padx=20, pady=(0, 10), fill="x")
        
        entry = ctk.CTkEntry(
            row_frame, fg_color="#000000", border_color=COLOR_BORDER, 
            text_color=COLOR_TEXT_GOLD, height=35, corner_radius=0
        )
        entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        entry.insert(0, initial_value)
        
        btn = ctk.CTkButton(
            row_frame, text="Browse", width=80, 
            fg_color=COLOR_BORDER, hover_color="#333", 
            corner_radius=0, text_color=COLOR_GOLD, 
            command=lambda: self.browse(entry)
        )
        btn.pack(side="right")
        return entry

    def browse(self, entry):
        path = filedialog.askopenfilename()
        if path:
            entry.delete(0, 'end')
            entry.insert(0, path)
            self.save_config()

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save_config(self):
        data = {"tool_path": self.tool_entry.get(), "ggpk_path": self.ggpk_entry.get()}
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def run_process(self):
        tool = self.tool_entry.get()
        ggpk = self.ggpk_entry.get()

        if not tool or not ggpk:
            self.update_status("Error: Missing file paths", is_error=True)
            return

        self.save_config()
        self.btn_run.configure(text="Translating...", state="disabled", fg_color="#333333")
        self.status_label.configure(text="Executing, please wait...", text_color=COLOR_TEXT_GOLD)

        def translation_task():
            try:
                subprocess.run(
                    [tool, ggpk], input=b"\n", stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True 
                )
                self.after(0, lambda: self.update_status("Translation Successful!", is_error=False))
            except Exception as e:
                self.after(0, lambda: self.update_status("Execution Failed", is_error=True))

        threading.Thread(target=translation_task, daemon=True).start()

    def update_status(self, message, is_error=False):
        self.btn_run.configure(state="normal")
        if is_error:
            self.btn_run.configure(text="FAILED", fg_color="#450000")
            self.status_label.configure(text=message, text_color="#FF4444")
        else:
            self.btn_run.configure(text="COMPLETE", fg_color=COLOR_SUCCESS)
            self.status_label.configure(text=message, text_color="#44FF44")
        self.after(3000, self.reset_button)

    def reset_button(self):
        self.btn_run.configure(text="TRANSLATE", fg_color=COLOR_BLOOD)
        self.status_label.configure(text=" ")

if __name__ == "__main__":
    app = PoETranslatorApp()
    app.mainloop()