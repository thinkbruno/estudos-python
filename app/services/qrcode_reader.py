from pyzbar.pyzbar import decode
from PIL import Image
from io import BytesIO


def read_qrcode_image(file_bytes: bytes) -> str:
    try:
        image = Image.open(BytesIO(file_bytes))
        decoded_objects = decode(image)

        if not decoded_objects:
            raise ValueError("QR Code não encontrado")

        return decoded_objects[0].data.decode("utf-8")

    except Exception:
        raise ValueError("Erro ao ler QR Code")
