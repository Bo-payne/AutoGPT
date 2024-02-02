import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
import json
import threading
import os  # For directory scanning
import openai

# Fetch the OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

# Check if the API key was successfully retrieved
if openai.api_key is None:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

class AutoGPTInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoGPT Interface")

        # UI setup
        tk.Label(root, text="This is TCL/Tk version 8.6").pack(pady=10)
        tk.Button(root, text="Run AutoGPT", command=self.run_auto_gpt).pack(pady=20)
        tk.Button(root, text="Click me!", command=self.click_me).pack(pady=10)
        tk.Button(root, text="Quit", command=root.destroy).pack(pady=10)
        self.status_label = tk.Label(root, text="AutoGPT is not running")
        self.status_label.pack(pady=10)
        tk.Button(root, text="Select File", command=self.select_file).pack(pady=10)
        tk.Button(root, text="Save Configuration", command=self.save_configuration).pack(pady=10)
        tk.Button(root, text="Scan Directory", command=self.scan_directory).pack(pady=10)

        # Command entry and submission
        tk.Label(root, text="Enter a command for AutoGPT:").pack(pady=5)
        self.command_entry = tk.Entry(root)
        self.command_entry.pack(pady=5)
        tk.Button(root, text="Submit Command", command=self.process_command).pack(pady=10)

        # Output window for command results
        tk.Label(root, text="Command Output:").pack(pady=5)
        self.command_output = scrolledtext.ScrolledText(root, height=10)
        self.command_output.pack(pady=5)

    def update_status_label(self, status):
        self.status_label.config(text=status)

    def run_auto_gpt(self):
        # This function should ideally start AutoGPT process. Placeholder for real implementation.
        self.update_status_label("Running AutoGPT... (Placeholder)")

    def click_me(self):
        messagebox.showinfo("Info", "This should be a cedilla: Ç")

    def select_file(self):
        file_path = filedialog.askopenfilename(title="Select a file for AutoGPT to process",
                                               filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path:
            self.update_status_label(f"Selected file: {file_path}")

    def save_configuration(self):
        config = {'example_setting': 'example_value'}
        file_path = filedialog.asksaveasfilename(defaultextension=".json",
                                                 filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as config_file:
                json.dump(config, config_file)
            messagebox.showinfo("Configuration Saved", f"Saved to: {file_path}")

    def process_command(self):
        command = self.command_entry.get()
        if command:
            # This is a placeholder for the function to process the command with AutoGPT.
            self.command_output.insert(tk.END, f"Command processed: {command} (Placeholder)\n")

    def scan_directory(self):
        directory_path = filedialog.askdirectory(title="Select a Directory to Scan")
        if directory_path:
            self.update_status_label(f"Scanning directory: {directory_path}")
            for entry in os.listdir(directory_path):
                self.command_output.insert(tk.END, f"{entry}\n")
            self.update_status_label("Directory scan complete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoGPTInterface(root)
    root.mainloop()
