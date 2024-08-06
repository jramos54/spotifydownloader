from looking_directories import run_matching_files
from arrange_files import run_sorting
from create_favoritos import run_favorites



if __name__ == "__main__":
    ruta=r"F:\MUSICA\Musica"
    run_matching_files(ruta)
    run_sorting(ruta)
    run_favorites(ruta)