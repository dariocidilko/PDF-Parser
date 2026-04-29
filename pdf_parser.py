import pymupdf
import os

def pdf_parser(filepath):
    document = pymupdf.open(filepath)
    document_text = "" # Initialize the variable that will be used to store text from the PDF.
    document_images = set() # Initialize the set that will be used to store images from the PDF.
    document_links = set() # Initialize the set that will be used to store links from the PDF.
    document_files = set() # Initialize the set that will be used to store files from the PDF.

    # This is the main loop to iterate through pages in the PDF.
    for page in document:
        document_text += page.get_text("text")

        # Get all unique images from the PDF file.
        for image in page.get_images():
            document_images.add(image)
        
        # Get all unique external links from the PDF file.
        for link in page.get_links():
            if "uri" in link:
                document_links.add(link["uri"])

    # Get all unique files from the PDF file.
    for file in document.embfile_names():
        document_files.add(file)

    # Check if the document was scanned successfully.
    if document_text == "" and len(document_images) == 0 and len(document_files) == 0:
        document.close()
        return f"The PDF: {filepath} may have been flattened, corrupted or is empty. \n"
    else:
        print(document_text)
        print(f"There was {len(document_images)} unique image(s) in the document. \n")
        print(f"There was {len(document_links)} unique link(s) in the document. \n")
        print(f"There was {len(document_files)} unique file(s) in the document. \n")
        
        document.close()
        return f"The document was scanned successfully. \n"

if __name__ == "__main__":
    while True:
        filepath = input("Enter the filepath to the PDF: ").strip()

        # Check if the filepath the user provided is valid.
        if not os.path.exists(filepath):
            print(f"The filepath: {filepath} is invalid. Please try again. \n")
        else:
            parsed_file = pdf_parser(filepath)
            print(parsed_file)
            break