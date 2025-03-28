from pathlib import Path

EXERCICES_FOLDER = 'docs/bac/exercices'


def get_file_stems(folder_path):
    file_stems = [file.stem for file in Path(folder_path).iterdir() if file.is_file()]
    return file_stems


stems = get_file_stems(EXERCICES_FOLDER)
stems.sort(key=lambda stem: stem[8:] if stem[6] == 'J' else stem[6:])

for stem in stems:
    print(f'| [<tt>{stem}</tt>](../bac/exercices/{stem}.pdf) | | — |')
