import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_time)  # Update every 1000ms (1 second)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=('Helvetica', 48), bg='black', fg='red')
label.pack(fill='both', expand=True)

update_time()  # Start the clock update loop
root.mainloop()