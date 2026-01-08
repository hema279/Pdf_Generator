from fpdf import FPDF
from fpdf.enums import XPos, YPos
import os
def draw_header(pdf, image_path):
    if os.path.exists(image_path):
        pdf.image(image_path, x=10, y=8, w=190)
        pdf.ln(55)
    else:
        pdf.ln(10)
def draw_invoice_details(pdf, customer_lines, invoice_date):
    top_y = pdf.get_y()

    pdf.set_x(10)
    pdf.set_font("helvetica", "B", size = 10)
    pdf.cell(100, 5, "TO,", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_font("helvetica", "B", size = 10)
    for line in customer_lines:
        pdf.cell(100, 5, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_y(top_y)
    pdf.set_x(150)
    pdf.set_font("helvetica", "B", 10)
    pdf.cell(50, 5, f"DATE: {invoice_date}", align='R', new_x = XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.ln(25)
    pdf.set_font("helvetica", "BU", 11)
    pdf.cell(0, 10, "BITUMEN TRANSPORTATION BILL", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)
def draw_table(pdf, data_list):
    col_widths = [30, 40, 70, 40]
    headers = ["Date", "Truck No", "Location", "Freight"]
    start_x = (210 - sum(col_widths)) / 2
    pdf.set_font("helvetica", "B", 9)
    pdf.set_fill_color(220, 220, 220)
    pdf.set_x(start_x)
    for i in range(len(headers)):
        pdf.cell(col_widths[i], 8, headers[i], border=1, fill=True, align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.ln()
    pdf.set_font("helvetica", size=9)
    total_amount = 0
    for row in data_list:
        date, truck, location, amount = row
        total_amount += amount
        pdf.set_x(start_x)
        pdf.cell(col_widths[0], 8, str(date), border=1, align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.cell(col_widths[1], 8, str(truck), border=1, align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.cell(col_widths[2], 8, str(location), border=1, align='L', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.cell(col_widths[3], 8, f"{amount:,.0f}", border=1, align='R', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.ln()
    pdf.set_font("helvetica", "B", 9)
    pdf.set_x(start_x)
    pdf.cell(sum(col_widths[:3]), 8, "Total Amount", border=1, align='R', new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(col_widths[3], 8, f"{total_amount:,.0f}", border=1, align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
def generate_bill():
    trip_data = [
        ("21-12-25", "AP31TF4989", "Jonnada", 15000),
        ("22-12-25", "AP39UT5949", "Karwar", 22500),
        ("23-12-25", "AP31TF2349", "Telangana", 12000),
    ]
    customer_info = [
        "VIJAYA LAKSHMI CONSTRUCTIONS,",
        "18-7-14, GF-114,",
        "VIJAYLAKSHMI CONSTRUCTION,",
        "MADHURAWADA, VISAKHAPATNAM.",
        "530048"
    ]
    image_file = "letter_head.jpg"
    output_filename = "transport_invoice.pdf"
    pdf = FPDF()
    pdf.add_page()
    draw_header(pdf, image_file)
    draw_invoice_details(pdf, customer_info, "25-12-25")
    draw_table(pdf, trip_data)
    pdf.output(output_filename)
    print(f"Success! Generated {output_filename}")

if __name__ == "__main__":
    generate_bill()
