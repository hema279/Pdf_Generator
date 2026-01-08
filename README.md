# Pdf_Generator
# Transport PDF Generator

A Python-based automation tool designed to generate professional PDF invoices and quotation letters for transport and logistics businesses. This project eliminates manual data entry by creating dynamic, formatted documents using the **FPDF2** library.

## Features

* **Universal Quotation Generator:** Interactive CLI tool that asks for user inputs (Client Name, Address, Subject) and generates a custom PDF.
* **Dynamic Formatting:** Supports bold text highlighting within PDF paragraphs (using Markdown-like syntax).
* **Image Handling:** Automatically embeds company letterheads and digital signatures into the documents.
* **Command Line Arguments:** Supports passing details via terminal arguments for quick batch processing.
* **Professional Layout:** Auto-adjusts margins, text alignment (Justified/Center), and page breaks.

## Tech Stack

* **Language:** Python 3.12+
* **Libraries:** `fpdf2`, `argparse`, `os`

