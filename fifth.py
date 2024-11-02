
import sys

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length): 
    """
    Tato funkce načte binární soubor z cesty file_name,
    z něj přečte prvních header_length bytů a ty vrátí pomocí return
    """
    with open(file_name, "rb") as file:  
        header = file.read(header_length) 
    return b'header'


def is_jpeg(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanou hlavičkou v proměnné jpeg_header
    """
        # načti hlavičku souboru
    header = read_header(file_name, len(jpeg_header))
    with open(file_name, "rb") as file:
            header = file.read(2)
            
            # Vyhodnotíme, zda se jedná o JPEG
            if header == jpeg_header:
                return True
            else:
                return False

def is_gif(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanými hlavičkami v proměnných gif_header1 a gif_header2
    """
    with open(file_name, "rb") as file:
        gif_header = file.read(6)

    # vyhodnoť zda je soubor gif
    if gif_header == gif_header1 or gif_header == gif_header2:
        return True
    else:
        return False


def is_png(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanou hlavičkou v proměnné png_header
    """
    with open(file_name, "rb") as file:
        png_header1 = file.read(8)

    # vyhodnoť zda je soubor png
    if png_header1 == png_header:
        return True
    else:
        return False


def print_file_type(file_name):
    """
    Funkce vypíše typ souboru - tuto funkci není třeba upravovat
    """
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')


if __name__ == '__main__':
        # přidej try-catch blok, odchyť obecnou vyjímku Exception a vypiš ji
    
    try:
        file_name = sys.argv[1]
        print_file_type(file_name)
    except IndexError:
        print("Zadej nazev soboru")
    except FileNotFoundError:
        print("Soubor neexistuje")
    