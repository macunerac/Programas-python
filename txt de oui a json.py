import re
import json
import requests

# URL oficial del archivo OUI
OUI_URL = "https://standards-oui.ieee.org/oui/oui.txt"

def download_oui_file(url: str) -> str:
    """Descarga el archivo oui.txt desde IEEE."""
    print(f"Descargando {url} ...")
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.text

def parse_oui_text(text: str) -> dict:
    """Convierte el texto del OUI a un diccionario."""
    oui_dict = {}
    # Ejemplo de línea: "00-11-22   (hex)    CISCO SYSTEMS, INC."
    pattern = re.compile(r"^([0-9A-Fa-f]{2}-[0-9A-Fa-f]{2}-[0-9A-Fa-f]{2})\s+\(hex\)\s+(.+)$")

    for line in text.splitlines():
        match = pattern.match(line)
        if match:
            oui = match.group(1).replace("-", "").upper()
            vendor = match.group(2).strip()
            oui_dict[oui] = vendor
    return oui_dict

def save_to_json(data: dict, filename: str):
    """Guarda el diccionario en formato JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Archivo JSON generado: {filename}")

def main():
    text = download_oui_file(OUI_URL)
    oui_dict = parse_oui_text(text)
    print(f"Se encontraron {len(oui_dict)} registros.")
    save_to_json(oui_dict, "oui.json")

if __name__ == "__main__":
    main()
