import pyqrcode
from io import BytesIO
from urllib.parse import urlparse


def is_valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return all([parsed.scheme in ("http", "https"), parsed.netloc])


def generate_qrcode_image(url: str) -> BytesIO:
    if not is_valid_url(url):
        raise ValueError("URL inválida")

    try:
        qr = pyqrcode.create(url)

        buffer = BytesIO()
        qr.png(buffer, scale=8)
        buffer.seek(0)

        return buffer

    except Exception:
        raise ValueError("Erro ao gerar QRCode")
