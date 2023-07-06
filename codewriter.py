def writeLine(file, code, spacing):
    f = open(file, "a")
    spaces = " " * spacing
    text = spaces + code
    f.write(spaces + code)
    f.close()
    return text