from pathlib import Path

def dosya_bul(dosya_adi, arama_dizini="."):
    dosya = list(Path(arama_dizini).rglob(dosya_adi))
    return dosya[0] if dosya else None
