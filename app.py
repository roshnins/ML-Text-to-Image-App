import tkinter as tk
import customtkinter as ctk

from PIL import ImageTk
from authtoken import auth_token

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

# Placeholder to contain images
lmain = ctk.CTkLabel(height=512, width=512)
lmain.place(x=10, y=110)

# Specify the model
modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
# Set the pipeline
pipe = StableDiffusionPipeline.from_pretrained(
    modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token=auth_token)
pipe.to(device)


def generate():
    pass


# Create a button
trigger = ctk.CTkButton(height=40, width=120, text_font=(
    "Arial", 20), text_color="white", fg_color="blue", command=generate)
# Text of button
trigger.configure(text="Generate")
trigger.place(x=206, y=60)
# Run the app
app.mainloop()
