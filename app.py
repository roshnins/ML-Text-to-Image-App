import tkinter as tk
import customtkinter as ctk

from PIL import ImageTk
#from authtoken import auth_token

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

# Create the application
app = tk.Tk()

# Set the sixe of the app
app.geometry("532x622")
app.title("Stable app")
ctk.set_appearance_mode("dark")

# Add in the entry field
prompt = ctk.CTkEntry(height=40, width=512, text_font=(
    "Arial", 20), text_color="black", fg_color="white")
# Position of the entry prompt
prompt.place(x=10, y=10)


# Run the app
app.mainloop()
