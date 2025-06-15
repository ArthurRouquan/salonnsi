

import os


def replace_curly_apostrophes_in_md_files(root_dir='.'):
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.md'):
                file_path = os.path.join(foldername, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()

                    updated_content = content.replace('’', "'")

                    if updated_content != content:
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(updated_content)
                        print(f"✅ Updated: {file_path}")
                    else:
                        print(f"— No change: {file_path}")
                except Exception as e:
                    print(f"❌ Error reading {file_path}: {e}")


# Lancer la fonction depuis le dossier courant
if __name__ == "__main__":
    replace_curly_apostrophes_in_md_files()
