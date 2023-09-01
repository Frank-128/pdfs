import os
import base64
from PyPDF2 import PdfReader, PdfWriter
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# custom font
# pdfmetrics.registerFont(TTFont("Arial", "arial.ttf"))
font_size = 12
# font_family = " "
# variable for Tax residency certificate
refNumberX = 75
refNumberY = 539
issuedDateX = 442
issuedDateY = 571
nameOfPersonX = 280
nameOfPersonY = 364
passportNumberX = 500
passportNumberY = 476
personCitizenX = 315
personCitizenY = 464
tradingNameX = 70
tradingNameY = 552
bussinessActivityX = 320
bussinessActivityY = 332
tinX = 115
tinY = 348
telephoneNoX = 370
telephoneNoY = 443
expireDateX = 420
expireDateY = 558
issueOfficeX = 429
issueOfficeY = 490
passportNumber1 = "17363Ay"
passportNumberX1 = 135
passportNumberY1 = 305
vatRegNo = "123456789"
vatRegNoX = 80
vatRegNoY = 429
comapanyRegNo = '987456'
comapanyRegNoX = 270
comapanyRegNoY = 429
# natureOfPerson = "Self-employed"
# natureOfPersonX = 333
# natureOfPersonY = 456
# CountryofIncorporation = "United Replublic Of Tanzania"
# CountryofIncorporationX = 333
# CountryofIncorporationY = 440
# ResidenceforTaxationPurpose = "United Replublic Of Tanzania"
# ResidenceforTaxationPurposeX = 333
# ResidenceforTaxationPurposeY = 425
# EndofGovernmentfinancialyear = "Dec 31"
# EndofGovernmentfinancialyearX = 132
# EndofGovernmentfinancialyearY = 375
SIGNATUREX = 160
SIGNATUREY = 255
# signature_image_path = "E:\\endgame\\WebTechnologies\\python\\Signature.png"
signature_image_path = ""
COMMISSIONERGENERALNAME = "Jackson Moon Kitonga"
COMMISSIONERGENERALNAMEX = 125
COMMISSIONERGENERALNAMEY = 395
SIGNATUREDATE = "16/Jul/2023"
SIGNATUREDATEX = 410
SIGNATUREDATEY = 170
qrcode_image_path = ""
# qrcode_image_path = "E:\\endgame\\WebTechnologies\\python\\qrcode.png"
QRCODEX = 450
QRCODEY = 140


def tax_clearance_pdf_generate(data):
    refNumber = '1234567890'
    issuedDate = str(data.get('issued_date'))
    nameOfPerson = str(data.get('taxpayer_name'))
    personCitizen = "Tanzania"
    tradingName = " INFORMATION TECHNOLOGIES LTD"
    tin = str(data.get('tin_number'))
    issueOffice = "TRA - ILALA"
    telephoneNo = "222678909"
    expireDate = '20/Aug/2023'
    bussinessActivity = "SOFTWARE AND ICT CONSULTATIONS"
    # nameOfPerson1 = "Said Mohamed Omary"
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    # can.setFont( font_size)
    can.drawString(refNumberX, refNumberY, refNumber)
    can.drawString(issuedDateX, issuedDateY, issuedDate)
    can.drawString(nameOfPersonX, nameOfPersonY, nameOfPerson)
    can.drawString(tradingNameX, tradingNameY, tradingName)
    can.drawString(issueOfficeX, issueOfficeY, issueOffice)
    can.drawString(comapanyRegNoX, comapanyRegNoY, comapanyRegNo)
    can.drawString(telephoneNoX, telephoneNoY, telephoneNo)
    can.drawString(vatRegNoX, vatRegNoY, vatRegNo)
    can.drawString(expireDateX, expireDateY, expireDate)
    can.drawString(tinX, tinY, tin)
    can.drawString(bussinessActivityX, bussinessActivityY, bussinessActivity)
    # can.drawString(
    #     CountryofIncorporationX, CountryofIncorporationY, CountryofIncorporation
    # )
    # can.drawString(
    #     ResidenceforTaxationPurposeX,
    #     ResidenceforTaxationPurposeY,
    #     ResidenceforTaxationPurpose,
    # )
    # can.drawString(
    #     EndofGovernmentfinancialyearX,
    #     EndofGovernmentfinancialyearY,
    #     EndofGovernmentfinancialyear,
    # )
    can.drawString(
        COMMISSIONERGENERALNAMEX, COMMISSIONERGENERALNAMEY, COMMISSIONERGENERALNAME
    )
    can.drawString(SIGNATUREDATEX, SIGNATUREDATEY, SIGNATUREDATE)
    # can.drawString(
    #     signature_image_path, SIGNATUREX, SIGNATUREY, width=50, height=50, mask="auto"

    # )
    # can.drawString(
    #     qrcode_image_path, QRCODEX, QRCODEY, width=120, height=120, mask="auto"
    # )
    can.save()
    # Move to the beginning of the StringIO buffer
    packet.seek(0)
    # Create a new PDF with Reportlab
    new_pdf = PdfReader(packet)
    # Read your existing PDF
    file_path = os.path.join(
        # os.path.dirname(file),
        "./order_certified_ballif.pdf"
    )
    # Open the existing PDF file and keep it open until merging is done
    with open(file_path, "rb") as pdf_file:
        existing_pdf = PdfReader(pdf_file)
        output = PdfWriter()
        # Add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)
        # Create a BytesIO buffer to store the result
        output_stream = io.BytesIO()
        output.write(output_stream)
        # Move the buffer's cursor to the beginning
        output_stream.seek(0)
        return output_stream.getvalue()

