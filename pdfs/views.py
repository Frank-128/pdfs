from django.http import HttpResponse
from django.shortcuts import render
from .utils import tax_clearance_pdf_generate
def myHomePage(request):
    return render(request,'pdfs/home.html')

def generate_pdf(request):
    # Generate PDF using your function
    data = {'issued_date' : '22/03/23',
            'taxpayer_name':"Frank",
            "tin_number":"1122334455"}


    pdf = tax_clearance_pdf_generate(data)  # Replace 'data' with your actual data

    # Create an HttpResponse with the PDF content type
    response = HttpResponse(pdf, content_type='application/pdf')

    # Set the Content-Disposition header to force download or display in the browser
    response['Content-Disposition'] = 'inline; filename="tax_clearance_certificate.pdf"'

    return response

# def generate_pdf(request):
#     # Create a BytesIO buffer to hold the PDF
#     buffer = io.BytesIO()
#
#     # Create a PDF object, similar to your existing code
#     can = canvas.Canvas(buffer, pagesize=letter)
#     # Your PDF generation code here...
#     can.showPage()
#     can.save()
#
#     # Move the buffer's cursor to the beginning
#     buffer.seek(0)
#
#     # Create an HttpResponse with the PDF content type
#     response = HttpResponse(buffer, content_type='application/pdf')
#
#     # Set the Content-Disposition header to force download or display in the browser
#     response['Content-Disposition'] = 'inline; filename="tax_clearance_certificate.pdf"'
#
#     return response
