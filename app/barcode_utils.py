from barcode import EAN13
from barcode.writer import ImageWriter
from io import BytesIO


def gerar_barcode(ean):

    buffer = BytesIO()

    barcode = EAN13(str(ean), writer=ImageWriter())

    barcode.write(buffer)

    buffer.seek(0)

    return buffer