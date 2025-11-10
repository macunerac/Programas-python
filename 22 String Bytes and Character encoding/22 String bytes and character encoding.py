import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()
    
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    
    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

#Correr el script en CMD como abajo, pasarle el dato de strict replace igonre para ver que hace
#investaiar https://docs.python.org/3/library/stdtypes.html#str.encode
#EN CMD entrar al directorio y abrir el archivo conmo lo siguiente
#C:\Users\Humberto Molina\Desktop\Programas python\22 String Bytes and Character encoding>python "22 String bytes and character encoding.py" "utf-8" "ignore"

