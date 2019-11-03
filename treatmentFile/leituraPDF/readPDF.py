import io

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from tika import parser


def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)


    for page in PDFPage.get_pages(pdf_path,
                                  caching=True,
                                  check_extractable=True):
        page_interpreter.process_page(page)

    text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()

    if text:
        return text


def vaiNaFePDF(nome):
    raw = parser.from_buffer(nome)
    s = str(raw['content'])
    index=0
    top=0
    while s[top]=='\n':
        top+=1
    botton=len(s)-1
    while s[botton]=='\n':
        botton-=1

    a=s[top:botton]
    print(a)


def pdf_to_txt(nome):
    try:
        texto = extract_text_from_pdf(nome)
        if (len(texto)<10):
            texto = vaiNaFePDF(nome)
        return texto
    except:
        texto = vaiNaFePDF(nome)
        return texto