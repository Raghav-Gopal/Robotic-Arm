import PyPDF2

# Path to the locked PDF file
pdf_file_path = "C:\\Users\\Dell\\Downloads\\CLUE 5.pdf"

# Function to attempt unlocking the PDF
def unlock_pdf(pdf_path):
    # Open the PDF in binary read mode
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        
        # Iterate through all possible combinations of the password
        for i in range(1, 100):
            for j in range(1, 100):
                for k in range(1, 100):
                    for h in range(1, 100):
                        # Format each number as two digits (e.g., 01, 02, etc.)
                        password = f"{i:02}{j:02}{k:02}{h:02}"
                        print(password)  # For debugging, prints the password being tried
                        
                        # Attempt to decrypt the PDF with the current password
                        if reader.decrypt(password) == 1:
                            print(f"PDF unlocked successfully! The password is: {password}")
                            return True
        
        print("Failed to unlock the PDF.")
        return False

# Run the unlock function
unlock_pdf(pdf_file_path)
