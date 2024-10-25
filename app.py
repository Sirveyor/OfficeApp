"""
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import tkinter as tk
from tkinter import ttk
import time_tracker as tt
import json

def load_layout_config(file_path):
    with open(file_path) as file:
        return json.load(file)

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Survey Office")
        self.geometry("800x600")

        self.menu_frame = ttk.Frame(self)
        self.menu_frame.pack(side="left", fill="y")

        self.content_frame = ttk.Frame(self)
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.create_menu()
        
        self.layouts =  load_layout_config('layouts.json')

    def create_menu(self):
        buttons = ["Time Tracking", "File Management", "Equipment Tracking", "Field Work Scheduling", "Field Crew Management"]
        for button in buttons:
            btn = ttk.Button(self.menu_frame, text=button, command=lambda b=button: self.show_tab(b))
            btn.pack(fill="x")
            
    def on_menu_button_ckick(self, layout_name):
        self.show_tab(layout_name)
        

    def show_tab(self, layout_name):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        layout = self.layouts.get(layout_name, [])
        for widget_config in layout:
            widget_type = widget_config.pop("type")
            widget_class = getattr(ttk, widget_type)
            widget = widget_class(self.content_frame, **widget_config)
            widget.grid(**{k: widget_config[k] for k in ["row", "column", "sticky", "padx", "pady"] if k in widget_config})
        

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
