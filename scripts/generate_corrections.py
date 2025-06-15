import sys
from pathlib import Path


def create_and_patch(base):
    corrections_dir = Path("docs/annales/corrections")
    corrections_dir.mkdir(parents=True, exist_ok=True)

    index_path = Path("docs/annales/index.md")
    if not index_path.exists():
        print("Erreur : index.md introuvable.")
        return

    with index_path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    updated_lines = []
    for line in lines:
        updated_line = line
        for i in range(1, 4):
            code = f"{base}-{i}"
            short = code[-3:]  # ex: AN1-1 → 1
            pdf_link = f"(exercices/{code}.pdf)"

            if pdf_link in line and "corrections/" not in line:
                # Créer le fichier correction si besoin
                file_path = corrections_dir / f"{code}.md"
                if not file_path.exists():
                    with file_path.open("w", encoding="utf-8") as f_md:
                        f_md.write(f"""---
title: {code}
---

<div class="circle-ol" markdown>

</div>
""")
                    print(f"Créé : {file_path}")

                # Ajouter le lien de correction dans la ligne
                correction_link = f"[:material-open-in-new:](corrections/{code}.md)"
                updated_line = line.replace("—", correction_link)
                print(f"Corrigé : {code}")
        updated_lines.append(updated_line)

    # Sauvegarde du fichier modifié
    with index_path.open("w", encoding="utf-8") as f:
        f.writelines(updated_lines)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py XXXXX")
    else:
        create_and_patch(sys.argv[1])
