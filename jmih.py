import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def open_file():
    filenames = filedialog.askopenfilenames(
        title="Choose your image",
        filetypes=[("Images", "*.jpg *.jpeg *.png *.bmp *.gif *.webp")]
    )
    if filenames:
        file_var.set(filenames[0])  # taking first file only

def save_file():
    filepath = file_var.get()
    if not filepath:
        messagebox.showerror("Error", "Choose the file first")
        return
    
    try:
        img = Image.open(filepath)

        save_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg")]
        )
        if save_path:
            img.save(
                save_path,
                "JPEG",
                optimize=True,
                quality=int(quality_var.get())
            )
            messagebox.showinfo("Done", f"File saved: {save_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

#   --- GUI ---
root = tk.Tk()
root.title("JMIH GUI - shakalizer")

file_var = tk.StringVar()
quality_var = tk.IntVar(value=1)

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Selected file:").grid(row=0, column=0, sticky="w")
tk.Entry(frame, textvariable=file_var, width=40).grid(row=0, column=1, padx=5)
tk.Button(frame, text="View", command=open_file).grid(row=0, column=2)

tk.Label(frame, text="Quality (1-100):").grid(row=1, column=0, sticky="w")
tk.Entry(frame, textvariable=quality_var, width=5).grid(row=1, column=1, sticky="w")

tk.Button(frame, text="Compress and save", command=save_file).grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
