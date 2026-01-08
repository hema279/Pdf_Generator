from fpdf import FPDF
from fpdf.enums import XPos, YPos, Align
import os

# 1. Header (Checks for logo file)
def draw_header(pdf, image_path):
    if os.path.exists(image_path):
        pdf.image(image_path, x=10, y=8, w=190)
        pdf.ln(55) 
    else:
        # If no logo found, just make space
        pdf.ln(10)

# 2. Letter Details (Date and Address)
def draw_letter_details(pdf, recipient_lines, letter_date):
    pdf.set_font("helvetica", size=10)
    
    # --- DATE ---
    pdf.set_x(140) 
    pdf.set_font("helvetica", "B", 10)
    pdf.cell(50, 5, f"Date: {letter_date}", align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.ln(5)
    
    # --- TO ADDRESS ---
    pdf.set_x(20) 
    pdf.set_font("helvetica", "B", 10)
    pdf.cell(100, 5, "To,", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_font("helvetica", size=10)
    for line in recipient_lines:
        pdf.set_x(20)
        pdf.cell(100, 5, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.ln(10)

# 3. The Letter Body (Generic Template)
def draw_body(pdf):
    # --- Salutation ---
    pdf.set_x(20)
    pdf.set_font("helvetica", size=10)
    pdf.cell(0, 5, "Respected Sir,", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)

    # --- Subject Line ---
    pdf.set_font("helvetica", "B", 10)
    subject = "Sub: Quotation for Transport Services [MATERIAL NAME]"
    pdf.set_x(20)
    pdf.multi_cell(w=0, h=5, text=subject, align='C')
    pdf.ln(8)

    # --- Main Paragraph ---
    pdf.set_font("helvetica", size=10) 
    
    # Dummy Text with placeholders
    text_p1 = (
        "We wish to introduce ourselves as a transport agency. "
        "We are interested in transporting materials from **[SOURCE LOCATION]** "
        "to your work site **[DESTINATION SITE]**. We are offering our most competitive "
        "rates: **Material A for Rs. 0000 per MT**, **Material B for Rs. 0000 per MT**. "
        "Margin of shortage allowed is **0.5%**. "
        "Halting charges of **Rs. 000/-** will apply if the vehicle is detained after 48 hours. "
        "Payment terms are **30-45 days** from the date of billing."
    )
    
    # markdown=True enables the bold text for the placeholders
    pdf.set_x(20)
    pdf.multi_cell(w=0, h=6, text=text_p1, align='J', markdown=True)
    pdf.ln(5)

    # --- Final Sentence ---
    text_p2 = "Please kindly accept our quotation."
    pdf.set_x(20)
    pdf.multi_cell(w=0, h=6, text=text_p2, align='J', markdown=True)
    pdf.ln(15)

# 4. Closing & Signature
def draw_footer(pdf):
    pdf.set_x(20)
    pdf.cell(100, 5, "Thanking you", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.ln(10)
    
    # Right side signature block
    pdf.set_x(120)
    pdf.cell(60, 5, "Yours Faithfully", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_x(120)
    pdf.cell(60, 5, "For [YOUR COMPANY NAME]", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.ln(20) # Space for signature image
    
    pdf.set_x(120)
    pdf.cell(60, 5, "([SIGNER NAME])", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.ln(5)
    pdf.set_x(100)
    pdf.set_font("helvetica", size=9)
    pdf.cell(80, 5, "Email: email@example.com | Cell: 0000000000", align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# 5. Main Execution
def generate_quotation():
    # Dummy Client Address
    recipient_address = [
        "The Project Manager,",
        "Client Company Name,",
        "Site Location,",
        "City, State - Pin Code."
    ]
    
    image_file = "letter_head.jpg"
    output_filename = "quotation_template.pdf"

    pdf = FPDF()
    pdf.add_page()
    
    draw_header(pdf, image_file)
    draw_letter_details(pdf, recipient_address, "DD-MM-YYYY")
    draw_body(pdf)
    draw_footer(pdf)
    
    pdf.output(output_filename)
    print(f"Success! Generated {output_filename}")

if __name__ == "__main__":
    generate_quotation()
