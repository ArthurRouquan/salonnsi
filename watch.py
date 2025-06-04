import os
import time
import webbrowser
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# === CONFIGURATION ===
MKDOCS_BASE_URL = "http://127.0.0.1:8000"
DOCS_DIR = "docs"


class MarkdownChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".md"):
            self.print_url(event.src_path)

    def print_url(self, path):
        abs_docs = os.path.abspath(DOCS_DIR)
        abs_path = os.path.abspath(path)

        if not abs_path.startswith(abs_docs):
            return

        rel_path = os.path.relpath(abs_path, abs_docs)
        url_path = rel_path.replace("\\", "/").replace(".md", "/")
        if url_path == "index/":
            url_path = ""
        full_url = f"{MKDOCS_BASE_URL}/{url_path}"
        print(f"🔗 Page mise à jour : {full_url}")


if __name__ == "__main__":
    print("👀 Surveillance des fichiers .md dans 'docs/'...")
    event_handler = MarkdownChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=DOCS_DIR, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
