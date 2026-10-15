import os
import shutil

pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")

tipos = {
    "Imagens":  [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "PDFs":     [".pdf"],
    "Videos":   [".mp4", ".mov", ".avi", ".mkv"],
    "Musicas":  [".mp3", ".wav", ".ogg", ".flac"],
    "Documentos": [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"],
    "Compactados": [".zip", ".rar", ".7z", ".tar"],
}

def encontrar_categoria(extensao):
    for categoria, extensoes in tipos.items():
        if extensao.lower() in extensoes:
            return categoria
    return "Outros"

movidos = 0
for arquivo in os.listdir(pasta_downloads):
    caminho = os.path.join(pasta_downloads, arquivo)
    if os.path.isfile(caminho):
        _, ext = os.path.splitext(arquivo)
        categoria = encontrar_categoria(ext)
        destino = os.path.join(pasta_downloads, categoria)
        os.makedirs(destino, exist_ok=True)
        shutil.move(caminho, os.path.join(destino, arquivo))
        print(f"Movido: {arquivo} → {categoria}/")
        movidos += 1

print(f"\nPronto! {movidos} arquivo(s) organizado(s).")