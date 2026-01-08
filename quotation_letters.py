from fpdf import FPDF
from fpdf.enums import XPos, YPos, Align
import os

# --- 1. FUNCTION TO COLLECT INPUTS ---
def get_user_inputs():
    print("\n--- GENERAL SETTINGS ---")
    output_filename = input("Enter output filename (e.g. quote.pdf): ") or "output.pdf"
    if not output_filename.endswith('.pdf'):
        output_filename += ".pdf"

    print("\n--- HEADER & IMAGES ---")
    # Tip: You can drag and drop the file into the terminal to get the path
    header_path = input("Enter Header Image filename (e.g. letter_head.jpg): ")
    signature_path = input("Enter Signature Image filename (e.g. signature.png): ")

    print("\n--- RECIPIENT DETAILS ---")
    date_str = input("Enter Date (e.g. 12.05.2024): ")
    # We ask for address as a single line separated by commas for ease
    print("Enter Recipient Address (separate lines with commas).")
    print("Example: The Manager, ABC Corp, Hyderabad")
    address_raw = input("Address: ")
    address_lines = [x.strip() for x in address_raw.split(',')]

    print("\n--- LETTER CONTENT ---")
    subject = input("Enter Subject Line: ")
    
    print("\n(Tip: You can use **double stars** for bold text in the body)")
    print("Press ENTER to use the default Bitumen text, or type your own paragraph:")
    custom_body = input("Body: ")

    # Default text if user just hits Enter
    if not custom_body:
        custom_body = (
            "We wish to introduce ourselves as an Agency Transporting Bulk Bitumen. "
            "We are offering our most comfortable rate for **VG30 per MT Rs. 1000**, "
            "for **VG40 per MT Rs.1000**. Payment must be cleared within **45 days**."
        )

    print("\n--- FOOTER DETAILS ---")
    signer_name = input("Enter Signer Name (e.g. G. SRINU): ")
    company_name = input("Enter Company Name for Signature (e.g. For SRI SRINIVASA TRANSPORT): ")
    contact_info = input("Enter Footer Contact (e.g. Email: sst@gmail.com | Cell: 999999999): ")

    # Return all data as a dictionary
    return {
        "filename": output_filename,
        "header": header_path,
        "signature": signature_path,
        "date": date_str,
        "address": address_lines,
        "subject": subject,
        "body": custom_body,
        "signer": signer_name,
        "company": company_name,
        "contact": contact_info
    }

# --- 2. PDF GENERATION FUNCTIONS ---

def draw_header(pdf, image_path):
    if os.path.exists(image_path):
        pdf.image(image_path, x=10, y=8, w=190)
        pdf.ln(45) # Space for header
    else:
        print(f"Warning: Header image '{image_path}' not found. Skipping.")
        pdf.ln(10)

def draw_letter_details(pdf, recipient_lines, letter_date):
    pdf.set_font("helvetica", size=10)
    
    # Date (Right Aligned)
    pdf.set_x(140) 
    pdf.set_font("helvetica", "B", 10)
    pdf.cell(50, 5, f"Date: {letter_date}", align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)
    
    # Address (Left Aligned)
    pdf.set_x(20) 
    pdf.set_font("helvetica", "B", 10)
    pdf.cell(100, 5, "To,", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_font("helvetica", size=10)
    for line in recipient_lines:
        pdf.set_x(20)
        pdf.cell(100, 5, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(10)

def draw_body(pdf, subject, body_text):
    # Salutation
    pdf.set_x(20)
    pdf.set_font("helvetica", size=10)
    pdf.cell(0, 5, "Respected Sir,", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)

    # Subject
    pdf.set_font("helvetica", "B", 10)
    pdf.set_x(20)
    pdf.multi_cell(w=0, h=5, text=f"Sub: {subject}", align='C')
    pdf.ln(8)

    # Main Body with Markdown for Bold
    pdf.set_font("helvetica", size=10) 
    pdf.set_x(20)
    pdf.multi_cell(w=0, h=6, text=body_text, align='J', markdown=True)
    pdf.ln(15)

def draw_footer(pdf, data):
    # Closing
    pdf.set_x(20)
    pdf.cell(100, 5, "Thanking you", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(10)
    
    # Signature Block
    pdf.set_x(120)
    pdf.cell(60, 5, "Yours Faithfully", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_x(120)
    pdf.cell(60, 5, data['company'], align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    # Insert Signature Image
    if os.path.exists(data['signature']):
        pdf.image(data['signature'], x=135, y=pdf.get_y() + 2, w=30)
        pdf.ln(15) 
    else:
        print(f"Warning: Signature image '{data['signature']}' not found. Leaving blank space.")
        pdf.ln(20) 
    
    # Signer Name
    pdf.set_x(120)
    pdf.cell(60, 5, f"({data['signer']})", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    # Contact Info
    pdf.ln(5)
    pdf.set_x(20) # Center-ish or Right
    pdf.set_font("helvetica", size=9)
    # We put this across the whole page width, right aligned
    pdf.cell(0, 5, data['contact'], align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# --- 3. MAIN EXECUTION ---
if __name__ == "__main__":
    # 1. Ask user for data
    data = get_user_inputs()

    # 2. Create PDF
    pdf = FPDF()
    pdf.add_page()
    
    # 3. Draw parts
    draw_header(pdf, data['header'])
    draw_letter_details(pdf, data['address'], data['date'])
    draw_body(pdf, data['subject'], data['body'])
    draw_footer(pdf, data)
    
    # 4. Save
    pdf.output(data['filename'])
    print(f"\nSuccess! PDF saved as: {data['filename']}")
