
import re

class Tokenizer:
    """Konfigurowany tokenizator: HTML strip + case + min length filter."""
    def __init__(self, lower: bool = True, strip_html: bool = True, min_length: int = 1):
        self.lower = lower
        self.strip_html = strip_html
        self.min_length = min_length

    def tokenize(self, text: str) -> list[str]:
        # 1. jesli self.strip_html: usun znaczniki regex r"<[^>]+>"
        if self.strip_html:
            text = re.sub(r"<[^>]+>", "", text)

        # 2. jesli self.lower: text -> lowercase
        if self.lower:
            text = text.lower()
        # 3. tokeny = re.findall(r"\w+", text)  (UWAGA: musi lapac polskie litery -> uzyj re.UNICODE)
        tokeny = re.findall(r"\w+", text, re.UNICODE)
        # 4. zwroc [t for t in tokeny if len(t) >= self.min_length]
        return [t for t in tokeny if len(t) >= self.min_length]

    def vocab(self, texts: list[str]) -> set[str]:
        # TODO: unia tokenow ze wszystkich tekstow
        return set().union(*[self.tokenize(text) for text in texts])
