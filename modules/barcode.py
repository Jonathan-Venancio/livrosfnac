from barcode import EAN13
from barcode.writer import ImageWriter
from io import BytesIO

def gerar(ean):

    fp=BytesIO()

    EAN13(ean,writer=ImageWriter()).write(fp)

    fp.seek(0)

    return fp