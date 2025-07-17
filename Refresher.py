import ctypes
import time
import tkinter as tk
from tkinter import messagebox
import threading

def refresh_desktop():
    # Call SystemParametersInfo with SPI_SETDESKWALLPAPER to refresh desktop
    ctypes.windll.user32.SystemParametersInfoW(20, 0, None, 0)

def run_refresh(num_refreshes, status_label, start_button):
    try:
        if num_refreshes <= 0:
            status_label.config(text="Please enter a positive number.", fg="#FF5555")
            start_button.config(state="normal")
            return
        
        status_label.config(text=f"Starting {num_refreshes} refreshes...", fg="#55FF55")
        for i in range(num_refreshes):
            refresh_desktop()
            time.sleep(0.1)  # Small delay to prevent system overload
            status_label.config(text=f"Refresh {i + 1}/{num_refreshes} completed.")
            status_label.update()  # Update GUI during loop
        status_label.config(text="Refresh completed!", fg="#55FF55")
        
    except Exception as e:
        status_label.config(text=f"Error: {e}", fg="#FF5555")
    finally:
        start_button.config(state="normal")

def start_refresh():
    try:
        num_refreshes = int(entry.get())
        start_button.config(state="disabled")  # Disable button during refresh
        status_label.config(text="Starting...", fg="#55FF55")
        # Run refresh in a separate thread to keep GUI responsive
        threading.Thread(target=run_refresh, args=(num_refreshes, status_label, start_button), daemon=True).start()
    except ValueError:
        status_label.config(text="Invalid input. Enter a number.", fg="#FF5555")

# Set up the GUI
root = tk.Tk()
root.title("Hacker Desktop Refresher")
root.geometry("400x300")
root.configure(bg="#1A1A1A")  # Dark background

# Styling
font_style = ("Consolas", 12)  # Monospaced font for hacker aesthetic
neon_green = "#55FF55"
dark_bg = "#1A1A1A"

# Title label
title_label = tk.Label(root, text="Desktop Refresher", font=("Consolas", 16, "bold"), fg=neon_green, bg=dark_bg)
title_label.pack(pady=20)

# Input field
input_frame = tk.Frame(root, bg=dark_bg)
input_frame.pack(pady=10)
tk.Label(input_frame, text="Number of Refreshes:", font=font_style, fg=neon_green, bg=dark_bg).pack(side="left")
entry = tk.Entry(input_frame, font=font_style, fg=neon_green, bg="#333333", insertbackground=neon_green, width=10)
entry.pack(side="left", padx=10)

# Start button
start_button = tk.Button(root, text="Start Refresh", font=font_style, fg=dark_bg, bg=neon_green, activebackground="#33DD33",
                        command=start_refresh, relief="flat", padx=10, pady=5)
start_button.pack(pady=20)

# Status label
status_label = tk.Label(root, text="Enter a number and click Start.", font=font_style, fg=neon_green, bg=dark_bg)
status_label.pack(pady=10)

# Run the GUI
root.mainloop()