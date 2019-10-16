from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from urllib.request import urlopen

def leituraPDF(pdf):
    recursos = PDFResourceManager()
    buffer = StringIO()
    layoutParams = LAParams()
    dispositivo = TextConverter(recursos, buffer, laparams=layoutParams)
    process_pdf(recursos, dispositivo, pdf)
    dispositivo.close()
    conteudo = buffer.getvalue()
    buffer.close()
    return conteudo