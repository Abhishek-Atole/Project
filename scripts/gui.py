import os
import tkinter as tk
from tkinter import filedialog, messagebox
from main import process_file

class MCQProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MCQ Processor")
        self.root.geometry("500x300")

        # Input directory label and button
        self.input_label = tk.Label(root, text="Select Input File:")
        self.input_label.pack(pady=10)
        self.input_button = tk.Button(root, text="Browse", command=self.select_input_file)
        self.input_button.pack()

        # Output directory label and button
        self.output_label = tk.Label(root, text="Select Output Directory:")
        self.output_label.pack(pady=10)
        self.output_button = tk.Button(root, text="Browse", command=self.select_output_directory)
        self.output_button.pack()

        # Process button
        self.process_button = tk.Button(root, text="Process File", command=self.process_file)
        self.process_button.pack(pady=20)

        # Status label
        self.status_label = tk.Label(root, text="", fg="green")
        self.status_label.pack(pady=10)

        # Variables to store paths
        self.input_file = None
        self.output_dir = None

    def select_input_file(self):
        self.input_file = filedialog.askopenfilename(
            filetypes=[("Supported Files", "*.docx *.pdf *.txt"), ("All Files", "*.*")]
        )
        if self.input_file:
            self.input_label.config(text=f"Input File: {os.path.basename(self.input_file)}")

    def select_output_directory(self):
        self.output_dir = filedialog.askdirectory()
        if self.output_dir:
            self.output_label.config(text=f"Output Directory: {self.output_dir}")

    def process_file(self):
        if not self.input_file:
            messagebox.showerror("Error", "Please select an input file.")
            return
        if not self.output_dir:
            messagebox.showerror("Error", "Please select an output directory.")
            return

        try:
            # Process the file
            file_name = os.path.basename(self.input_file)
            input_dir = os.path.dirname(self.input_file)
            process_file(file_name, input_dir, self.output_dir)

            # Update status
            self.status_label.config(text="File processed successfully!", fg="green")
            messagebox.showinfo("Success", "File processed successfully!")
        except Exception as e:
            self.status_label.config(text="Error processing file.", fg="red")
            messagebox.showerror("Error", f"An error occurred: {e}")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = MCQProcessorApp(root)
    root.mainloop()