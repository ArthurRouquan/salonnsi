import os
import re
from collections import defaultdict

DOCS_DIR = "docs/annales/corrections/"


def parse_filename(filename):
    match = re.match(r"(?P<base>[\w-]+)-(?P<num>[1-3])\.md", filename)
    if not match:
        return None
    return match.group("base"), int(match.group("num"))


def generate_nav_block(base, num, filenames_by_base):
    filenames = filenames_by_base[base]
    filenames_sorted = sorted(filenames, key=lambda f: parse_filename(f)[1])

    current_index = num - 1
    prev_file = filenames_sorted[current_index - 1] if current_index > 0 else None
    next_file = filenames_sorted[current_index + 1] if current_index < 2 else None

    enonce_pdf = f"../exercices/{base}-{num}.pdf"
    sujet_pdf = f"../sujets/{base}.pdf"

    def link_info(file, base, direction="left"):
        if not file:
            if base.startswith("24-"):
                href = "../index.md/#sujets-2024"
            elif base.startswith("25-"):
                href = "../index.md/#sujets-2025"
            else:
                href = "../index.md"
            icon = ":material-home:" if direction == "right" else ":material-home:"
            return {"href": href, "icon": icon}
        return {
            "href": file,
            "icon": ":material-arrow-left:" if direction == "left" else ":material-arrow-right:"
        }

    prev = link_info(prev_file, base, direction="left")
    next = link_info(next_file, base, direction="right")

    return f'''
<!--NAVIGATION_START-->
<div class="center-button" markdown>
[{prev["icon"]}]({prev["href"]}){{ .md-button .nav-button }}
[:fontawesome-solid-file-pdf: &nbsp; Énoncé]({enonce_pdf}){{ .md-button }}
[:fontawesome-solid-file-pdf: &nbsp; Sujet]({sujet_pdf}){{ .md-button }}
[{next["icon"]}]({next["href"]}){{ .md-button .nav-button }}
</div>
<!--NAVIGATION_END-->
'''.strip()


def update_file_with_nav(path, nav_block):
    with open(path, encoding="utf-8") as f:
        content = f.read()

    # Supprimer un éventuel bloc NAV existant
    content = re.sub(
        r"<!--NAVIGATION_START-->.*?<!--NAVIGATION_END-->\n?",
        "",
        content,
        flags=re.DOTALL
    )

    # Trouver la fin du YAML (---)
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            yaml = parts[0] + '---' + parts[1] + '---'
            body = parts[2].lstrip()
            new_content = yaml + '\n\n' + nav_block + '\n\n' + body
        else:
            new_content = nav_block + '\n\n' + content
    else:
        new_content = nav_block + '\n\n' + content

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)


def main():
    files = sorted([
        f for f in os.listdir(DOCS_DIR) if re.match(r".+-[1-3]\.md", f)
    ])

    # Grouper par base (ex : 25-NSIJ1AN1)
    filenames_by_base = defaultdict(list)
    for f in files:
        parsed = parse_filename(f)
        if parsed:
            base, _ = parsed
            filenames_by_base[base].append(f)

    for base, filenames in filenames_by_base.items():
        for f in filenames:
            print(f)
            num = parse_filename(f)[1]
            nav_block = generate_nav_block(base, num, filenames_by_base)
            update_file_with_nav(os.path.join(DOCS_DIR, f), nav_block)

    print("✅ Navigation ajoutée à tous les exercices.")


if __name__ == "__main__":
    main()
