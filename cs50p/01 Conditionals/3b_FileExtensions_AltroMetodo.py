"""
Altro metodo per risolvere il problema
"""


def main():
    file_name = input("Enter the filename: ")

    match estrai_estensione(file_name):
        case ".jpg" | ".jpeg":
            print("image/jpeg")
        case ".gif":
            print("image/gif")
        case ".png":
            print("image/png")
        case ".pdf":
            print("application/pdf")
        case ".txt":
            print("text/plain")
        case ".zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


def estrai_estensione(f):
    f = f.casefold().strip()

    if len(f) > 4:
        if f[-5:] == ".jpeg":
            return ".jpeg"
        else:
            return f[-4:]
    else:
        return ""


main()
