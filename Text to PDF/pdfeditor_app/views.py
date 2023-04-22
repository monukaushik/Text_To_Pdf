from django.shortcuts import render
from fpdf import FPDF

def index(request):
   if request.method=='POST':
      text1=request.POST.get('text')

      # save FPDF() class into a
      # variable pdf
      pdf = FPDF()

      # Add a page
      pdf.add_page()

      # set style and size of font
      # that you want in the pdf
      pdf.set_font("Arial", size = 15)

      # create a cell
      pdf.multi_cell(0, 10, txt = text1,   
            align = 'L')

      # save the pdf with name .pdf
      pdf.output("GFG.pdf")


   return render(request,'index.html')




