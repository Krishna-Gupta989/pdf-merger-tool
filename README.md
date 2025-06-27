# PDF Merger Tool 🧩

This is a simple Python-based tool to merge multiple PDF files into a single file. It is useful for combining multiple documents in one step — saving time and effort!

---

## 📂 Folder Structure

```

project-root/
│
├── merge\_pdf.py           ← Main Python script (CLI)
├── gui\_merge\_pdf.py       ← ✅ GUI-based script using tkinter
├── .gitignore
├── README.md
└── output/
├── pdf\_files/         ← Place your PDF files here
└── merged\_output.pdf  ← This is the final merged PDF (auto-generated)

````

---

## 🚀 How to Use

### 1. Add your PDF files
- Go to the folder: `output/pdf_files/`
- Add all the `.pdf` files you want to merge

### 2. Run the script (Command Line)
If you have Python installed, open terminal or command prompt and run:

```bash
python merge_pdf.py
````

### 3. Run with GUI (Optional)

You can also use the graphical version of the tool:

```bash
python gui_merge_pdf.py
```

A window will open to select a folder and merge your PDFs easily.

---

## 💻 Executable (.exe) Version

If you don't have Python installed, you can use the executable version (created using auto-py-to-exe).

⚠️ Note: The .exe file is not included in this repository due to file size limits.
You can request it from the author if needed.

---

## 🛠 Built With

* Python 3
* PyPDF2
* auto-py-to-exe
* tkinter (built-in GUI module)

---

## 📌 Author

**Krishn Kumar**
Created as a personal file automation project.
[www.linkedin.com/in/krishn-kumar-650462290](http://www.linkedin.com/in/krishn-kumar-650462290)

---

### ✨ GUI Feature Added By

**Harsh Gupta**
Added a tkinter-based GUI for folder selection and PDF merging.

