import requests
from bs4 import BeautifulSoup
from io import BytesIO


def extract_text_from_url(url: str) -> BytesIO:
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove scripts e styles
        for script in soup(["script", "style"]):
            script.decompose()

        # Primeiro tenta pegar <p>
        paragraphs = soup.find_all("p")
        text = "\n".join(p.get_text(strip=True) for p in paragraphs)

        # Se não houver <p>, pega texto geral
        if not text.strip():
            text = soup.get_text(separator="\n", strip=True)

        if not text.strip():
            raise ValueError("Nenhum texto encontrado na página.")

        return BytesIO(text.encode("utf-8"))

    except requests.exceptions.RequestException:
        raise ValueError("Erro ao acessar a URL.")

    except Exception:
        raise ValueError("Erro ao processar a página.")
