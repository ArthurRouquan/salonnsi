"""
Utilisation :
    1. Télécharger les sujets (comme 25-NSIJ2G11.pdf) et les ajouter dans docs/annales/sujets/
    2. Ajouter leurs informations dans docs/annales/metadata.csv ; par exemple pour le sujet 24-NSIJ2PO1.pdf :

        repere;page1;page2;page3;theme1;theme2;theme3
        ...
        24-NSIJ2PO1;2-5,16;6-9;10-15;File,Pile,Graphe;ABR,POO,Récursivité;Réseau,SQL,Programmation
        ...

    3. Exécuter la commande `$ python scripts/addsujects.py`

Le script, pour chaque sujet comme 25-NSIJ2G11.pdf :
    1. Sépare le sujet en trois exercices, 25-NSIJ2G11-1.pdf, 25-NSIJ2G11-2.pdf etc. dans docs/annales/exercices/ (ne fait rien si existe déjà)
    2. Génère trois fichiers markdown 25-NSIJ2G11-1.md, 25-NSIJ2G11-2.md dans docs/annales/corrections/ (ne fait rien si existe déjà)
       Ces fichiers contient, par exemple pour 25-NSIJ2G11-1.md :

        ---
        title: 25-NSIJ2G11-1
        ---

        <div class="circle-ol" markdown>
        </div>

    3. Ajoute trois lignes dans la table de la section « ### Sujets 20XX » (où XX est 24, 25, etc. suivant le code) dans le fichier docs/annales/index2.md (ne fait rien si existe déjà) :

        ### Sujets 2025

        | Exercice | Thèmes | Correction |
        | :------- | :----- | :--------: |
        ...
        | 25-NSIJ2G11-1 | [Thème de l'exercice 1]  | [Lien vers docs/annales/corrections/25-NSIJ2G11-1.md]  |
        | 25-NSIJ2G11-2 | [Thème de l'exercice 1]  | [Lien vers docs/annales/corrections/25-NSIJ2G11-2.md]  |
        | 25-NSIJ2G11-3 | [Thème de l'exercice 1]  | [Lien vers docs/annales/corrections/25-NSIJ2G11-3.md]  |

Maintenant tu peux juste t'occuper de la correction ! Pas mal, non ?! :)
"""

import csv
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
from tqdm import tqdm
from yachalk import chalk

ANNALES_ROOT = 'docs/annales/'
CORRECTIONS_FOLDER = ANNALES_ROOT + 'corrections/'
EXERCICES_FOLDER = ANNALES_ROOT + 'exercices/'
SUJETS_FOLDER = ANNALES_ROOT + 'sujets/'
METADATA_PATH = ANNALES_ROOT + 'metadata.csv'
INDEX_PATH = ANNALES_ROOT + 'index.md'


def get_table_line(exercice_code: str, themes: str):
    themes_html = ''.join(f'<span class="tag">{theme}</span>' for theme in sorted(themes.split(',')))
    return f'| [:fontawesome-solid-file-pdf: <tt>{exercice_code[6:]}</tt>](exercices/{exercice_code}.pdf) | <span class="tags-container">{themes_html}</span> | [:material-open-in-new:](corrections/{exercice_code}.md) |\n'


def parse_page_ranges(pages_str: str) -> list[int]:
    # parse_page_ranges('2-5,16') renvoie [1, 2, 3, 4, 15]
    pages = []
    for part in pages_str.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            pages.extend(range(start, end + 1))
        else:
            pages.append(int(part))
    return [p - 1 for p in pages]  # PyPDF2 utilise des index 0-based


def extract_pages(pdf_path: str, page_indices: list[int], output_path: str, force: bool = False):
    if not force and Path(output_path).exists():
        # print(chalk.blue(f'[Ignore] {chalk.bold(Path(output_path).name)} already exists.'))
        return
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for idx in page_indices:
        if 0 <= idx < len(reader.pages):
            writer.add_page(reader.pages[idx])
    with open(output_path, 'wb') as f:
        writer.write(f)
        print(chalk.green(f'[New] {Path(output_path).name} created.'))


def load_csv(csv_path):
    with open(csv_path, encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter=';'))


def write_markdown(exercice_code, force: bool = False):
    output_path = f'{CORRECTIONS_FOLDER}{exercice_code}.md'
    if not force and Path(output_path).exists():
        # print(chalk.blue(f'[Ignore] {chalk.bold(Path(output_path).name)} already exists.'))
        return
    content = f"""---
title: {exercice_code}
---

<div class="circle-ol" markdown>

</div>
"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
        print(chalk.green(f'[New] {Path(output_path).name} created.'))


def append_to_index(exercice_code: str, themes: str, force: bool = False):
    year = repere[:2]
    section_title = f"### Sujets 20{year}"
    table_line = get_table_line(exercice_code, themes)

    with open(INDEX_PATH, 'r+', encoding='utf-8') as f:
        content = f.readlines()
        try:
            idx = next(i for i, line in enumerate(content) if line.strip() == section_title)
        except StopIteration:
            print(chalk.red(f'[Error] Section {section_title} not found in index2.md'))
            return

        # Locate bounds of the table section (between ### and </div>)
        start = idx
        end = idx
        while end < len(content) and not content[end].strip().startswith("</div>"):
            end += 1

        if not force:
            for i in range(start, end):
                if exercice_code in content[i]:
                    # print(chalk.blue(f'[Ignore] {exercice_code} already in index.'))
                    return

        # Search for existing matching line within the section
        found_idx = None
        for i in range(start, end):
            if exercice_code in content[i]:
                if found_idx is None:
                    found_idx = i
                content[i] = None  # mark for deletion

        # Remove old lines if any
        content = [line for line in content if line is not None]

        if found_idx is not None:
            insert_pos = found_idx
            print(chalk.yellow(f'[Update] Replacing existing entry for {exercice_code}'))
        else:
            # Insert before </div>
            insert_pos = end if end < len(content) else len(content)
            print(chalk.green(f'[New] {exercice_code} added at end of table'))

        content.insert(insert_pos, table_line)
        f.seek(0)
        f.truncate()
        f.writelines(content)


for sujet in load_csv(METADATA_PATH):
    repere = sujet['repere']
    print(f'Sujet {chalk.bold(f"{repere}.pdf")}')
    pdf_path = f'{SUJETS_FOLDER}{repere}.pdf'
    for i in range(1, 4):
        exercice_code = f'{repere}-{i}'
        print(f'Exercice {chalk.bold(exercice_code)}')
        pages_indices = parse_page_ranges(sujet[f'page{i}'])
        output_path = f'{EXERCICES_FOLDER}{exercice_code}.pdf'
        extract_pages(pdf_path, pages_indices, output_path, force=False)
        write_markdown(exercice_code, force=False)
        append_to_index(exercice_code, sujet[f'theme{i}'], force=True)
