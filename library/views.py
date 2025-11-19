

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO

@login_required
def library_home(request):
    reading_text = ""
    if request.method == "POST":
        reading_text = request.POST.get("reading_text", "")

        # Check if PDF button was clicked
        if "download_pdf" in request.POST:
            template = get_template("library/library_pdf.html")
            html = template.render({"reading_text": reading_text})
            response = HttpResponse(content_type="application/pdf")
            response["Content-Disposition"] = 'attachment; filename="LibraryGate.pdf"'

            pisa_status = pisa.CreatePDF(html, dest=response)
            if pisa_status.err:
                return HttpResponse("Error generating PDF")
            return response

    return render(request, "library/library.html", {"reading_text": reading_text})