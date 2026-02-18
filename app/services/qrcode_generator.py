# PEP8 OK
# -*- coding: utf-8 -*-

import pyqrcode
from io import BytesIO
from urllib.parse import urlparse


def normalize_url(url: str) -> str:
    """
    Garante que a URL tenha esquema (http/https).
    Se não tiver, adiciona https automaticamente.
    """
    parsed = urlparse(url)

    if not parsed.scheme:
        url = "https://" + url

    return url


def is_valid_url(url: str) -> bool:
    """
    Valida se a URL possui:
    - Esquema http ou https
    - Netloc válido
    - Pelo menos um ponto no domínio
    """
    parsed = urlparse(url)

    return parsed.scheme in ("http", "https") and parsed.netloc and "." in parsed.netloc


def generate_qrcode_image(url: str) -> BytesIO:
    """
    Gera imagem PNG do QRCode a partir da URL validada.
    Retorna BytesIO pronto para StreamingResponse.
    """

    url = normalize_url(url)

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
