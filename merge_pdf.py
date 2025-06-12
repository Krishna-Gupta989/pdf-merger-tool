import PyPDF2
import os

def merge_pdfs(input_folder, output_pdf):
    # Remove the existing merged.pdf file if it exists
    if os.path.exists(output_pdf):
        os.remove(output_pdf)

    # Get a list of PDF files in the input folder
    pdf_files = [file for file in os.listdir(input_folder) if file.endswith('.pdf')]

    # Sort the list of PDF files (this is optional)
    pdf_files.sort()

    # Create a PdfWriter object
    pdf_writer = PyPDF2.PdfWriter()

    # Loop through each PDF file and merge it
    for pdf in pdf_files:
        with open(os.path.join(input_folder, pdf), 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

    # Write the merged PDF to the output file
    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)



# Let's use the function
input_folder = "pdffiles"  # Path to the folder containing PDFs
output_pdf = "output/pdf_files/merged.pdf"  # Output PDF file name (relative path)

merge_pdfs(input_folder, output_pdf)
