# gui_merge_pdf.py

import tkinter as tk
from tkinter import filedialog, messagebox
import os
import PyPDF2


def merge_pdfs(input_folder, output_pdf):
    if os.path.exists(output_pdf):
        os.remove(output_pdf)

    pdf_files = [file for file in os.listdir(input_folder) if file.endswith('.pdf')]
    pdf_files.sort()

    pdf_writer = PyPDF2.PdfWriter()

    for pdf in pdf_files:
        with open(os.path.join(input_folder, pdf), 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)


class PDFMergerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger Tool 🧩")
        self.root.geometry("400x200")
        self.input_folder = ""
        self.output_path = ""

        # Input folder selector
        self.select_btn = tk.Button(root, text="Select PDF Folder", command=self.select_folder)
        self.select_btn.pack(pady=10)

        self.label_folder = tk.Label(root, text="No folder selected")
        self.label_folder.pack()

        # Merge button
        self.merge_btn = tk.Button(root, text="Merge PDFs", command=self.merge)
        self.merge_btn.pack(pady=20)

    def select_folder(self):
        self.input_folder = filedialog.askdirectory()
        if self.input_folder:
            self.label_folder.config(text=f"Selected: {self.input_folder}")

    def merge(self):
        if not self.input_folder:
            messagebox.showerror("Error", "Please select a folder first.")
            return

        output_folder = os.path.join(self.input_folder, "merged_output")
        os.makedirs(output_folder, exist_ok=True)
        output_pdf = os.path.join(output_folder, "merged.pdf")

        try:
            merge_pdfs(self.input_folder, output_pdf)
            messagebox.showinfo("Success", f"PDFs merged successfully:\n{output_pdf}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to merge PDFs:\n{str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerGUI(root)
    root.mainloop()
